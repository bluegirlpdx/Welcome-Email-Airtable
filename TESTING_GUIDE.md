# Testing Guide - How to Test with Your Canva File

## 📤 How to Upload Your PowerPoint File

### Method 1: Direct Upload (Easiest)
1. Simply drag and drop your `.pptx` file into the chat
2. Or click the paperclip/attach icon and select your file
3. I'll automatically have access to the uploaded file

### Method 2: Provide a Link
If your file is in cloud storage:
- Google Drive: Share link with "Anyone with link can view"
- Dropbox: Generate a direct download link
- OneDrive: Share link
- Any public URL to a `.pptx` file

## 🔍 Testing Workflow

Once you upload your file, I can:

### Step 1: Inspect the Fonts
```bash
python font_inspector.py your-file.pptx
```
This will show:
- All fonts detected in the PowerPoint
- How many times each font is used
- Font sizes, colors, and styles
- Whether we have automatic mappings for each font
- Suggestions for unmapped fonts

### Step 2: Export Font Data
```bash
python font_inspector.py your-file.pptx --export --mappings
```
This creates:
- `detected_fonts.json` - Complete font analysis
- `font_mappings_custom.json` - Template for custom font mappings

### Step 3: Run the Conversion
```bash
python canva_to_webflow.py your-file.pptx -o test-output
```
This will convert your file using the best available font mappings.

### Step 4: Review the Output
Check the generated files:
- `test-output/index.html` - See if fonts are applied correctly
- `test-output/styles.css` - Check the font-family declarations
- `test-output/font_report.txt` - Font usage summary

## 🎨 Handling Canva Custom Fonts

### If Fonts Are Missing/Wrong:

1. **Check the font inspector output** to see what names were detected
2. **For Canva proprietary fonts:**
   - Edit `font_mappings_custom.json`
   - Map to similar Google Fonts
   - Example:
     ```json
     {
       "Canva Sans": {
         "google": "Inter",
         "weights": [400, 500, 700]
       }
     }
     ```

3. **For custom uploaded fonts:**
   - You'll need to manually upload these fonts to Webflow
   - Or find similar alternatives on Google Fonts

## 📝 What to Look For

When you upload your file, tell me:
1. What fonts you used in Canva (if you know)
2. What you see when you open the PPT in PowerPoint
3. Whether the fonts look correct or are being replaced

I'll then:
- Inspect the file
- Show you exactly what fonts are detected
- Suggest the best mappings
- Run a test conversion
- Show you the results

## 🚀 Ready to Test!

Just upload your `.pptx` file or provide a link, and I'll:
1. Run the font inspector
2. Show you what was detected
3. Convert it to Webflow
4. Help you fix any font issues

---

**Pro Tip:** If you want to test just the font detection without converting,
just ask me to run the font inspector only!
