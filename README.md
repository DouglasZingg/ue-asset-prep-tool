# UE Asset Prep & Validation Tool (Editor Utility Widget)

Production-style Unreal Engine **Editor Utility Widget** for validating and preparing assets for game / film / mobile pipelines.

This tool complements my pipeline portfolio by showing **engine-side tooling**, **batch processing**, and **artist-facing UI**, alongside my DCC and tracking tools:

## ✨ Features

### Scan Modes
- ✅ **Selected Assets** scan
- ✅ **Folder scan** (batch mode)
- ✅ Progress display while scanning
- ✅ **Cancel** mid-scan safely

### Validation Categories
- ✅ **Naming**
  - Prefix rules (SM_, T_, M_, etc.)
  - No spaces
- ✅ **Textures**
  - sRGB rules (Normal / ORM behavior)
  - Compression preset checks
- ✅ **Static Mesh**
  - LOD count rules
  - Collision required (rule-driven)

### Reporting
- ✅ Severity UI (INFO / WARNING / ERROR)
- ✅ Summary counters (Scanned / OK / Warnings / Errors)
- ✅ **Export JSON report**

### Pipeline Polish
- ✅ Rule presets: **Game / Film / Mobile**
- ✅ Save/Load validation profiles (SaveGame-based)
- ✅ Performance improvements for folder scans

---

## 🧰 Tech Stack

- Unreal Engine **5.3+**
- **Editor Utility Widget** (Blueprint)
- Editor Scripting Utilities
- Unreal Python (optional, only if your export uses it)

---

## 📁 Repo Structure

