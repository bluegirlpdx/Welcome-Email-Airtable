"""
Webflow Generator Module
Generates Webflow-compatible HTML and CSS from extracted PowerPoint data
"""

import os
import json
import zipfile
from typing import List, Dict, Any
from pptx_extractor import SlideData
from font_mapper import FontMapper


class WebflowGenerator:
    """Generates Webflow-compatible code from slide data"""

    def __init__(self, slides_data: List[SlideData], output_dir: str = "./output",
                 section_prefix: str = "section", responsive: bool = True):
        self.slides_data = slides_data
        self.output_dir = output_dir
        self.section_prefix = section_prefix
        self.responsive = responsive
        self.sections_dir = os.path.join(output_dir, "sections")

        # Create directories
        os.makedirs(self.sections_dir, exist_ok=True)

        # CSS accumulator
        self.css_rules = []
        self.global_styles = []

        # Font mapper
        self.font_mapper = FontMapper()

    def generate_all(self):
        """Generate all HTML and CSS files"""
        print("\n" + "="*50)
        print("Generating Webflow Code")
        print("="*50)

        # Generate individual sections
        section_html_parts = []
        for slide in self.slides_data:
            html, css = self.generate_section(slide)
            section_html_parts.append(html)

            # Save individual section file
            section_file = os.path.join(
                self.sections_dir,
                f"{self.section_prefix}-{slide.slide_number}.html"
            )
            with open(section_file, 'w', encoding='utf-8') as f:
                f.write(html)

        # Generate main HTML file
        main_html = self.generate_main_html(section_html_parts)
        main_file = os.path.join(self.output_dir, "index.html")
        with open(main_file, 'w', encoding='utf-8') as f:
            f.write(main_html)

        # Generate CSS file
        css_content = self.generate_css()
        css_file = os.path.join(self.output_dir, "styles.css")
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content)

        # Generate font report
        font_report = self.font_mapper.get_font_report()
        font_report_file = os.path.join(self.output_dir, "font_report.txt")
        with open(font_report_file, 'w', encoding='utf-8') as f:
            f.write(font_report)

        # Export font configuration
        self.font_mapper.export_font_config(
            os.path.join(self.output_dir, "fonts_used.json")
        )

        # Generate Webflow export package
        self.generate_webflow_package()

        print(f"\n✓ Generated {len(self.slides_data)} sections")
        print(f"✓ Main HTML: {main_file}")
        print(f"✓ Styles: {css_file}")
        print(f"✓ Font report: {font_report_file}")

    def generate_section(self, slide: SlideData) -> tuple:
        """Generate HTML and CSS for a single section"""
        section_id = f"{self.section_prefix}-{slide.slide_number}"
        section_class = f"{self.section_prefix}"

        # Sort elements by z-index
        sorted_elements = sorted(slide.elements, key=lambda x: x.z_index)

        # Generate HTML
        html_parts = [f'<section id="{section_id}" class="{section_class}">']

        # Add container
        html_parts.append(f'  <div class="{section_id}-container container">')

        # Process elements
        for idx, element in enumerate(sorted_elements):
            element_html = self._generate_element_html(element, section_id, idx)
            if element_html:
                html_parts.append(f"    {element_html}")

        html_parts.append('  </div>')
        html_parts.append('</section>')

        # Generate CSS for this section
        self._generate_section_css(slide, section_id, sorted_elements)

        return '\n'.join(html_parts), None

    def _generate_element_html(self, element: Any, section_id: str, idx: int) -> str:
        """Generate HTML for a single element"""
        class_name = f"{section_id}-el-{idx}"

        if element.type == 'text':
            # Determine heading level based on font size
            tag = self._determine_text_tag(element)
            content = self._format_text_content(element.content)
            return f'<{tag} class="{class_name}">{content}</{tag}>'

        elif element.type == 'image':
            alt_text = element.styling.get('alt', 'Image')
            img_path = f"images/{element.content}"
            return f'<img src="{img_path}" alt="{alt_text}" class="{class_name}" />'

        elif element.type == 'shape':
            return f'<div class="{class_name} shape-element"></div>'

        return ''

    def _generate_section_css(self, slide: SlideData, section_id: str,
                              elements: List[Any]):
        """Generate CSS rules for a section"""
        # Section styles
        section_styles = {
            'position': 'relative',
            'width': '100%',
            'min-height': '100vh',
            'padding': '60px 20px',
        }

        if slide.background_color:
            section_styles['background-color'] = slide.background_color

        self.css_rules.append(self._css_rule(f'#{section_id}', section_styles))

        # Container styles
        container_styles = {
            'position': 'relative',
            'max-width': '1200px',
            'margin': '0 auto',
            'height': '100%',
        }
        self.css_rules.append(
            self._css_rule(f'#{section_id}-container', container_styles)
        )

        # Element styles
        for idx, element in enumerate(elements):
            class_name = f"{section_id}-el-{idx}"
            element_styles = self._generate_element_styles(element, slide)
            self.css_rules.append(self._css_rule(f'.{class_name}', element_styles))

    def _generate_element_styles(self, element: Any, slide: SlideData) -> Dict[str, str]:
        """Generate CSS styles for an element"""
        styles = {}

        # Position (convert from inches to percentage for responsiveness)
        if self.responsive:
            # Use percentage-based positioning
            left_pct = (element.position['left'] / slide.width * 100)
            top_pct = (element.position['top'] / slide.height * 100)
            width_pct = (element.position['width'] / slide.width * 100)

            styles['position'] = 'absolute'
            styles['left'] = f'{left_pct:.2f}%'
            styles['top'] = f'{top_pct:.2f}%'
            styles['width'] = f'{width_pct:.2f}%'
        else:
            # Use fixed positioning
            styles['position'] = 'absolute'
            styles['left'] = f'{element.position["left"]}in'
            styles['top'] = f'{element.position["top"]}in'
            styles['width'] = f'{element.position["width"]}in'

        # Type-specific styles
        if element.type == 'text':
            if element.styling.get('font_family'):
                # Map font using font mapper
                font_mapping = self.font_mapper.map_font(element.styling["font_family"])
                styles['font-family'] = font_mapping['css_family']
            if element.styling.get('font_size'):
                styles['font-size'] = f'{element.styling["font_size"]}px'
            if element.styling.get('color'):
                styles['color'] = element.styling['color']
            if element.styling.get('bold'):
                styles['font-weight'] = '700'
            if element.styling.get('italic'):
                styles['font-style'] = 'italic'
            if element.styling.get('alignment'):
                styles['text-align'] = element.styling['alignment']

        elif element.type == 'image':
            styles['object-fit'] = element.styling.get('object_fit', 'cover')
            styles['height'] = 'auto'

        elif element.type == 'shape':
            if element.styling.get('fill_color'):
                styles['background-color'] = element.styling['fill_color']
            if element.styling.get('border_color'):
                styles['border'] = f'{element.styling.get("border_width", 1)}px solid {element.styling["border_color"]}'
            styles['height'] = f'{element.position["height"]}in' if not self.responsive else 'auto'

        # Z-index
        styles['z-index'] = str(element.z_index)

        return styles

    def _css_rule(self, selector: str, styles: Dict[str, str]) -> str:
        """Generate a CSS rule"""
        if not styles:
            return ''

        rules = [f'  {key}: {value};' for key, value in styles.items()]
        return f'{selector} {{\n' + '\n'.join(rules) + '\n}'

    def generate_css(self) -> str:
        """Generate complete CSS file"""
        css_parts = []

        # Add Google Fonts import (if any fonts are needed)
        font_import = self.font_mapper.generate_font_face_css()
        if font_import:
            css_parts.append(font_import)

        # Add reset and base styles
        css_parts.append("""/* CSS Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.6;
  color: #333;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Sections */
""")

        # Add generated rules
        css_parts.extend(self.css_rules)

        # Add responsive breakpoints
        if self.responsive:
            css_parts.append("""
/* Responsive Breakpoints */
@media screen and (max-width: 991px) {
  section {
    padding: 40px 15px;
  }
}

@media screen and (max-width: 767px) {
  section {
    padding: 30px 10px;
  }

  /* Stack elements on mobile */
  section [class*="-el-"] {
    position: relative !important;
    width: 100% !important;
    left: 0 !important;
    margin-bottom: 20px;
  }
}
""")

        return '\n'.join(css_parts)

    def generate_main_html(self, section_html_parts: List[str]) -> str:
        """Generate the main HTML file"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Canva to Webflow Conversion</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Generated from Canva via PowerPoint -->
  <!-- Total sections: {len(section_html_parts)} -->

{chr(10).join(section_html_parts)}

  <!-- Webflow-style scripts (add as needed) -->
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</body>
</html>
"""
        return html

    def generate_webflow_package(self):
        """Create a Webflow-ready export package"""
        zip_path = os.path.join(self.output_dir, "webflow-import.zip")

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add HTML
            zipf.write(
                os.path.join(self.output_dir, "index.html"),
                "index.html"
            )

            # Add CSS
            zipf.write(
                os.path.join(self.output_dir, "styles.css"),
                "css/styles.css"
            )

            # Add images
            images_dir = os.path.join(self.output_dir, "images")
            if os.path.exists(images_dir):
                for img_file in os.listdir(images_dir):
                    img_path = os.path.join(images_dir, img_file)
                    if os.path.isfile(img_path):
                        zipf.write(img_path, f"images/{img_file}")

            # Add metadata
            metadata = {
                'generator': 'Canva to Webflow Converter',
                'sections': len(self.slides_data),
                'responsive': self.responsive
            }
            zipf.writestr('metadata.json', json.dumps(metadata, indent=2))

        print(f"✓ Webflow package: {zip_path}")

    @staticmethod
    def _determine_text_tag(element) -> str:
        """Determine appropriate HTML tag based on font size"""
        font_size = element.styling.get('font_size', 16)

        if font_size >= 32:
            return 'h1'
        elif font_size >= 24:
            return 'h2'
        elif font_size >= 20:
            return 'h3'
        elif font_size >= 18:
            return 'h4'
        else:
            return 'p'

    @staticmethod
    def _format_text_content(content: str) -> str:
        """Format text content for HTML"""
        # Convert newlines to <br> tags
        content = content.replace('\n', '<br>')
        # Escape HTML characters
        content = content.replace('<', '&lt;').replace('>', '&gt;')
        # Restore <br> tags
        content = content.replace('&lt;br&gt;', '<br>')
        return content


if __name__ == "__main__":
    print("This module should be imported and used by canva_to_webflow.py")
