#!/usr/bin/env python3
"""
Example usage of the Canva to Webflow Converter
Demonstrates how to use the converter programmatically
"""

from canva_to_webflow import CanvaToWebflowConverter
from pptx_extractor import PowerPointExtractor
from webflow_generator import WebflowGenerator


def example_basic_conversion():
    """Example 1: Basic conversion"""
    print("Example 1: Basic Conversion")
    print("-" * 50)

    converter = CanvaToWebflowConverter(
        input_file="my-canva-design.pptx",
        output_dir="./output"
    )

    success = converter.convert()

    if success:
        print("✓ Conversion successful!")
    else:
        print("✗ Conversion failed")


def example_custom_settings():
    """Example 2: Conversion with custom settings"""
    print("\nExample 2: Custom Settings")
    print("-" * 50)

    converter = CanvaToWebflowConverter(
        input_file="my-canva-design.pptx",
        output_dir="./custom-output",
        section_prefix="hero",
        responsive=True,
        webflow_export=True
    )

    converter.convert()


def example_programmatic_extraction():
    """Example 3: Programmatic extraction and generation"""
    print("\nExample 3: Programmatic Extraction")
    print("-" * 50)

    # Step 1: Extract PowerPoint data
    extractor = PowerPointExtractor(
        pptx_path="my-canva-design.pptx",
        output_dir="./manual-output"
    )

    slides_data = extractor.extract_all_slides()

    # Step 2: Process slides data
    for slide in slides_data:
        print(f"\nSlide {slide.slide_number}: {slide.title}")
        print(f"  Elements: {len(slide.elements)}")

        for element in slide.elements:
            if element.type == 'text':
                print(f"    Text: {element.content[:50]}...")
            elif element.type == 'image':
                print(f"    Image: {element.content}")

    # Step 3: Generate Webflow code
    generator = WebflowGenerator(
        slides_data=slides_data,
        output_dir="./manual-output",
        responsive=True
    )

    generator.generate_all()

    print("\n✓ Manual extraction and generation complete!")


def example_batch_conversion():
    """Example 4: Batch conversion of multiple files"""
    print("\nExample 4: Batch Conversion")
    print("-" * 50)

    pptx_files = [
        ("homepage.pptx", "./site/home"),
        ("about.pptx", "./site/about"),
        ("contact.pptx", "./site/contact"),
    ]

    for pptx_file, output_dir in pptx_files:
        print(f"\nConverting {pptx_file}...")

        converter = CanvaToWebflowConverter(
            input_file=pptx_file,
            output_dir=output_dir
        )

        converter.convert()

    print("\n✓ Batch conversion complete!")


def example_custom_processing():
    """Example 5: Custom processing of extracted data"""
    print("\nExample 5: Custom Processing")
    print("-" * 50)

    # Extract data
    extractor = PowerPointExtractor("my-canva-design.pptx")
    slides_data = extractor.extract_all_slides()

    # Custom processing: Find all images
    all_images = []
    for slide in slides_data:
        for element in slide.elements:
            if element.type == 'image':
                all_images.append(element.content)

    print(f"Found {len(all_images)} images across {len(slides_data)} slides")

    # Custom processing: Extract all text
    all_text = []
    for slide in slides_data:
        for element in slide.elements:
            if element.type == 'text':
                all_text.append(element.content)

    print(f"Found {len(all_text)} text elements")

    # Save text to file
    with open("extracted_text.txt", 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(all_text))

    print("✓ Custom processing complete!")


def main():
    """Run all examples"""
    print("="*60)
    print("CANVA TO WEBFLOW CONVERTER - EXAMPLE USAGE")
    print("="*60)

    # Note: Uncomment the example you want to run
    # Make sure to replace "my-canva-design.pptx" with your actual file

    # example_basic_conversion()
    # example_custom_settings()
    # example_programmatic_extraction()
    # example_batch_conversion()
    # example_custom_processing()

    print("\n" + "="*60)
    print("To run an example, uncomment it in the main() function")
    print("and replace 'my-canva-design.pptx' with your actual file")
    print("="*60)


if __name__ == "__main__":
    main()
