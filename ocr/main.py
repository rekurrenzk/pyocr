from PIL import Image
import pytesseract
from pathlib import Path

rd = Path(__file__).resolve().parents[1]
print(rd)


def pdf_ocr_text(pdf_path) -> str:
    image = Image.open(pdf_path)
    text = pytesseract.image_to_string(image)
    return text

rdd = rd / "pdf" / "adalet" / "adalet-sayfa-1.pdf"
pdf_ocr_text(rdd)
