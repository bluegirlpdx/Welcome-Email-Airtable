# FLOWLab⁵ Welcome Email Template

This repository contains the HTML email template for welcoming new members to FLOWLab⁵.

## Files

- `email-template.html` - Clean, formatted HTML email template for Airtable automation

## How to Use in Airtable

### Method 1: Copy the entire template
1. Open `email-template.html`
2. Copy the entire contents
3. In your Airtable automation, paste into the email body field
4. Make sure your email action is set to send HTML emails

### Method 2: Use Airtable's rich text editor
1. Open `email-template.html`
2. Copy the HTML code
3. In Airtable, switch the email body to "HTML mode" or "Code view"
4. Paste the template

## Dynamic Fields

The template includes a `{tier}` placeholder where you can insert the member's tier:
- In Airtable, replace `{tier}` with your dynamic field reference
- Example: Replace `{tier}` with something like `{{Tier}}` or your actual field name

## Key Features

- **Consistent font sizing**: 18px body text, 20px greeting, 16px mission statement
- **Proper hyperlinks**: All links maintain consistent font size
- **Brand colors**:
  - Primary purple: `#3D2CAF`
  - Text: `#120935`
- **Clean structure**: Properly formatted HTML with semantic elements

## Customization

To modify the template:
1. Edit `email-template.html`
2. Keep font sizes consistent (18px for body text)
3. Use the same color codes for brand consistency
4. Always include `font-size` in link styles to prevent shrinking

## Colors Used

- **Purple (brand)**: `#3D2CAF` - Used for headings, links, and emphasis
- **Dark blue (text)**: `#120935` - Primary text color
- **Font**: Montserrat (falls back to sans-serif)

## Support

For questions, contact: info@flowlab5.org
