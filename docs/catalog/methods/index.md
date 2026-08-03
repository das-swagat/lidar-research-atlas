# Method catalog

<div class="atlas-stat-grid"><div><strong>53</strong><span>method records</span></div><div><strong>25</strong><span>verified</span></div><div><strong>26</strong><span>discovery-only</span></div></div>

Methods cover point representations, semantic and moving-object segmentation, 3D detection, ground segmentation, registration, SLAM, odometry, place recognition, self-supervised learning, and sensor calibration.

<div class="atlas-filter"><input type="search" data-atlas-filter="method-table" placeholder="Filter methods by name, category, representation, year, or status…" aria-label="Filter methods by name, category, representation, year, or status…"></div>

<div id="method-table">

| Method | Year | Category | Representation | Source relationship | Status |
|---|---:|---|---|---|---|
| [Automatic Urban Point-Cloud Labelling by Data Fusion](automatic-urban-point-cloud-labelling-by-data-fusion.md) | 2020 | semantic segmentation | multi-sensor data fusion and automatic labels | `official_or_author_maintained_unverified` | `discovery_only` |
| [Cylinder3D](cylinder3d.md) | 2021 | LiDAR semantic segmentation | cylindrical voxel partition and sparse convolution | `official_or_author_maintained` | `verified` |
| [DepthContrast](depthcontrast.md) | 2021 | Self-supervised 3D learning | contrastive learning from depth/point clouds | `official_or_author_maintained` | `partial` |
| [detection_by_tracker](detection-by-tracker.md) | 2020 | 3D multi-object tracking | tracking-driven detection | `official_or_author_maintained_unverified` | `discovery_only` |
| [Direct Visual-LiDAR Calibration](direct-visual-lidar-calibration.md) | 2023 | sensor calibration | targetless direct visual-LiDAR alignment | `official_or_author_maintained_unverified` | `discovery_only` |
| [FAST-LIO2](fast-lio2.md) | 2022 | LiDAR-inertial odometry | direct point-to-map, iterated Kalman filter | `official_or_author_maintained` | `verified` |
| [Frustum PointNets](frustum-pointnets.md) | 2018 | 3D object detection | RGB-D frustums and point networks | `official_or_author_maintained_unverified` | `discovery_only` |
| [GMapping / OpenSLAM GMapping](gmapping.md) | 2007 | 2D SLAM | Rao-Blackwellized particle filter | `canonical_project_page` | `verified` |
| [Google Cartographer](cartographer.md) | 2016 | 2D/3D SLAM | submaps, scan matching, pose graph | `official_or_author_maintained` | `verified` |
| [GSeg3D](gseg3d.md) | 2025 | ground segmentation | grid-based high-precision segmentation | `official_or_author_maintained_unverified` | `discovery_only` |
| [Hector SLAM](hector-slam.md) | 2011 | 2D SLAM | scan matching without wheel odometry | `official_or_author_maintained` | `verified` |
| [Heteroscedastic Aleatoric LiDAR 3D Detection](heteroscedastic-aleatoric-lidar-3d-detection.md) | 2019 | 3D object detection | uncertainty-aware detection | `official_or_author_maintained_unverified` | `discovery_only` |
| [KISS-ICP](kiss-icp.md) | 2023 | LiDAR odometry | adaptive point-to-point ICP | `official_or_author_maintained_unverified` | `discovery_only` |
| [KISS-SLAM](kiss-slam.md) | 2025 | 3D LiDAR SLAM | KISS-ICP-based mapping and loop closure | `official_or_author_maintained_unverified` | `discovery_only` |
| [KPConv](kpconv.md) | 2019 | 3D semantic segmentation | kernel point convolution | `official_or_author_maintained` | `verified` |
| [LaserMix](lasermix.md) | 2023 | Semi-supervised LiDAR segmentation | scene mixing with spatial priors | `official_or_author_maintained` | `verified` |
| [Learning to Optimally Segment Point Clouds](learning-to-optimally-segment-point-clouds.md) | 2020 | 3D instance segmentation | learned point-cloud segmentation | `official_or_author_maintained_unverified` | `discovery_only` |
| [LeGO-LOAM](lego-loam.md) | 2018 | LiDAR odometry and mapping | ground-optimized feature-based LiDAR | `official_or_author_maintained` | `verified` |
| [libpointmatcher](libpointmatcher.md) | 2013 | point-cloud registration | modular ICP variants | `official_or_author_maintained_unverified` | `discovery_only` |
| [LiDAR-MOS](lidar-mos.md) | 2021 | moving-object segmentation | range-image residuals and semantic segmentation | `official_or_author_maintained_unverified` | `discovery_only` |
| [LineFit Ground Segmentation](linefit-ground-segmentation.md) | 2017 | ground segmentation | radial line fitting | `official_or_author_maintained_unverified` | `discovery_only` |
| [LIO-SAM](lio-sam.md) | 2020 | LiDAR-inertial odometry | factor graph, LiDAR and IMU | `official_or_author_maintained` | `verified` |
| [LOAM](loam.md) | 2014 | LiDAR odometry and mapping | feature-based 3D LiDAR | `community_reimplementation` | `verified` |
| [MaskPoint](maskpoint.md) | 2022 | Self-supervised 3D learning | masked point discrimination | `official_or_author_maintained` | `partial` |
| [MinkowskiEngine](minkowski-engine.md) | 2019 | Sparse 3D deep learning | generalized sparse convolution | `official_framework` | `verified` |
| [MOLA](mola.md) | 2024 | SLAM and localization framework | modular LiDAR odometry, SLAM, and georeferencing | `official_or_author_maintained_unverified` | `discovery_only` |
| [OpenCalib](opencalib.md) | 2022 | sensor calibration | multi-sensor calibration toolbox | `official_or_author_maintained_unverified` | `discovery_only` |
| [OverlapNet](overlapnet.md) | 2020 | place recognition and loop closure | range-image overlap prediction | `official_or_author_maintained_unverified` | `discovery_only` |
| [Patchwork](patchwork.md) | 2021 | ground segmentation | region-wise plane fitting | `official_or_author_maintained_unverified` | `discovery_only` |
| [Patchwork++](patchwork-plusplus.md) | 2022 | ground segmentation | robust region-wise plane fitting | `official_or_author_maintained_unverified` | `discovery_only` |
| [Plane Seg](plane-seg.md) | 2017 | ground segmentation | plane fitting for LiDAR | `official_or_author_maintained_unverified` | `discovery_only` |
| [Point Transformer](point-transformer.md) | 2021 | 3D representation learning | vector attention over point neighborhoods | `official_or_author_maintained` | `verified` |
| [Point-BERT](point-bert.md) | 2022 | Self-supervised 3D learning | masked point-token modeling | `official_or_author_maintained` | `verified` |
| [Point-MAE](point-mae.md) | 2022 | Self-supervised 3D learning | masked autoencoding for point clouds | `official_or_author_maintained` | `verified` |
| [PointNet](pointnet.md) | 2017 | 3D representation learning | raw points, shared MLP, symmetric aggregation | `official_or_author_maintained` | `verified` |
| [PointNet++](pointnet2.md) | 2017 | 3D representation learning | hierarchical point neighborhoods | `official_or_author_maintained` | `verified` |
| [PointNeXt](pointnext.md) | 2022 | 3D representation learning | modernized PointNet++ design | `official_or_author_maintained` | `verified` |
| [PointPillars](pointpillars.md) | 2019 | 3D object detection | pillarized point cloud pseudo-image | `framework_integration` | `verified` |
| [PolarNet](polarnet.md) | 2020 | LiDAR semantic segmentation | polar bird’s-eye-view grid | `official_or_author_maintained` | `verified` |
| [PV-RCNN](pv-rcnn.md) | 2020 | 3D object detection | point-voxel feature aggregation | `official_or_framework_integration` | `verified` |
| [RandLA-Net](randlanet.md) | 2020 | 3D semantic segmentation | random sampling and local feature aggregation | `official_or_author_maintained` | `verified` |
| [RangeNet++](rangenetpp.md) | 2019 | LiDAR semantic segmentation | range image projection and post-processing | `official_or_author_maintained` | `verified` |
| [Removert](removert.md) | 2020 | mapping and dynamic-object removal | multi-resolution range images | `official_or_author_maintained_unverified` | `discovery_only` |
| [RESPLE](resple.md) | 2025 | LiDAR odometry | recursive spline estimation | `official_or_author_maintained_unverified` | `discovery_only` |
| [SalsaNext](salsanext.md) | 2020 | LiDAR semantic segmentation | uncertainty-aware range image CNN | `official_or_author_maintained` | `verified` |
| [simpleICP](simpleicp.md) | 2019 | point-cloud registration | point-to-point iterative closest point | `official_or_author_maintained_unverified` | `discovery_only` |
| [SphereFormer](sphereformer.md) | 2023 | LiDAR semantic segmentation | spherical transformer windows | `official_or_author_maintained` | `verified` |
| [SPVNAS / SPVCNN](spvnas.md) | 2020 | Efficient 3D perception | sparse point-voxel convolution | `official_or_author_maintained` | `verified` |
| [SuMa++](suma-plusplus.md) | 2019 | semantic SLAM | surfel mapping with semantic labels | `official_or_author_maintained_unverified` | `discovery_only` |
| [Superpoint Graph](superpoint-graph.md) | 2018 | semantic segmentation | superpoint partition and graph neural network | `official_or_author_maintained_unverified` | `discovery_only` |
| [Superpoint Transformer](superpoint-transformer.md) | 2023 | semantic segmentation | hierarchical superpoints and transformers | `official_or_author_maintained_unverified` | `discovery_only` |
| [urban_road_filter](urban-road-filter.md) | 2022 | road and sidewalk detection | geometric urban road filtering | `official_or_author_maintained_unverified` | `discovery_only` |
| [WYSIWYG 3D Detection](wysiwyg-3d-detection.md) | 2020 | 3D object detection | visibility-aware point-cloud detection | `official_or_author_maintained_unverified` | `discovery_only` |

</div>
