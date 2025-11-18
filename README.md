# Canva to Webflow Converter

A tool that converts Canva websites into Webflow websites using PowerPoint as an intermediate format.

## Overview

This tool allows you to:
1. Export your Canva website design to PowerPoint (each page becomes a slide)
2. Convert the PowerPoint slides into Webflow-compatible HTML/CSS sections
3. Generate a ready-to-import Webflow site structure

## Features

- **PowerPoint Parsing**: Extracts content, images, text, and layout from PowerPoint slides
- **Smart Font Mapping**: Automatically maps Canva/PowerPoint fonts to Google Fonts or web-safe alternatives
- **Font Inspector**: Analyze fonts in your PowerPoint to see what's detected and how they'll be mapped
- **Layout Detection**: Analyzes slide layouts and converts them to responsive Webflow sections
- **Image Extraction**: Automatically extracts and organizes images from slides
- **Text Preservation**: Maintains text content, fonts, colors, and styling
- **Google Fonts Integration**: Automatically imports needed Google Fonts with proper weights
- **Webflow-Ready Output**: Generates clean HTML/CSS compatible with Webflow
- **Section-Based Structure**: Each PowerPoint slide becomes a Webflow section

## Prerequisites

- Python 3.8 or higher
- PowerPoint file exported from Canva
- (Optional) Webflow account for importing the generated code

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Welcome-Email-Airtable
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python canva_to_webflow.py input.pptx -o output_directory
```

### Advanced Options

```bash
python canva_to_webflow.py input.pptx \
  -o output_directory \
  --section-prefix "section" \
  --extract-images \
  --responsive \
  --webflow-export
```

### Command Line Arguments

- `input_file`: Path to the PowerPoint file exported from Canva (required)
- `-o, --output`: Output directory for generated files (default: `./output`)
- `--section-prefix`: Prefix for section class names (default: `section`)
- `--extract-images`: Extract images to separate folder (default: True)
- `--responsive`: Generate responsive CSS (default: True)
- `--webflow-export`: Generate Webflow-specific export format (default: True)
- `--preserve-fonts`: Attempt to preserve original fonts (default: True)

## Workflow

### Step 1: Export from Canva

1. Open your Canva website design
2. Go to **Share** → **Download**
3. Select **Microsoft PowerPoint** as the file type
4. Download the .pptx file

### Step 2: Convert to Webflow

```bash
python canva_to_webflow.py your-canva-design.pptx -o webflow-site
```

This will create:
```
webflow-site/
├── index.html               # Main HTML file with all sections
├── styles.css               # Compiled CSS styles with Google Fonts
├── sections/                # Individual section HTML files
│   ├── section-1.html
│   ├── section-2.html
│   └── ...
├── images/                  # Extracted images
│   ├── slide-1-img-1.png
│   └── ...
├── font_report.txt          # Font usage and mapping report
├── fonts_used.json          # Machine-readable font data
├── conversion_summary.txt   # Complete conversion summary
└── webflow-import.zip       # Ready-to-import Webflow package
```

### Step 3: Import to Webflow

1. Log in to your Webflow account
2. Create a new project or open existing one
3. Use the generated HTML/CSS in custom code sections
4. Upload images to Webflow assets
5. Adjust responsive breakpoints as needed

## Font Handling

### Inspecting Fonts Before Conversion

To see what fonts are in your PowerPoint file:

```bash
python font_inspector.py your-canva-design.pptx
```

This shows:
- All fonts detected
- How many times each is used
- Font sizes and colors
- Automatic mappings to Google Fonts
- Suggestions for unmapped fonts

**Export detailed font data:**
```bash
python font_inspector.py your-canva-design.pptx --export --mappings
```

Creates:
- `detected_fonts.json` - Complete font analysis
- `font_mappings_custom.json` - Template for custom mappings

### How Font Mapping Works

1. **Automatic Mapping**: Common fonts (Montserrat, Poppins, Roboto, etc.) are automatically mapped to Google Fonts
2. **Google Fonts Import**: The tool automatically generates the @import statement for all needed fonts
3. **Web-Safe Fallbacks**: Unmapped fonts fall back to web-safe alternatives
4. **Font Report**: Every conversion generates a `font_report.txt` showing what fonts were used and how they were mapped

### Handling Canva Custom Fonts

If Canva fonts aren't mapping correctly:

1. **Run the font inspector** to see what PowerPoint detected
2. **Check `font_report.txt`** in the output directory
3. **For unmapped fonts**: Edit `font_mappings_custom.json` to map to similar Google Fonts
4. **Upload to Webflow**: For truly custom fonts, you'll need to manually upload them to your Webflow project

### Font Output Files

After conversion, check:
- `output/styles.css` - Google Fonts @import at the top
- `output/font_report.txt` - Detailed font usage report
- `output/fonts_used.json` - Machine-readable font data

## How It Works

1. **PowerPoint Parsing**: Uses `python-pptx` to parse the PowerPoint file
2. **Content Extraction**: Extracts text, images, shapes, and layout information
3. **Layout Analysis**: Analyzes positioning and sizing of elements
4. **HTML Generation**: Creates semantic HTML structure for each slide/section
5. **CSS Generation**: Generates CSS with positioning, typography, and colors
6. **Webflow Optimization**: Applies Webflow best practices and conventions

## Output Structure

Each PowerPoint slide becomes a Webflow section with:
- Semantic HTML5 structure
- CSS classes following Webflow naming conventions
- Responsive design breakpoints
- Extracted images with optimized references
- Preserved text styling (fonts, colors, sizes)

## Limitations

- Complex animations are not converted
- Some custom fonts may need manual import
- Advanced Canva effects may require manual adjustment
- Webflow interactions need to be added manually in Webflow
- Exact pixel-perfect conversion may require fine-tuning

## Tips for Best Results

1. **Keep Layouts Simple**: Simpler Canva layouts convert more accurately
2. **Use Standard Fonts**: Web-safe fonts convert better
3. **Group Elements**: Group related elements in Canva for better section organization
4. **Consistent Spacing**: Use consistent margins and padding in Canva
5. **Test Responsive**: Review the output at different screen sizes

## Troubleshooting

**Issue**: Images not extracting properly
- **Solution**: Ensure images are embedded in the PowerPoint, not linked

**Issue**: Fonts look different
- **Solution**: Use `--preserve-fonts` flag and manually import fonts to Webflow

**Issue**: Layout doesn't match exactly
- **Solution**: Adjust CSS positioning values in the generated styles.css

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use and modify as needed.

## Support

For issues or questions, please open an issue on GitHub.
