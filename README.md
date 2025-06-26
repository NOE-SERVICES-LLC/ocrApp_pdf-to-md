# OCR Markdown Converter

This Python tool converts scanned PDF documents into clean, structured Markdown (`.md`) files using OCR. It preserves the document's original layout as readable text, making it ideal for downstream processing like search indexing, NLP, or vector database embedding. The tool supports batch processing and is optimized for high-DPI OCR using Tesseract and Poppler.

---

## 📦 Installation

### 1. Clone or copy the project

```bash
git clone <your-repo-url>
cd ocrApp_pdf-to-md
```

### 2. Install required Python packages

```bash
pip install pdf2image pytesseract pillow
```

### 3. Install Poppler (PDF to image converter)

- Download from: [https://github.com/oschwartz10612/poppler-windows/releases](https://github.com/oschwartz10612/poppler-windows/releases)
- Extract and add the `poppler-xx/Library/bin` folder to your **System PATH**.

### 4. Install Tesseract OCR

- Download from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

use the .exe from the site or ->

sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

---

## 📂 Folder Structure

```
OCRtool/
│
├── pdfs/                  # Put all input PDF files here
├── markdown_output/       # Markdown results will be saved here
└── ocrApp.py              # Main script
```

---

## 🚀 Usage

```bash
py ocrApp.py
```

- Processes all PDFs in the `pdfs/` folder
- Outputs corresponding `.md` files in the `markdown_output/` folder
- Removes page numbers and preserves original formatting as closely as possible

---

## ✅ Output Example

```markdown
# Anorexia Nervosa: Outpatient Care

Admission criteria:
- BMI above 17
- No acute medical risk

Treatment options:
- Family therapy
- Meal supervision
```

---

## 📌 Dependencies

- Python 3.7+
- Poppler (for PDF → Image)
- Tesseract OCR (for Image → Text)
- Python packages: `pdf2image`, `pytesseract`, `Pillow`

---

## 🧠 Use Cases

- Prepare structured clinical documents for semantic search
- Convert scanned guidelines for embedding in vector databases
- Enable NLP workflows on scanned PDFs
