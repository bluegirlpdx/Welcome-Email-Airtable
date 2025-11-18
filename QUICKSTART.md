# Quick Start Guide

Get started with the Canva to Webflow Converter in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Export from Canva

1. Open your Canva website design
2. Click **Share** → **Download**
3. Select **Microsoft PowerPoint (.pptx)**
4. Save the file to your computer

## Step 3: Run the Converter

```bash
python canva_to_webflow.py your-canva-design.pptx
```

This creates an `output/` directory with:
- `index.html` - Your complete website
- `styles.css` - All styles
- `images/` - Extracted images
- `webflow-import.zip` - Ready to import

## Step 4: Review the Output

Open `output/index.html` in your browser to preview:

```bash
# macOS
open output/index.html

# Linux
xdg-open output/index.html

# Windows
start output/index.html
```

## Step 5: Import to Webflow

### Method 1: Custom Code (Recommended)

1. Create a new Webflow project
2. Add a new page or section
3. Add an **Embed** element
4. Copy the HTML from `output/index.html`
5. Add **Custom CSS** in Page Settings
6. Copy the CSS from `output/styles.css`

### Method 2: Manual Import

1. Create sections in Webflow for each slide
2. Add elements matching the generated HTML
3. Upload images to Webflow Assets
4. Apply styles from the CSS file

## Common Use Cases

### Landing Page
```bash
python canva_to_webflow.py landing-page.pptx -o landing
```

### Multi-page Site
```bash
python canva_to_webflow.py homepage.pptx -o site/home
python canva_to_webflow.py about.pptx -o site/about
python canva_to_webflow.py contact.pptx -o site/contact
```

### Non-responsive (Fixed Width)
```bash
python canva_to_webflow.py design.pptx --no-responsive
```

## Tips for Best Results

1. **Use Simple Layouts**: Complex overlapping elements may need adjustment
2. **Group Elements**: Group related items in Canva before exporting
3. **Standard Fonts**: Use web-safe fonts for better compatibility
4. **Consistent Spacing**: Use grid/guides in Canva for alignment
5. **Optimize Images**: Large images may need compression

## Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### Images not showing
- Check that `images/` folder exists in output
- Verify image paths in HTML are correct
- Upload images to Webflow Assets

### Layout looks different
- Adjust CSS positioning values
- Check responsive breakpoints
- Test at different screen sizes

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Customize the generated CSS
- Add Webflow interactions
- Set up responsive breakpoints
- Test across different browsers

## Need Help?

- Check [README.md](README.md) for detailed documentation
- Review the generated `conversion_summary.txt`
- Open an issue on GitHub

Happy converting! 🚀
