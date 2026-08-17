import json
import os
from pathlib import Path

DEFAULT_THEMES = {
    "Vintage 95": {
        "background": "#C0C0C0",
        "surface": "#C0C0C0",
        "surfaceRaised": "#FFFFFF",
        "surfaceAlt": "#E6E6E6",
        "borderSubtle": "#808080",
        "borderStrong": "#404040",
        "borderHighlight": "#FFFFFF",
        "borderDark": "#404040", 
        "borderMuted": "#808080",
        "textPrimary": "#000000",
        "textSecondary": "#202020",
        "textMuted": "#666666",
        "accentTurquoise": "#008080",
        "accentTurquoiseDim": "#006666",
        "accentTealDeep": "#004C4C",
        "success": "#008000",
        "warning": "#800000",
        "danger": "#800000",
        "bg_header": "#008080",
        "accentCursor": "#008080",
        "selection": "#008080", 
    },
    "Vintage Golden": {
        "background": "#1A0F05",
        "surface": "#2A1C0A",
        "surfaceRaised": "#362812",
        "surfaceAlt": "#3A2A15",
        "borderSubtle": "#4A3820", 
        "borderStrong": "#0E0803", 
        "borderHighlight": "#C0A060",
        "borderDark": "#0E0803",
        "textPrimary": "#D4B87A",
        "textSecondary": "#B09558",
        "textMuted": "#7A6838",
        "accentTurquoise": "#008080",
        "accentTurquoiseDim": "#006666",
        "accentTealDeep": "#004C4C",
        "success": "#4A7A20",
        "warning": "#7A7A20",
        "danger": "#7A2020",
        "bg_header": "#004C4C",
        "accentCursor": "#D4B87A",
        "selection": "#362812",
    }
}


class ThemeManager:
    def __init__(self, config_path="theme_config.json"):
        self.config_path = config_path
        self.themes = DEFAULT_THEMES.copy()
        
        self.config = {
            "active_theme": "Vintage Golden", # Set to new default
            "is_custom": False,
            "font_size": 14,
            "custom_palette": self.themes["Vintage Golden"].copy() # Updated default
        }
        self.load_config()

    def load_config(self):
        if Path(self.config_path).exists():
            try:
                with open(self.config_path, 'r') as f:
                    data = json.load(f)
                    self.config.update(data)
            except Exception:
                pass

        self.themes["Custom"] = self.config["custom_palette"]

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)

    def get_palette(self) -> dict:
        if self.config.get("is_custom", False):
            return self.config.get("custom_palette", self.themes["Vintage 95"])
        name = self.config.get("active_theme", "Vintage 95")
        return self.themes.get(name, self.themes["Vintage 95"])

    def set_active_theme(self, name: str):
        if name in self.themes:
            self.config["active_theme"] = name
            self.save_config()

    def get_active_theme_name(self) -> str:
        return self.config.get("active_theme", "Vintage 95")

    def update_custom_color(self, key: str, hex_color: str):
        self.config["custom_palette"][key] = hex_color
        self.themes["Custom"] = self.config["custom_palette"]
        self.save_config()

    def get_font_family(self) -> str:
        return self.config.get("font_family", "MS Sans Serif")

    def set_font_family(self, font: str):
        self.config["font_family"] = font
        self.save_config()

    def get_font_size(self) -> int:
        return self.config.get("font_size", 14)

    def set_font_size(self, size: int):
        self.config["font_size"] = size
        self.save_config()
