# 3D LiDAR perception

![Conceptual 3D perception pipeline](../assets/images/perception-pipeline.svg)

LiDAR perception pipelines commonly validate sensor frames, compensate motion, transform coordinates, represent points as raw neighborhoods, voxels, pillars, range images, or hybrids, learn features, predict task outputs, and evaluate with dataset-specific protocols.

Representation changes alter quantization, neighborhood structure, memory, latency, and domain-transfer behavior. Benchmark values are comparable only when splits, label maps, preprocessing, and metrics align.
