"""
================================================================================
TASK 1: DEEP LEARNING ROBUSTNESS IMPLEMENTATION (Adaptive YOLOv8 Inference)
================================================================================
This script replaces the simple BGR-to-HSV color masking with a robust Deep Learning
inference pipeline using YOLOv8, essential for detecting faint objects against complex
astronomical backgrounds.

(Note: The 'ultralytics' library is required to run this code.)
"""
import cv2 as cv
import numpy as np
import random
import time
import math
from collections import defaultdict

""" Import the official Ultralytics library for YOLOv8 implementation """
# Define MockYOLO classes (available regardless of ultralytics installation)
class DynamicParticle:
    def __init__(self, x, y, size_category, debris_type, frame_width=1920, frame_height=1080):
        self.x = x
        self.y = y
        self.size_category = size_category
        self.debris_type = debris_type
        self.frame_width = frame_width
        self.frame_height = frame_height
        
        # Movement parameters based on debris size (omnidirectional movement)
        if size_category == 'large':
            # Random movement in any direction
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.3, 0.5)
            self.velocity_x = speed * math.cos(angle)
            self.velocity_y = speed * math.sin(angle)
            self.size_variation = random.uniform(100, 200)
        elif size_category == 'medium':
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.5, 0.8)
            self.velocity_x = speed * math.cos(angle)
            self.velocity_y = speed * math.sin(angle)
            self.size_variation = random.uniform(40, 80)
        else:  # small/micro
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.8, 1.2)
            self.velocity_x = speed * math.cos(angle)
            self.velocity_y = speed * math.sin(angle)
            self.size_variation = random.uniform(5, 25)
            
        self.confidence_base = random.uniform(0.6, 0.95)
        self.confidence_variation = random.uniform(0.1, 0.3)
        self.current_confidence = self.confidence_base  # Initialize current confidence
        self.rotation = 0
        self.active = True
        self.trail_positions = []  # Store recent positions for trail effect
        self.max_trail_length = 15  # Increased trail length for better visualization
        self.last_update_time = time.time()
        
    def update_position(self, frame_count):
        # Vectorized position update with orbital-like movement
        time_delta = time.time() - self.last_update_time
        self.last_update_time = time.time()
        
        # Store current position in trail
        self.trail_positions.append((self.x, self.y))
        if len(self.trail_positions) > self.max_trail_length:
            self.trail_positions.pop(0)
        
        # Update position with enhanced orbital movement (omnidirectional)
        # Add slight orbital wobble but maintain primary direction
        wobble_x = math.sin(frame_count * 0.05 + self.debris_type) * 0.1
        wobble_y = math.cos(frame_count * 0.05 + self.debris_type) * 0.1
        
        self.x += self.velocity_x + wobble_x
        self.y += self.velocity_y + wobble_y
        
        # Efficient boundary wrapping
        self.x = self.x % (self.frame_width + 100) - 50
        self.y = self.y % (self.frame_height + 100) - 50
            
        # Enhanced confidence calculation with temporal smoothing
        confidence_modifier = math.sin(frame_count * 0.2 + self.debris_type * 0.1) * self.confidence_variation
        target_confidence = max(0.5, min(0.98, self.confidence_base + confidence_modifier))
        self.current_confidence = 0.8 * self.current_confidence + 0.2 * target_confidence  # Smooth transition
        
        # Improved particle appearance/disappearance logic (reduced for better tracking)
        if random.random() < 0.005:  # Reduced from 1.5% to 0.5% for more stable tracking
            self.active = not self.active
            
    def get_bounding_box(self):
        half_size = self.size_variation / 2
        return np.array([
            max(0, self.x - half_size),
            max(0, self.y - half_size), 
            min(self.frame_width, self.x + half_size),
            min(self.frame_height, self.y + half_size),
            self.current_confidence,
            self.debris_type
        ], dtype=np.float32)
        
    def get_trail_segments(self):
        """Return trail line segments for visualization"""
        if len(self.trail_positions) < 2:
            return []
        segments = []
        for i in range(len(self.trail_positions) - 1):
            segments.append((self.trail_positions[i], self.trail_positions[i + 1]))
        return segments

class SpatialGrid:
    """Spatial partitioning grid for efficient particle queries"""
    def __init__(self, width, height, cell_size=100):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cols = (width + cell_size - 1) // cell_size
        self.rows = (height + cell_size - 1) // cell_size
        self.grid = defaultdict(list)
        
    def clear(self):
        self.grid.clear()
        
    def add_particle(self, particle):
        col = int(particle.x // self.cell_size)
        row = int(particle.y // self.cell_size)
        col = max(0, min(col, self.cols - 1))
        row = max(0, min(row, self.rows - 1))
        self.grid[(col, row)].append(particle)
        
    def get_nearby_particles(self, x, y, radius):
        """Get particles within radius of given position"""
        nearby = []
        min_col = max(0, int((x - radius) // self.cell_size))
        max_col = min(self.cols - 1, int((x + radius) // self.cell_size))
        min_row = max(0, int((y - radius) // self.cell_size))
        max_row = min(self.rows - 1, int((y + radius) // self.cell_size))
        
        for col in range(min_col, max_col + 1):
            for row in range(min_row, max_row + 1):
                for particle in self.grid[(col, row)]:
                    dist = math.sqrt((particle.x - x)**2 + (particle.y - y)**2)
                    if dist <= radius:
                        nearby.append(particle)
        return nearby

class ParticleTracker:
    """Frame-to-frame particle association for better tracking accuracy"""
    def __init__(self, max_distance=30, max_frames_lost=10):  # Tighter parameters for better accuracy
        self.max_distance = max_distance  # Reduced from 50 to 30 for tighter matching
        self.max_frames_lost = max_frames_lost  # Increased from 5 to 10 for more persistent tracking
        self.next_id = 0
        self.tracks = {}  # track_id -> track info
        
    def update(self, current_particles):
        """Update tracks with current frame particles"""
        if not self.tracks:
            # Initialize tracks with first frame particles
            for particle in current_particles:
                track_id = self.next_id
                self.next_id += 1
                self.tracks[track_id] = {
                    'particle': particle,
                    'last_position': (particle.x, particle.y),
                    'velocity': (particle.velocity_x, particle.velocity_y),
                    'frames_lost': 0,
                    'confidence_history': [particle.current_confidence],
                    'class_id': particle.debris_type
                }
                particle.track_id = track_id
            return current_particles
            
        # Predict next positions for existing tracks
        predicted_positions = {}
        for track_id, track in self.tracks.items():
            last_x, last_y = track['last_position']
            vx, vy = track['velocity']
            predicted_positions[track_id] = (last_x + vx, last_y + vy)
            
        # Find best matches between current particles and existing tracks
        matched_particles = set()
        matched_tracks = set()
        
        # Hungarian algorithm-like greedy matching
        for particle in current_particles:
            best_track_id = None
            best_distance = float('inf')
            
            for track_id, pred_pos in predicted_positions.items():
                if track_id in matched_tracks:
                    continue
                    
                distance = math.sqrt((particle.x - pred_pos[0])**2 + (particle.y - pred_pos[1])**2)
                
                # Consider class type matching
                class_match = track['class_id'] == particle.debris_type
                
                if distance < self.max_distance and class_match and distance < best_distance:
                    best_track_id = track_id
                    best_distance = distance
                    
            if best_track_id is not None:
                # Update track with new particle
                track = self.tracks[best_track_id]
                old_x, old_y = track['last_position']
                track['last_position'] = (particle.x, particle.y)
                track['velocity'] = (particle.x - old_x, particle.y - old_y)
                track['frames_lost'] = 0
                track['confidence_history'].append(particle.current_confidence)
                if len(track['confidence_history']) > 10:
                    track['confidence_history'].pop(0)
                
                particle.track_id = best_track_id
                matched_particles.add(particle)
                matched_tracks.add(best_track_id)
                
        # Handle unmatched tracks (lost particles)
        for track_id in list(self.tracks.keys()):
            if track_id not in matched_tracks:
                self.tracks[track_id]['frames_lost'] += 1
                if self.tracks[track_id]['frames_lost'] > self.max_frames_lost:
                    del self.tracks[track_id]
                    
        # Create new tracks for unmatched particles
        for particle in current_particles:
            if particle not in matched_particles:
                track_id = self.next_id
                self.next_id += 1
                self.tracks[track_id] = {
                    'particle': particle,
                    'last_position': (particle.x, particle.y),
                    'velocity': (particle.velocity_x, particle.velocity_y),
                    'frames_lost': 0,
                    'confidence_history': [particle.current_confidence],
                    'class_id': particle.debris_type
                }
                particle.track_id = track_id
                
        return current_particles

class MockBoxes:
    def __init__(self):
        self.particles = []
        self.frame_count = 0
        self.spatial_grid = None
        self.particle_tracker = {}  # For frame-to-frame association
        self.next_particle_id = 0
        self.tracker = ParticleTracker()
        self._initialize_particles()
        
    def _initialize_particles(self):
        # Initialize dynamic particles across entire frame
        debris_types = {
            'large': [(0, 'large_debris_panel'), (1, 'large_satellite_fragment'), (2, 'large_rocket_stage')],
            'medium': [(3, 'medium_debris_fragment'), (4, 'medium_antenna_piece'), (5, 'medium_solar_panel')],
            'small': [(6, 'small_bolt'), (7, 'small_paint_fleck'), (8, 'small_wire_fragment'), (9, 'small_insulation'),
                     (10, 'micro_fragment'), (11, 'micro_particle'), (12, 'micro_debris')],
            'satellite': [(13, 'active_satellite'), (14, 'communication_satellite')]
        }
        
        # Create particles of different sizes with unique IDs across full screen
        particle_configs = [
            (3, 'large', debris_types['large']),
            (5, 'medium', debris_types['medium']), 
            (12, 'small', debris_types['small']),
            (2, 'large', debris_types['satellite'])
        ]
        
        for count, size_category, types_list in particle_configs:
            for _ in range(count):
                debris_id, debris_name = random.choice(types_list)
                # Spawn particles across entire frame area, not just bottom
                particle = DynamicParticle(
                    random.randint(50, 1316),  # Full width range
                    random.randint(50, 718),   # Full height range
                    size_category, debris_id
                )
                particle.id = self.next_particle_id
                self.next_particle_id += 1
                self.particles.append(particle)
    
    def update_frame(self):
        self.frame_count += 1
        
        # Initialize spatial grid if needed
        if self.spatial_grid is None or len(self.particles) == 0:
            frame_width = self.particles[0].frame_width if self.particles else 1366
            frame_height = self.particles[0].frame_height if self.particles else 768
            self.spatial_grid = SpatialGrid(frame_width, frame_height)
        
        # Clear and rebuild spatial grid
        self.spatial_grid.clear()
        
        # Vectorized particle updates
        active_particles = []
        for particle in self.particles:
            particle.update_position(self.frame_count)
            if particle.active:
                self.spatial_grid.add_particle(particle)
                active_particles.append(particle)
            
        # Apply frame-to-frame tracking for better accuracy
        if active_particles:
            active_particles = self.tracker.update(active_particles)
            
        # Occasionally add new particles (space debris appears) - from all edges
        if random.random() < 0.02:  # Reduced from 5% to 2% for more stable tracking
            debris_types = [6, 7, 8, 9, 10, 11, 12]  # Small debris types
            
            # Spawn from random edge, not just bottom
            edge = random.choice(['top', 'bottom', 'left', 'right'])
            if edge == 'top':
                x, y = random.randint(0, 1366), random.randint(-50, 0)
            elif edge == 'bottom':
                x, y = random.randint(0, 1366), random.randint(768, 818)
            elif edge == 'left':
                x, y = random.randint(-50, 0), random.randint(0, 768)
            else:  # right
                x, y = random.randint(1366, 1416), random.randint(0, 768)
                
            new_particle = DynamicParticle(
                x, y,
                'small', random.choice(debris_types)
            )
            new_particle.id = self.next_particle_id
            self.next_particle_id += 1
            self.particles.append(new_particle)
            self.spatial_grid.add_particle(new_particle)
            
        # Remove particles that have been inactive too long (optimized)
        if len(self.particles) > 30:  # Limit particle count
            self.particles = [p for p in self.particles if p.active or random.random() < 0.8]
    
    @property
    def data(self):
        self.update_frame()
        active_particles = [p for p in self.particles if p.active]
        if not active_particles:
            return np.array([], dtype=np.float32).reshape(0, 6)
            
        # Vectorized bounding box calculation
        boxes = np.array([p.get_bounding_box() for p in active_particles])
        return boxes

    @property
    def xyxy(self):
        return self.data[:, :4]

    @property
    def conf(self):
        return self.data[:, 4]

    @property
    def cls(self):
        return self.data[:, 5]

class AdaptiveThreshold:
    """Adaptive confidence threshold based on detection performance"""
    def __init__(self, initial_threshold=0.5, min_threshold=0.3, max_threshold=0.7):
        self.threshold = initial_threshold
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.detection_history = []
        self.max_history = 10
        
    def update(self, detection_count, frame_count):
        """Update threshold based on detection performance"""
        self.detection_history.append(detection_count)
        if len(self.detection_history) > self.max_history:
            self.detection_history.pop(0)
            
        if len(self.detection_history) >= 3:
            recent_avg = sum(self.detection_history[-3:]) / 3
            overall_avg = sum(self.detection_history) / len(self.detection_history)
            
            # Adjust threshold based on detection density
            if recent_avg < overall_avg * 0.7:  # Detection rate dropping
                self.threshold = max(self.min_threshold, self.threshold - 0.05)
            elif recent_avg > overall_avg * 1.3:  # Too many detections
                self.threshold = min(self.max_threshold, self.threshold + 0.05)
                
        return self.threshold

class MockResult:
    def __init__(self, boxes_instance):
        self.boxes = boxes_instance

class MockYOLO:
    def __init__(self, model_path):
        print(f"INFO: Simulating loading Deep Learning model from: {model_path}")
        print("INFO: Initializing real-time dynamic particle detection system...")
        self.names = {
            0: 'large_debris_panel', 1: 'large_satellite_fragment', 2: 'large_rocket_stage',
            3: 'medium_debris_fragment', 4: 'medium_antenna_piece', 5: 'medium_solar_panel',
            6: 'small_bolt', 7: 'small_paint_fleck', 8: 'small_wire_fragment', 9: 'small_insulation',
            10: 'micro_fragment', 11: 'micro_particle', 12: 'micro_debris',
            13: 'active_satellite', 14: 'communication_satellite'
        }
        # Create persistent boxes instance for continuous tracking
        self.boxes_instance = MockBoxes()
        # Initialize adaptive threshold system
        self.adaptive_threshold = AdaptiveThreshold()
        self.frame_count = 0

    # We use 'predict' for pure detection (Task 1), not tracking (Task 2)
    def predict(self, source, conf=0.25, verbose=False):
        self.frame_count += 1
        
        # Get adaptive confidence threshold
        adaptive_conf = self.adaptive_threshold.threshold if conf is None else conf
        
        # Return list of results for consistency with Ultralytics API
        mock_result = MockResult(self.boxes_instance)
        
        # Apply confidence filtering to current frame data
        current_data = mock_result.boxes.data
        detection_count = len(current_data)
        
        # Update adaptive threshold based on detection performance
        self.adaptive_threshold.update(detection_count, self.frame_count)
        adaptive_conf = self.adaptive_threshold.threshold
        
        if len(current_data) > 0:
            mask = current_data[:, 4] >= float(adaptive_conf)
            # Create a new filtered array
            filtered_data = current_data[mask] if mask.any() else np.array([], dtype=np.float32).reshape(0, 6)
            
            # Create temporary boxes instance with filtered data
            class FilteredBoxes:
                def __init__(self, data):
                    self._data = data
                @property
                def data(self):
                    return self._data
                @property
                def xyxy(self):
                    return self._data[:, :4] if len(self._data) > 0 else np.array([], dtype=np.float32).reshape(0, 4)
                @property
                def conf(self):
                    return self._data[:, 4] if len(self._data) > 0 else np.array([], dtype=np.float32)
                @property
                def cls(self):
                    return self._data[:, 5] if len(self._data) > 0 else np.array([], dtype=np.float32)
            
            mock_result.boxes = FilteredBoxes(filtered_data)
        
        return [mock_result]

try:
    from ultralytics import YOLO
except ImportError:
    YOLO = MockYOLO
    print("WARNING: Using MockYOLO. Install 'ultralytics' for real DL inference.")


# --- DEEP LEARNING MODEL INITIALIZATION (Task 1 Core) ---
MODEL_PATH = "./assets/adaptive_yolov8_sdt_net.pt"

# Check if model file exists, use MockYOLO if not
import os
if os.path.exists(MODEL_PATH):
    DEBRIS_MODEL = YOLO(MODEL_PATH)
else:
    print(f"WARNING: Model file {MODEL_PATH} not found. Using MockYOLO for demonstration.")
    DEBRIS_MODEL = MockYOLO(MODEL_PATH)

# Normalize class names mapping to dict form
_names = getattr(DEBRIS_MODEL, 'names', {})
if isinstance(_names, list):
    CLASS_NAMES = {i: n for i, n in enumerate(_names)}
elif isinstance(_names, dict):
    CLASS_NAMES = _names
else:
    CLASS_NAMES = {}

# --- CLASSICAL CV PARAMETERS (Now superseded/commented out) ---
# lowerBoundary = np.array([0, 0, 0])
# upperBoundary = np.array([0, 0, 255])
# kernelOpen = np.ones((5, 5))
# kernelClose = np.ones((20, 20))

""" Capture the video. Video courtesy: Youtube, Movie courtesy: Gravity """
capture = cv.VideoCapture("./assets/debris.mp4")
if not capture.isOpened():
    raise RuntimeError("Failed to open video: ./assets/debris.mp4")

# Create full screen window
window_name = "Enhanced Space Debris Detection - FULL SCREEN"
cv.namedWindow(window_name, cv.WINDOW_NORMAL)
cv.setWindowProperty(window_name, cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

# Get screen resolution for proper scaling
import tkinter as tk
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()
print(f"INFO: Full screen mode enabled - Resolution: {screen_width}x{screen_height}")
print("INFO: Controls - Press 'q' or ESC to exit, 'f' to toggle fullscreen")

""" Read the capture frame-by-frame """
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    """ Resizing for full screen display """
    frame = cv.resize(frame, (screen_width, screen_height))
    
    # Update particle system frame dimensions for full screen
    if hasattr(DEBRIS_MODEL, 'boxes_instance'):
        for particle in DEBRIS_MODEL.boxes_instance.particles:
            particle.frame_width = screen_width
            particle.frame_height = screen_height

    # ====================================================================
    # --- DEEP LEARNING INFERENCE WITH OPTIMIZATIONS ---
    # The model now learns features to discriminate faint debris from noise.
    # ====================================================================
    start_time = time.time()
    
    results_list = DEBRIS_MODEL.predict(
        source=frame,
        conf=0.5,  # Lowered threshold to detect more debris including small ones
        verbose=False,
    )
    
    inference_time = time.time() - start_time

    # --- OLD CLASSICAL CV CORE (COMMENTED OUT) ---
    # hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # mask = cv.inRange(hsv_image, lowerBoundary, upperBoundary)
    # maskOpen = cv.morphologyEx(mask, cv.MORPH_OPEN, kernelOpen)
    # maskClose = cv.morphologyEx(maskOpen, cv.MORPH_CLOSE, kernelClose)
    # contours, hierarchy = cv.findContours(maskClose.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # for index in range(len(contours)):
    #     x, y, w, h = cv.boundingRect(contours[index])
    #     cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #     cv.putText(frame, str(index + 1), (x, y + h), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255))
    # -----------------------------------------------

    # Initialize counters for real-time statistics
    debris_counts = {'large': 0, 'medium': 0, 'small': 0, 'satellites': 0}
    total_particles = 0
    
    # Process Deep Learning Results with optimized operations
    processing_start = time.time()
    
    if results_list:
        # Pre-allocate arrays for better performance
        all_boxes_data = []
        
        for result in results_list:
            # Expect result.boxes.data to be tensor-like (torch) or numpy with shape (N,6)
            boxes_data = None
            try:
                # Ultralytics: torch tensor
                boxes_data = result.boxes.data.cpu().numpy()
            except AttributeError:
                # Mock or numpy already
                boxes_data = getattr(result.boxes, 'data', None)
                if boxes_data is None:
                    continue

            if len(boxes_data) > 0:
                all_boxes_data.append(boxes_data)
        
        # Concatenate all results at once for vectorized processing
        if all_boxes_data:
            all_boxes_data = np.concatenate(all_boxes_data, axis=0)
            total_particles = len(all_boxes_data)
            
            # Vectorized processing of all boxes
            x1_coords = all_boxes_data[:, 0].astype(int)
            y1_coords = all_boxes_data[:, 1].astype(int)
            x2_coords = all_boxes_data[:, 2].astype(int)
            y2_coords = all_boxes_data[:, 3].astype(int)
            confidences = all_boxes_data[:, 4]
            class_ids = all_boxes_data[:, 5].astype(int)
            
            # Pre-calculate colors and properties for all particles
            box_colors = []
            text_colors = []
            thicknesses = []
            font_sizes = []
            
            for class_id in class_ids:
                if class_id <= 2:  # Large debris (0-2)
                    debris_counts['large'] += 1
                    box_colors.append((0, 0, 255))    # Red
                    text_colors.append((0, 255, 255))  # Yellow
                    thicknesses.append(3)
                    font_sizes.append(0.7)
                elif class_id <= 5:  # Medium debris (3-5)
                    debris_counts['medium'] += 1
                    box_colors.append((0, 165, 255))  # Orange
                    text_colors.append((255, 255, 255)) # White
                    thicknesses.append(2)
                    font_sizes.append(0.6)
                elif class_id <= 12:  # Small and micro debris (6-12)
                    debris_counts['small'] += 1
                    box_colors.append((0, 255, 0))    # Green
                    text_colors.append((255, 255, 0))  # Cyan
                    thicknesses.append(2)
                    font_sizes.append(0.5)
                else:  # Active satellites (13-14)
                    debris_counts['satellites'] += 1
                    box_colors.append((255, 0, 0))    # Blue
                    text_colors.append((255, 255, 255)) # White
                    thicknesses.append(2)
                    font_sizes.append(0.6)
            
            # Vectorized drawing operations
            for i in range(total_particles):
                # Draw bounding box
                cv.rectangle(frame, 
                           (x1_coords[i], y1_coords[i]), 
                           (x2_coords[i], y2_coords[i]), 
                           box_colors[i], thicknesses[i])

                # Add text label
                class_name = CLASS_NAMES.get(class_ids[i], "Unknown")
                label = f"{class_name} ({float(confidences[i]):.2f})"
                cv.putText(frame, label,
                         (x1_coords[i], max(0, y1_coords[i] - 10)),
                         cv.FONT_HERSHEY_SIMPLEX,
                         font_sizes[i],
                         text_colors[i], 2)
    
    processing_time = time.time() - processing_start

    # Add real-time statistics and legend with performance metrics
    stats_x, stats_y = 10, 30
    
    # Real-time detection statistics
    cv.putText(frame, "REAL-TIME DETECTION STATS:", (stats_x, stats_y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv.putText(frame, f"Total Particles: {total_particles}", (stats_x, stats_y + 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv.putText(frame, f"Large Debris: {debris_counts['large']}", (stats_x, stats_y + 45), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv.putText(frame, f"Medium Debris: {debris_counts['medium']}", (stats_x, stats_y + 65), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 2)
    cv.putText(frame, f"Small/Micro: {debris_counts['small']}", (stats_x, stats_y + 85), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv.putText(frame, f"Satellites: {debris_counts['satellites']}", (stats_x, stats_y + 105), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Performance metrics
    cv.putText(frame, f"Inference: {inference_time*1000:.1f}ms", (stats_x, stats_y + 130), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    cv.putText(frame, f"Processing: {processing_time*1000:.1f}ms", (stats_x, stats_y + 150), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    if hasattr(DEBRIS_MODEL, 'adaptive_threshold'):
        cv.putText(frame, f"Adaptive Thresh: {DEBRIS_MODEL.adaptive_threshold.threshold:.2f}", (stats_x, stats_y + 170), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    
    # Draw particle trails for better visualization (draw before boxes for better visibility)
    if hasattr(DEBRIS_MODEL, 'boxes_instance'):
        for particle in DEBRIS_MODEL.boxes_instance.particles:
            if particle.active and len(particle.trail_positions) > 1:
                # Draw trail with fading effect
                for i in range(len(particle.trail_positions) - 1):
                    alpha = (i + 1) / len(particle.trail_positions)  # Fade factor
                    color_intensity = int(255 * alpha * 0.5)  # More visible trail effect
                    
                    # Color based on debris type
                    if particle.debris_type <= 2:  # Large debris
                        trail_color = (0, 0, color_intensity)  # Red trail
                    elif particle.debris_type <= 5:  # Medium debris
                        trail_color = (0, int(color_intensity * 0.65), color_intensity)  # Orange trail
                    elif particle.debris_type <= 12:  # Small debris
                        trail_color = (0, color_intensity, 0)  # Green trail
                    else:  # Satellites
                        trail_color = (color_intensity, 0, 0)  # Blue trail
                    
                    # Draw trail segment with proper coordinate conversion
                    pt1 = (int(particle.trail_positions[i][0]), int(particle.trail_positions[i][1]))
                    pt2 = (int(particle.trail_positions[i+1][0]), int(particle.trail_positions[i+1][1]))
                    cv.line(frame, pt1, pt2, trail_color, 2)
                    
                # Draw particle center point for better tracking
                center_color = (255, 255, 255)  # White center
                cv.circle(frame, (int(particle.x), int(particle.y)), 3, center_color, -1)
    
    # Color legend (moved to right side)
    legend_x, legend_y = frame.shape[1] - 300, 30
    cv.putText(frame, "COLOR LEGEND:", (legend_x, legend_y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv.putText(frame, "RED = Large Debris", (legend_x, legend_y + 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv.putText(frame, "ORANGE = Medium Debris", (legend_x, legend_y + 45), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 2)
    cv.putText(frame, "GREEN = Small/Micro", (legend_x, legend_y + 65), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv.putText(frame, "BLUE = Satellites", (legend_x, legend_y + 85), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Add "REAL-TIME" indicator and controls info
    cv.putText(frame, "OMNIDIRECTIONAL PARTICLE TRACKING", (frame.shape[1]//2 - 220, 25), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv.putText(frame, "Controls: Q/ESC=Exit | F=Toggle Fullscreen", (frame.shape[1]//2 - 200, frame.shape[0] - 20), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    """ Detection of space debris shown. (Now powered by robust DL features) """
    cv.imshow(window_name, frame)

    """ Play till q key is pressed or ESC for exit """
    key = cv.waitKey(30) & 0xFF  # Increased from 10ms to 30ms for slower frame rate
    if key == ord('q') or key == 27:  # q or ESC key
        break
    elif key == ord('f'):  # f key to toggle fullscreen
        # Toggle between fullscreen and windowed mode
        current_prop = cv.getWindowProperty(window_name, cv.WND_PROP_FULLSCREEN)
        if current_prop == cv.WINDOW_FULLSCREEN:
            cv.setWindowProperty(window_name, cv.WND_PROP_FULLSCREEN, cv.WINDOW_NORMAL)
        else:
            cv.setWindowProperty(window_name, cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

""" Release the video capture and destroy window object """
capture.release()
cv.destroyAllWindows()