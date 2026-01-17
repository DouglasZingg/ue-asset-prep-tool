
---

## ✅ `CHANGELOG.md`

```md
# Changelog
All notable changes to this project will be documented here.

---

## [1.0.0] - Release
### Added
- Editor Utility Widget UI for asset validation and prep
- Scan modes:
  - Selected Assets scan
  - Folder batch scan
  - Progress indicator
  - Cancel scanning
- Naming validation:
  - Prefix enforcement
  - No spaces rule
- Texture validation:
  - sRGB checks
  - Compression checks
- Static mesh validation:
  - Minimum LOD rule
  - Collision required rule
- Severity-based UI output (INFO / WARNING / ERROR)
- Summary counters (Scanned / OK / Warnings / Errors)
- JSON export report generation
- Rule presets:
  - Game / Film / Mobile
- Save / Load profiles (SaveGame-based)
- Performance polish for batch scans

### Changed
- Refactored scanning to support timer-based processing (responsive UI)

---

## [0.9.0] - Day 9
### Added
- Rule presets + CurrentRules struct
- Save/Load profiles (SaveGame)
- Performance improvements for folder scans

---

## [0.8.0] - Day 8
### Added
- Folder scan mode using List Assets + Load Asset
- Timer-driven scanning (avoids freezing)
- Cancel scan support
- Progress text updates

---

## [0.7.0] - Day 7
### Added
- Severity-colored output rows
- Summary counters
- JSON export (results array)

---

## [0.6.0] - Day 6
### Added
- Collision validation support (UE version-dependent)
- Safer evaluation routing to reduce crashes

---

## [0.5.0] - Day 5
### Added
- Static mesh validation baseline (LOD/collision checks)

---

## [0.4.0] - Day 4
### Added
- Texture validation (sRGB + compression)

---

## [0.3.0] - Day 3
### Added
- Naming validation + expected prefix mapping

---

## [0.2.0] - Day 2
### Added
- Asset selection scanning
- UI row creation for scanned assets

---

## [0.1.0] - Day 1
### Added
- Unreal project setup
- First Editor Utility Widget “Hello World”
