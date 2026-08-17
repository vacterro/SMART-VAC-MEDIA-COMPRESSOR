# Requirements

## Functional
1. **Media Compression:** Compress and convert Images, Videos, and Audio sequences.
2. **Batch Queue:** Handle multiple files sequentially without memory leaks.
3. **Save/Restore State:** Queue must persist between crashes or application closures.
4. **Resiliency:** Handle invalid media, unsupported formats, and missing output directories gracefully.

## Design & UI (`/vintage`)
1. **Aesthetics:** strictly adhere to Vintage 95 design language (`#C0C0C0` background, no rounded corners except 2-4px where absolutely required, MS Sans Serif or Tahoma 14-16px).
2. **Compactness:** Maximize screen real estate. Replace bloated nested `QVBoxLayout`/`QHBoxLayout` with unified `QGridLayout`.
3. **Accessibility:** All primary buttons (e.g., Start, Cancel) must have a touch target of at least 44x44px. Focus states must be distinct.

## Performance (`/doo`)
1. **Thread Safety:** `BatchManager` (QThread) must communicate perfectly with `MainWindow` (Main Thread) without race conditions.
2. **Clean Code:** `main_window.py` must be modular. 1,700 lines of spaghetti UI code must be organized into private setup methods.
