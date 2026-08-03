# Source-list comparison and expansion strategy

The v0.2.0 expansion was informed by two public GitHub collections supplied by the atlas maintainer:

- [Awesome 3D LiDAR Datasets](https://github.com/minwoo0611/Awesome-3D-LiDAR-Datasets)
- [Awesome LIDAR](https://github.com/szenergy/awesome-lidar)

## What those collections do well

The focused 3D-dataset collection provides a compact year/sensor/task/scale table and adds detailed dataset descriptions. The broader Awesome LIDAR collection spans manufacturers, datasets, libraries, frameworks, algorithms, simulators, tools, and related lists. It also uses recognizable badges, a contribution guide, an optional website, and popularity indicators.


## Coverage audit for this candidate

The candidate maps every named dataset in the reviewed **Awesome 3D LiDAR Datasets** summary table available during the 2026-08-03 review. It also maps the named resources reviewed from **Awesome LIDAR** across manufacturers, datasets, libraries, frameworks, algorithms, simulators, tools, and neighboring lists. Secondary YouTube/Vimeo links and popularity badges are not independently cataloged because they are discovery aids rather than primary research or access records.

Coverage parity is not the same as verification parity. Newly mapped entries remain `discovery_only` or `source_listed` until the atlas independently confirms primary publications, contributors, licensing, access rules, maintenance state, and implementation relationships.

## Design comparison

| Capability | Awesome 3D LiDAR Datasets | Awesome LIDAR | LiDAR Research Atlas v0.2.0 |
|---|---|---|---|
| Primary strength | Focused 3D-dataset summary | Broad LiDAR ecosystem directory | Structured discovery, provenance, lawful access, and search |
| Presentation | README table plus descriptions | Categorized README with badges | Generated documentation site and searchable tables |
| Dataset dimensions | Primarily 3D | Broad LiDAR scope | Explicit 2D, 3D, indoor, outdoor, aerial, terrestrial, mobile, and synthetic fields |
| Methods and ecosystem | Dataset-focused | Manufacturers, libraries, frameworks, algorithms, simulators, tools, and lists | Separate dataset, method, and ecosystem schemas and pages |
| Machine-readable export | Not the central interface | Not the central interface | YAML sources plus CSV and JSON exports |
| Access and license modeling | Links and descriptive notes | Links and descriptive notes | Access class, registration/agreement status, commercial-use status, redistribution status, and provider-terms source |
| Verification state | Curator-maintained list | Curator-maintained list | `verified`, `partial`, `discovery_only`, and `source_listed` labels |
| Legal boundary | Upstream-specific | CC0 list presentation | No data mirroring, separate software/content licenses, third-party notices, correction/takedown process |
| Automation | README maintenance | README maintenance and badges | Schema validation, page generation, export generation, restricted-file scanning, tests, and source-link audit |

## What the atlas adds

The LiDAR Research Atlas does not replace or claim ownership of those collections. It adds a different layer:

- structured YAML, CSV, and JSON records;
- searchable documentation tables;
- indoor, outdoor, 2D, 3D, aerial, mobile, terrestrial, and synthetic scope;
- explicit distinction between verified and discovery-only records;
- provider-controlled lawful-access workflow;
- separate dataset, annotation, code, model-weight, and commercial-use considerations;
- original explanatory pages and diagrams;
- machine validation, restricted-file checks, and generated source registers;
- rights-holder correction and takedown procedures.

## Copyright and database boundary

No abstracts, long descriptions, figures, screenshots, logos, or tables were copied from the upstream collections. Resource names, dates, sensor/task facts, and outbound project links were used as discovery signals and reorganized into independently written atlas records. The broader Awesome LIDAR repository identifies a CC0-1.0 license. No repository license was detected for Awesome 3D LiDAR Datasets during this review, so its prose and presentation were not reproduced.

## Verification layers

A `verified` or `partial` atlas record has undergone direct source review to the level stated in the record. A `discovery_only` record has been indexed from a scholarly source list and official project URL but still requires independent review of contributors, publication, access, license, and current availability.

The provider's current terms always control.
