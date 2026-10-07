<div align="center">

# SMART VAC Media Compressor

**A compact PyQt6 batch converter for aggressively shrinking images and videos with simple drag-and-drop controls.**

[![Version](https://img.shields.io/badge/version-0.0.1-D4B86A?style=flat-square)](#)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/UI-PyQt6-41CD52?style=flat-square)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

</div>

## What it does

SMART VAC Media Compressor is the lightweight member of the VAC media-tool family. It focuses on fast local batch work rather than a large workflow surface.

- drop files or folders into the app;
- use Smart Auto or pick a target format;
- process image and video queues without blocking the GUI;
- keep external media tools beside the app when you want a portable setup.

## Quick start

```powershell
git clone https://github.com/vacterro/SMART-VAC-MEDIA-COMPRESSOR.git
cd SMART-VAC-MEDIA-COMPRESSOR
pip install -r requirements.txt
python SMART_VAC_COMPRESSOR.pyw
```

Python dependencies are **PyQt6** and **Pillow**.

## Features

| Area | Capability |
|---|---|
| **Batch input** | files and folders with drag-and-drop workflow |
| **Smart Auto** | chooses a conversion path from source media type |
| **Images** | WebP, AVIF, JPG, PNG, TIFF, ICO workflows |
| **Video** | AV1, HEVC, and H.264 paths when suitable tools/hardware are available |
| **UI** | dark desktop interface with persistent configuration |
| **Portable tools** | local `bin/` folder for external executables |
| **Build** | included Windows `build.bat` helper |

## Configuration

- `theme_config.json` stores editable theme values;
- the Settings UI exposes compression parameters;
- backend/hardware availability is detected by the processing layer;
- `core/` contains conversion logic while `gui/` owns the desktop surface.

## Languages

[English](README.md) · [Русский](README.ru.md) · [Eesti](README.et.md)

## License

[MIT](LICENSE)


## Project network

Part of the broader **SAIPEN / vacterro** project ecosystem.

[**Author hub**](https://github.com/vacterro) · [**SAIPEN HQ**](https://github.com/saipenhq) · [**SAIPEN Core**](https://github.com/vacterro/saipen) · [**ZAICODE**](https://github.com/vacterro/zaicode) · [**FastPrompter**](https://github.com/vacterro/FastPrompter) · [**SAIPEN Community**](https://discord.gg/SEYaYkuVgN)

For reproducible bugs and durable feature requests, use [GitHub Issues](https://github.com/vacterro/SMART-VAC-MEDIA-COMPRESSOR/issues).

<!-- VACTERRO_SUPPORT:BEGIN -->
---
<sub>If SMART VAC Media Compressor is useful to you, optional support: [Buy Me a Coffee](https://buymeacoffee.com/vacuum34) · [Boosty](https://boosty.to/vacuum34/donate) · [PayPal](https://paypal.me/AlexNelin) · [other ways](https://github.com/vacterro/vacterro/blob/main/SUPPORT.md)</sub>
<!-- VACTERRO_SUPPORT:END -->
