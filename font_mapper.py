"""
Font Mapper Module
Maps Canva/PowerPoint fonts to web-safe alternatives and Google Fonts
"""

import json
import re
from typing import Dict, List, Optional


class FontMapper:
    """Maps fonts to web-safe alternatives and generates font imports"""

    # Comprehensive font mapping from Canva fonts to Google Fonts
    FONT_MAPPINGS = {
        # Canva's most common fonts
        'Montserrat': {'google': 'Montserrat', 'weights': [300, 400, 500, 600, 700, 800]},
        'Montserrat medium': {'google': 'Montserrat', 'weights': [500]},
        'Montserrat Medium': {'google': 'Montserrat', 'weights': [500]},
        'Poppins': {'google': 'Poppins', 'weights': [300, 400, 500, 600, 700]},
        'Roboto': {'google': 'Roboto', 'weights': [300, 400, 500, 700]},
        'Open Sans': {'google': 'Open Sans', 'weights': [400, 600, 700]},
        'Lato': {'google': 'Lato', 'weights': [400, 700]},
        'Playfair Display': {'google': 'Playfair Display', 'weights': [400, 700]},
        'Raleway': {'google': 'Raleway', 'weights': [300, 400, 600, 700]},
        'Bebas Neue': {'google': 'Bebas Neue', 'weights': [400]},
        'Anton': {'google': 'Anton', 'weights': [400]},
        'Oswald': {'google': 'Oswald', 'weights': [400, 500, 700]},
        'Merriweather': {'google': 'Merriweather', 'weights': [400, 700]},
        'Source Sans Pro': {'google': 'Source Sans Pro', 'weights': [400, 600, 700]},
        'PT Sans': {'google': 'PT Sans', 'weights': [400, 700]},
        'Ubuntu': {'google': 'Ubuntu', 'weights': [400, 500, 700]},
        'Nunito': {'google': 'Nunito', 'weights': [400, 600, 700]},
        'Work Sans': {'google': 'Work Sans', 'weights': [400, 500, 600, 700]},
        'Quicksand': {'google': 'Quicksand', 'weights': [400, 500, 600, 700]},
        'Crimson Text': {'google': 'Crimson Text', 'weights': [400, 600, 700]},

        # Common Microsoft fonts to web equivalents
        'Arial': {'fallback': 'Arial, Helvetica, sans-serif'},
        'Helvetica': {'fallback': 'Helvetica, Arial, sans-serif'},
        'Times New Roman': {'fallback': 'Times New Roman, Times, serif'},
        'Georgia': {'fallback': 'Georgia, serif'},
        'Verdana': {'fallback': 'Verdana, sans-serif'},
        'Courier New': {'fallback': 'Courier New, monospace'},
        'Calibri': {'google': 'Roboto', 'weights': [400, 700]},  # Close alternative
        'Cambria': {'google': 'Merriweather', 'weights': [400, 700]},

        # Canva-specific font variations
        'Abril Fatface': {'google': 'Abril Fatface', 'weights': [400]},
        'Amatic SC': {'google': 'Amatic SC', 'weights': [400, 700]},
        'Archivo': {'google': 'Archivo', 'weights': [400, 700]},
        'Arvo': {'google': 'Arvo', 'weights': [400, 700]},
        'Asap': {'google': 'Asap', 'weights': [400, 700]},
        'Barlow': {'google': 'Barlow', 'weights': [400, 500, 600, 700]},
        'Bitter': {'google': 'Bitter', 'weights': [400, 700]},
        'Cabin': {'google': 'Cabin', 'weights': [400, 600, 700]},
        'Comfortaa': {'google': 'Comfortaa', 'weights': [400, 700]},
        'Dancing Script': {'google': 'Dancing Script', 'weights': [400, 700]},
        'DM Sans': {'google': 'DM Sans', 'weights': [400, 500, 700]},
        'Exo': {'google': 'Exo', 'weights': [400, 700]},
        'Fjalla One': {'google': 'Fjalla One', 'weights': [400]},
        'Heebo': {'google': 'Heebo', 'weights': [400, 500, 700]},
        'Inconsolata': {'google': 'Inconsolata', 'weights': [400, 700]},
        'Indie Flower': {'google': 'Indie Flower', 'weights': [400]},
        'Inter': {'google': 'Inter', 'weights': [400, 500, 600, 700]},
        'Josefin Sans': {'google': 'Josefin Sans', 'weights': [400, 700]},
        'Karla': {'google': 'Karla', 'weights': [400, 700]},
        'League Spartan': {'google': 'League Spartan', 'weights': [400, 700]},
        'Lexend': {'google': 'Lexend', 'weights': [400, 500, 700]},
        'Libre Baskerville': {'google': 'Libre Baskerville', 'weights': [400, 700]},
        'Lobster': {'google': 'Lobster', 'weights': [400]},
        'Noto Sans': {'google': 'Noto Sans', 'weights': [400, 700]},
        'Pacifico': {'google': 'Pacifico', 'weights': [400]},
        'Permanent Marker': {'google': 'Permanent Marker', 'weights': [400]},
        'Righteous': {'google': 'Righteous', 'weights': [400]},
        'Rubik': {'google': 'Rubik', 'weights': [400, 500, 700]},
        'Shadows Into Light': {'google': 'Shadows Into Light', 'weights': [400]},
        'Signika': {'google': 'Signika', 'weights': [400, 700]},
        'Spartan': {'google': 'League Spartan', 'weights': [400, 700]},
        'Spectral': {'google': 'Spectral', 'weights': [400, 700]},
        'Titillium Web': {'google': 'Titillium Web', 'weights': [400, 700]},
        'Zilla Slab': {'google': 'Zilla Slab', 'weights': [400, 700]},
    }

    # Default fallback fonts
    DEFAULT_SANS_SERIF = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    DEFAULT_SERIF = 'Georgia, "Times New Roman", Times, serif'
    DEFAULT_MONOSPACE = '"Courier New", Courier, monospace'

    def __init__(self):
        self.used_fonts = set()
        self.google_fonts_needed = {}

    def map_font(self, font_name: str, fallback_type: str = 'sans-serif') -> Dict[str, any]:
        """
        Map a font to its web equivalent
        Returns dict with 'css_family', 'google_font', 'weights'
        """
        if not font_name:
            return {
                'css_family': self.DEFAULT_SANS_SERIF,
                'google_font': None,
                'weights': []
            }

        # Clean font name
        clean_name = self._clean_font_name(font_name)

        # Check if we have a mapping
        if clean_name in self.FONT_MAPPINGS:
            mapping = self.FONT_MAPPINGS[clean_name]

            # Track this font
            self.used_fonts.add(clean_name)

            if 'google' in mapping:
                # Google Font available
                google_font = mapping['google']
                weights = mapping.get('weights', [400])

                # Track for import
                if google_font not in self.google_fonts_needed:
                    self.google_fonts_needed[google_font] = set()
                self.google_fonts_needed[google_font].update(weights)

                # Build CSS family string
                css_family = f'"{google_font}", {self._get_fallback(fallback_type)}'

                return {
                    'css_family': css_family,
                    'google_font': google_font,
                    'weights': weights
                }

            elif 'fallback' in mapping:
                # Use fallback
                return {
                    'css_family': mapping['fallback'],
                    'google_font': None,
                    'weights': []
                }

        # No mapping found - use font name with fallback
        css_family = f'"{clean_name}", {self._get_fallback(fallback_type)}'
        return {
            'css_family': css_family,
            'google_font': None,
            'weights': []
        }

    def generate_google_fonts_url(self) -> Optional[str]:
        """Generate Google Fonts import URL for all used fonts"""
        if not self.google_fonts_needed:
            return None

        # Build URL
        families = []
        for font, weights in sorted(self.google_fonts_needed.items()):
            # Sort weights
            sorted_weights = sorted(weights)
            weights_str = ';'.join([f"{w}" for w in sorted_weights])

            # Format: Family:weight1;weight2;weight3
            family_str = f"{font.replace(' ', '+')}:wght@{weights_str}"
            families.append(family_str)

        # Combine all families
        url = f"https://fonts.googleapis.com/css2?{'&'.join([f'family={f}' for f in families])}&display=swap"

        return url

    def generate_font_face_css(self) -> str:
        """Generate @font-face CSS imports"""
        if not self.google_fonts_needed:
            return ""

        css_parts = ["/* Google Fonts Import */"]
        url = self.generate_google_fonts_url()

        if url:
            css_parts.append(f"@import url('{url}');")
            css_parts.append("")

        return '\n'.join(css_parts)

    def get_font_report(self) -> str:
        """Generate a report of fonts used and their mappings"""
        lines = ["Font Mapping Report", "=" * 60, ""]

        if not self.used_fonts:
            lines.append("No fonts detected.")
            return '\n'.join(lines)

        lines.append(f"Total fonts detected: {len(self.used_fonts)}")
        lines.append("")

        # Google Fonts
        if self.google_fonts_needed:
            lines.append("Google Fonts Required:")
            for font, weights in sorted(self.google_fonts_needed.items()):
                weights_str = ', '.join([str(w) for w in sorted(weights)])
                lines.append(f"  • {font} (weights: {weights_str})")
            lines.append("")

        # All fonts
        lines.append("All Fonts Used:")
        for font in sorted(self.used_fonts):
            mapping = self.FONT_MAPPINGS.get(font, {})
            if 'google' in mapping:
                lines.append(f"  • {font} → Google Font: {mapping['google']}")
            elif 'fallback' in mapping:
                lines.append(f"  • {font} → Fallback: {mapping['fallback']}")
            else:
                lines.append(f"  • {font} → No mapping (using fallback)")

        lines.append("")
        lines.append("Google Fonts URL:")
        lines.append(self.generate_google_fonts_url() or "N/A")

        return '\n'.join(lines)

    def export_font_config(self, filepath: str):
        """Export font configuration as JSON"""
        config = {
            'used_fonts': list(self.used_fonts),
            'google_fonts': {
                font: list(weights)
                for font, weights in self.google_fonts_needed.items()
            },
            'google_fonts_url': self.generate_google_fonts_url()
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)

    @staticmethod
    def _clean_font_name(font_name: str) -> str:
        """Clean and normalize font name"""
        # Remove extra whitespace
        clean = re.sub(r'\s+', ' ', font_name.strip())
        return clean

    @staticmethod
    def _get_fallback(fallback_type: str) -> str:
        """Get fallback font stack"""
        if fallback_type == 'serif':
            return FontMapper.DEFAULT_SERIF
        elif fallback_type == 'monospace':
            return FontMapper.DEFAULT_MONOSPACE
        else:
            return FontMapper.DEFAULT_SANS_SERIF


if __name__ == "__main__":
    # Example usage and testing
    mapper = FontMapper()

    # Test various fonts
    test_fonts = [
        'Montserrat',
        'Montserrat medium',
        'Arial',
        'Unknown Font',
        'Poppins',
        'Roboto'
    ]

    print("Font Mapping Test")
    print("=" * 60)

    for font in test_fonts:
        result = mapper.map_font(font)
        print(f"\n{font}:")
        print(f"  CSS: {result['css_family']}")
        print(f"  Google: {result['google_font']}")
        print(f"  Weights: {result['weights']}")

    print("\n" + "=" * 60)
    print("\nGoogle Fonts URL:")
    print(mapper.generate_google_fonts_url())

    print("\n" + "=" * 60)
    print("\n" + mapper.get_font_report())
