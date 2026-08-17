# PROJECT.md

**Name:** SMART VAC MEDIA COMPRESSOR
**Purpose:** A robust desktop application for batch compressing and converting media files (images and video), powered by ffmpeg and imagemagick.
**Architecture:** Python + PyQt6 GUI with multi-threaded `BatchManager` orchestrating `ImageProcessor` and `VideoProcessor`.

## Core Technologies
- Python 3.12+
- PyQt6
- FFmpeg
- ImageMagick / svt-av1 / x265

## Design System
- Theme: Vintage 95 (Strictly enforced via `/vintage` guidelines).
- Focus: Usability, compactness, and high accessibility.
