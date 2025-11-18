#!/usr/bin/env python3
"""
Canva to Webflow Converter
Main script to convert Canva websites (exported as PowerPoint) to Webflow sites
"""

import argparse
import os
import sys
from datetime import datetime
from pptx_extractor import PowerPointExtractor
from webflow_generator import WebflowGenerator


class CanvaToWebflowConverter:
    """Main converter class"""

    def __init__(self, input_file: str, output_dir: str = "./output",
                 section_prefix: str = "section", extract_images: bool = True,
                 responsive: bool = True, webflow_export: bool = True,
                 preserve_fonts: bool = True):
        self.input_file = input_file
        self.output_dir = output_dir
        self.section_prefix = section_prefix
        self.extract_images = extract_images
        self.responsive = responsive
        self.webflow_export = webflow_export
        self.preserve_fonts = preserve_fonts

        # Validate input file
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        if not input_file.endswith('.pptx'):
            raise ValueError("Input file must be a PowerPoint file (.pptx)")

    def convert(self):
        """Run the conversion process"""
        print("\n" + "="*60)
        print(" CANVA TO WEBFLOW CONVERTER")
        print("="*60)
        print(f"Input:  {self.input_file}")
        print(f"Output: {self.output_dir}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)

        try:
            # Step 1: Extract PowerPoint content
            print("\n[Step 1/3] Extracting PowerPoint content...")
            extractor = PowerPointExtractor(self.input_file, self.output_dir)
            slides_data = extractor.extract_all_slides()

            if not slides_data:
                print("✗ No slides found in PowerPoint file")
                return False

            print(f"✓ Extracted {len(slides_data)} slides")

            # Step 2: Generate Webflow code
            print("\n[Step 2/3] Generating Webflow HTML/CSS...")
            generator = WebflowGenerator(
                slides_data,
                self.output_dir,
                self.section_prefix,
                self.responsive
            )
            generator.generate_all()

            print("✓ Generated Webflow code")

            # Step 3: Create summary
            print("\n[Step 3/3] Creating conversion summary...")
            self._create_summary(slides_data)

            print("\n" + "="*60)
            print(" CONVERSION COMPLETE!")
            print("="*60)
            print(f"\nOutput files:")
            print(f"  📄 HTML:     {os.path.join(self.output_dir, 'index.html')}")
            print(f"  🎨 CSS:      {os.path.join(self.output_dir, 'styles.css')}")
            print(f"  🖼️  Images:   {os.path.join(self.output_dir, 'images/')}")
            print(f"  📦 Package:  {os.path.join(self.output_dir, 'webflow-import.zip')}")
            print(f"\n✓ {len(slides_data)} sections created")
            print("\nNext steps:")
            print("  1. Review the generated HTML/CSS in the output directory")
            print("  2. Import images to your Webflow project assets")
            print("  3. Copy HTML sections to Webflow custom code sections")
            print("  4. Add Webflow interactions and animations as needed")
            print("  5. Test responsive design at different breakpoints")

            return True

        except Exception as e:
            print(f"\n✗ Error during conversion: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _create_summary(self, slides_data):
        """Create a summary file of the conversion"""
        summary_path = os.path.join(self.output_dir, "conversion_summary.txt")

        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("CANVA TO WEBFLOW CONVERSION SUMMARY\n")
            f.write("="*60 + "\n\n")
            f.write(f"Input File: {self.input_file}\n")
            f.write(f"Output Directory: {self.output_dir}\n")
            f.write(f"Conversion Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Sections: {len(slides_data)}\n\n")

            f.write("="*60 + "\n")
            f.write("SECTIONS OVERVIEW\n")
            f.write("="*60 + "\n\n")

            for slide in slides_data:
                f.write(f"Section {slide.slide_number}: {slide.title}\n")
                f.write(f"  Size: {slide.width:.2f}\" × {slide.height:.2f}\"\n")
                f.write(f"  Elements: {len(slide.elements)}\n")

                # Count element types
                text_count = sum(1 for el in slide.elements if el.type == 'text')
                image_count = sum(1 for el in slide.elements if el.type == 'image')
                shape_count = sum(1 for el in slide.elements if el.type == 'shape')

                f.write(f"    - Text elements: {text_count}\n")
                f.write(f"    - Images: {image_count}\n")
                f.write(f"    - Shapes: {shape_count}\n")

                if slide.background_color:
                    f.write(f"  Background: {slide.background_color}\n")

                f.write("\n")

            f.write("="*60 + "\n")
            f.write("SETTINGS\n")
            f.write("="*60 + "\n")
            f.write(f"Section Prefix: {self.section_prefix}\n")
            f.write(f"Responsive: {self.responsive}\n")
            f.write(f"Extract Images: {self.extract_images}\n")
            f.write(f"Webflow Export: {self.webflow_export}\n")
            f.write(f"Preserve Fonts: {self.preserve_fonts}\n\n")

            f.write("="*60 + "\n")
            f.write("NOTES\n")
            f.write("="*60 + "\n")
            f.write("- Review generated HTML for accuracy\n")
            f.write("- Test responsive breakpoints\n")
            f.write("- Add Webflow interactions manually\n")
            f.write("- Import custom fonts if needed\n")
            f.write("- Optimize images for web performance\n")

        print(f"✓ Summary: {summary_path}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Convert Canva websites (exported as PowerPoint) to Webflow sites",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic conversion
  python canva_to_webflow.py my-canva-site.pptx

  # Specify output directory
  python canva_to_webflow.py my-canva-site.pptx -o ./my-webflow-site

  # Custom section prefix
  python canva_to_webflow.py my-canva-site.pptx --section-prefix "hero"

  # Non-responsive output
  python canva_to_webflow.py my-canva-site.pptx --no-responsive

For more information, visit: https://github.com/yourusername/canva-to-webflow
        """
    )

    parser.add_argument(
        'input_file',
        help='Path to PowerPoint file exported from Canva'
    )

    parser.add_argument(
        '-o', '--output',
        default='./output',
        help='Output directory (default: ./output)'
    )

    parser.add_argument(
        '--section-prefix',
        default='section',
        help='Prefix for section class names (default: section)'
    )

    parser.add_argument(
        '--no-extract-images',
        action='store_true',
        help='Do not extract images from PowerPoint'
    )

    parser.add_argument(
        '--no-responsive',
        action='store_true',
        help='Generate fixed-width layout instead of responsive'
    )

    parser.add_argument(
        '--no-webflow-export',
        action='store_true',
        help='Do not create Webflow export package'
    )

    parser.add_argument(
        '--no-preserve-fonts',
        action='store_true',
        help='Do not preserve original fonts'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='Canva to Webflow Converter v1.0.0'
    )

    args = parser.parse_args()

    # Create converter instance
    try:
        converter = CanvaToWebflowConverter(
            input_file=args.input_file,
            output_dir=args.output,
            section_prefix=args.section_prefix,
            extract_images=not args.no_extract_images,
            responsive=not args.no_responsive,
            webflow_export=not args.no_webflow_export,
            preserve_fonts=not args.no_preserve_fonts
        )

        # Run conversion
        success = converter.convert()

        sys.exit(0 if success else 1)

    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
