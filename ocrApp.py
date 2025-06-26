import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# If Tesseract isn't in PATH, set this manually:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Input and output directories
INPUT_FOLDER = 'pdfs'  # Folder containing PDFs
OUTPUT_FOLDER = 'markdown_output'
DPI = 300  # Resolution for image conversion

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def pdf_to_images(pdf_path, dpi=300):
    return convert_from_path(pdf_path, dpi=dpi)

def extract_text_from_images(images):
    all_text = []
    for i, img in enumerate(images):
        print(f"  OCR page {i + 1}...")
        text = pytesseract.image_to_string(img)
        cleaned = text.strip().replace('\n\n', '\n')  # Remove extra newlines
        all_text.append(cleaned)
    return "\n\n".join(all_text)

def save_markdown(text, output_md_path):
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✓ Saved to {output_md_path}")

def process_pdf(file_path, output_md_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    print(f"\nProcessing '{base_name}'...")
    images = pdf_to_images(file_path, dpi=DPI)
    text = extract_text_from_images(images)
    save_markdown(text, output_md_path)

def main():
    for dirpath, _, files in os.walk(INPUT_FOLDER):
        for filename in files:
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(dirpath, filename)
                # Get relative path from input folder to the PDF
                rel_dir = os.path.relpath(dirpath, INPUT_FOLDER)
                # Output directory mirrors the input's subdirectory structure
                out_dir = os.path.join(OUTPUT_FOLDER, rel_dir)
                out_md_path = os.path.join(out_dir, os.path.splitext(filename)[0] + ".md")
                process_pdf(pdf_path, out_md_path)

if __name__ == "__main__":
    main()
