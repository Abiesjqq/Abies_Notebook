
Aim: Target is what, it is doing what.

Training: **Train** model to classify short clips with low FPS.  
Testing: Run model on different clips, average predictions.

## Simple solutions

### Single-Frame CNN

Train normal 2D CNN to classify video frames independently. (Average predicted probs at test-time)

### Late Fusion

- (With FC Layers) CNN each frame, flatten together, and MLP
- (With Pooling) CNN each frame, average pool over space and time, and apply a linear layer.

### Early Fusion

Reshape $T \times 3 \times H \times W$ to $3T \times H \times W$, and sent it to a 2D CNN.

!!! waring-box "Problem"
    One layer of temporal processing may not be enough!

### 3D CNN



