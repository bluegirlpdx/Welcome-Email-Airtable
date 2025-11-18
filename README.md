# FLOWLab⁵ Welcome Email Template for Airtable

This repository contains the email template for welcoming new members to FLOWLab⁵, formatted for Airtable's Markdown/HTML hybrid system.

## Files

- **`airtable-email-template.txt`** - The working template (Markdown + HTML for Airtable)
- `email-template.html` - Pure HTML version (not for Airtable, ignore this)

## How to Use in Airtable

1. Open `airtable-email-template.txt`
2. Copy the entire contents
3. Paste into your Airtable automation email body
4. Replace `{tier}` with your Airtable field reference (e.g., insert the actual field)

## What Was Fixed

### The Problem
Your original code had Markdown links **outside** of styled `<span>` tags:
```
</span> [Contact us here.](mailto:info@flowlab5.org)
```
This caused links to render at the default font size instead of inheriting your styled size.

### The Solution
Now all Markdown is **inside** the span tags:
```
<span style="font-size: 18px; ...">Please visit the [Onboarding hub](url) here.</span>
```
The Markdown links now inherit the 18px font size from the enclosing span!

### Other Improvements
- ✅ Consistent font sizes: 20px greeting, 18px body, 16px mission
- ✅ Fixed "Montserrat medium" to use `font-weight: 600` (proper CSS)
- ✅ Removed extra spaces and inconsistent span breaks
- ✅ Cleaned up line breaks
- ✅ Each paragraph is one complete span (easier to maintain)

## Airtable's Markdown/HTML Format

Airtable supports a hybrid of Markdown and HTML:
- **Markdown**: `**bold**`, `_italics_`, `[links](url)`
- **HTML**: `<span>`, `<br>`, inline styles
- **You can mix them!** Put Markdown inside HTML tags

## Brand Colors

- **Purple (brand)**: `#3D2CAF` - Headings, mission statement
- **Dark blue (text)**: `#120935` - Body text
- **Font**: Montserrat, sans-serif

## Tips

1. Keep Markdown **inside** `<span>` tags so links inherit font size
2. Use `font-weight: 600` instead of "Montserrat medium"
3. Use consistent font sizes (18px for body text)
4. Each paragraph = one complete span tag

## Support

For questions, contact: info@flowlab5.org
