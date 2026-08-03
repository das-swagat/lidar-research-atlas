# Choosing a dataset

## Selection matrix

| Question | Why it matters |
|---|---|
| 2D planar or 3D point cloud? | Determines sensor model, storage, representation, and compatible algorithms. |
| Indoor, outdoor, aerial, or mixed? | Controls geometry, range, occlusion, motion, and domain shift. |
| Raw scans or labeled benchmark? | Raw data may support SLAM but not supervised segmentation. |
| Which coordinate frames and calibration? | Reproducibility depends on transform conventions and timing. |
| Which license and permitted purpose? | Free access can still prohibit commercial use or redistribution. |
| Is evaluation server access required? | Test labels may remain private. |
| Are sparse/safety-critical classes represented? | Aggregate scores can hide weak minority-class performance. |
| Are geography, weather, and season diverse? | Narrow domains can overstate generalization. |

Do not choose solely by citation count. A specialized dataset may be the correct scientific choice even when it is less popular.
