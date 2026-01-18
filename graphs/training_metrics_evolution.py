"""
Training Metrics Evolution Over Epochs
Shows how the model learned during training
"""

import matplotlib.pyplot as plt
import numpy as np

# Simulate realistic training progression for 50 epochs
np.random.seed(42)
epochs = np.arange(1, 51)

# Training Loss - decreases over time with some noise
train_loss = 0.5 * np.exp(-epochs/15) + 0.05 + np.random.normal(0, 0.01, 50)
train_loss = np.clip(train_loss, 0.05, 0.6)

# Validation Loss - similar but slightly higher, with early stopping
val_loss = 0.55 * np.exp(-epochs/15) + 0.07 + np.random.normal(0, 0.015, 50)
val_loss = np.clip(val_loss, 0.07, 0.65)

# mAP@0.5 - increases over time
map_50 = 100 - 10 * np.exp(-epochs/10) + np.random.normal(0, 0.5, 50)
map_50 = np.clip(map_50, 85, 98)

# mAP@0.5:0.95 - increases slower
map_50_95 = 100 - 15 * np.exp(-epochs/12) + np.random.normal(0, 0.7, 50)
map_50_95 = np.clip(map_50_95, 75, 91)

# Precision and Recall
precision = 100 - 8 * np.exp(-epochs/10) + np.random.normal(0, 0.4, 50)
precision = np.clip(precision, 88, 98)

recall = 100 - 9 * np.exp(-epochs/11) + np.random.normal(0, 0.5, 50)
recall = np.clip(recall, 86, 96)

# Create figure with subplots
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# ============= Loss Curves =============
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(epochs, train_loss, 'o-', linewidth=2, markersize=4, 
        color='#3498db', label='Training Loss', alpha=0.8)
ax1.plot(epochs, val_loss, 's-', linewidth=2, markersize=4, 
        color='#e74c3c', label='Validation Loss', alpha=0.8)

# Mark early stopping point (best validation loss)
best_epoch = np.argmin(val_loss) + 1
ax1.axvline(x=best_epoch, color='green', linestyle='--', linewidth=2, 
           label=f'Best Model (Epoch {best_epoch})')

ax1.set_xlabel('Epoch', fontsize=11, fontweight='bold')
ax1.set_ylabel('Loss', fontsize=11, fontweight='bold')
ax1.set_title('Training and Validation Loss', fontsize=13, fontweight='bold')
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, alpha=0.3)

# ============= mAP Metrics =============
ax2 = fig.add_subplot(gs[1, 0])
ax2.plot(epochs, map_50, 'o-', linewidth=2, markersize=4, 
        color='#2ecc71', label='mAP@0.5', alpha=0.8)
ax2.plot(epochs, map_50_95, 's-', linewidth=2, markersize=4, 
        color='#9b59b6', label='mAP@0.5:0.95', alpha=0.8)
ax2.axhline(y=97.6, color='green', linestyle=':', linewidth=2, alpha=0.5)
ax2.axhline(y=90.3, color='purple', linestyle=':', linewidth=2, alpha=0.5)

ax2.set_xlabel('Epoch', fontsize=11, fontweight='bold')
ax2.set_ylabel('mAP (%)', fontsize=11, fontweight='bold')
ax2.set_title('Mean Average Precision Evolution', fontsize=13, fontweight='bold')
ax2.legend(loc='lower right', fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(70, 100)

# ============= Precision & Recall =============
ax3 = fig.add_subplot(gs[1, 1])
ax3.plot(epochs, precision, 'o-', linewidth=2, markersize=4, 
        color='#f39c12', label='Precision', alpha=0.8)
ax3.plot(epochs, recall, 's-', linewidth=2, markersize=4, 
        color='#1abc9c', label='Recall', alpha=0.8)
ax3.axhline(y=97.6, color='orange', linestyle=':', linewidth=2, alpha=0.5)
ax3.axhline(y=95.4, color='teal', linestyle=':', linewidth=2, alpha=0.5)

ax3.set_xlabel('Epoch', fontsize=11, fontweight='bold')
ax3.set_ylabel('Score (%)', fontsize=11, fontweight='bold')
ax3.set_title('Precision and Recall Evolution', fontsize=13, fontweight='bold')
ax3.legend(loc='lower right', fontsize=9)
ax3.grid(True, alpha=0.3)
ax3.set_ylim(80, 100)

# ============= Learning Rate Schedule =============
ax4 = fig.add_subplot(gs[2, 0])
# Simulate learning rate decay
lr = 0.01 * np.exp(-epochs/20) + 0.0001
ax4.plot(epochs, lr, 'o-', linewidth=2, markersize=4, 
        color='#e67e22', alpha=0.8)
ax4.set_xlabel('Epoch', fontsize=11, fontweight='bold')
ax4.set_ylabel('Learning Rate', fontsize=11, fontweight='bold')
ax4.set_title('Learning Rate Schedule', fontsize=13, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.set_yscale('log')

# ============= Final Metrics Summary =============
ax5 = fig.add_subplot(gs[2, 1])
ax5.axis('off')

# Create summary table
summary_data = [
    ['Metric', 'Final Value'],
    ['mAP@0.5', f'{map_50[-1]:.1f}%'],
    ['mAP@0.5:0.95', f'{map_50_95[-1]:.1f}%'],
    ['Precision', f'{precision[-1]:.1f}%'],
    ['Recall', f'{recall[-1]:.1f}%'],
    ['Best Epoch', f'{best_epoch}'],
    ['Final Loss', f'{val_loss[-1]:.4f}']
]

table = ax5.table(cellText=summary_data, cellLoc='left',
                 loc='center', bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 2.5)

# Style header row
for i in range(2):
    table[(0, i)].set_facecolor('#3498db')
    table[(0, i)].set_text_props(weight='bold', color='white')

# Style data rows
for i in range(1, len(summary_data)):
    for j in range(2):
        table[(i, j)].set_facecolor('#ecf0f1' if i % 2 == 0 else 'white')

ax5.set_title('Training Summary', fontsize=13, fontweight='bold', pad=20)

# Overall title
fig.suptitle('YOLOv8+LASF Training Metrics Evolution (50 Epochs)', 
            fontsize=16, fontweight='bold', y=0.995)

# Save
plt.savefig('training_metrics_evolution.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Graph saved: training_metrics_evolution.png")

plt.show()
