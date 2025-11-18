# Changelog

All notable changes to the Canva to Webflow Converter project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-11-18

### Added
- Initial release of Canva to Webflow Converter
- PowerPoint extraction module (`pptx_extractor.py`)
  - Extract slides, text, images, and shapes from PowerPoint files
  - Support for positioning, styling, and layout information
  - Automatic image extraction and organization
- Webflow code generator (`webflow_generator.py`)
  - Generate semantic HTML5 structure
  - Create responsive CSS with breakpoints
  - Webflow-compatible class naming conventions
  - Section-based architecture
- Main converter script (`canva_to_webflow.py`)
  - Command-line interface with argument parsing
  - Configurable output options
  - Progress tracking and status reporting
  - Conversion summary generation
- Documentation
  - Comprehensive README.md with usage instructions
  - Quick Start Guide (QUICKSTART.md)
  - Example usage script (example_usage.py)
  - Configuration example file (config.example.json)
- Project infrastructure
  - requirements.txt with Python dependencies
  - .gitignore for Python projects
  - MIT License
  - CHANGELOG.md

### Features
- Convert PowerPoint slides to Webflow sections
- Extract and preserve text styling (fonts, colors, sizes)
- Extract images with automatic file organization
- Generate responsive CSS with mobile breakpoints
- Create Webflow-ready export package (ZIP)
- Support for custom section prefixes
- Flexible output directory configuration
- Detailed conversion summary reports

### Supported Elements
- Text elements with styling preservation
- Images with positioning
- Shapes with fill and border colors
- Background colors
- Z-index layering

### Output Formats
- HTML5 semantic structure
- CSS3 with responsive breakpoints
- Individual section HTML files
- Combined index.html
- Webflow import package (ZIP)
- Conversion summary (TXT)

## [Unreleased]

### Planned Features
- Webflow API integration for direct import
- Advanced animation conversion
- Custom font importing
- Image optimization options
- Multi-page site support
- Template system for common layouts
- Configuration file support
- GUI interface
- Webflow CMS integration
- Advanced shape support
- Gradient and shadow effects
- Video embedding support

---

## Version History

- **1.0.0** (2024-11-18) - Initial release with core conversion functionality
