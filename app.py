from extractor import extract_text_from_pdf
from parser import parse_invoice_fields

pdf_path = input("Enter PDF path: ")
text = extract_text_from_pdf(pdf_path)

print("\nEXTRACTED TEXT:\n")
parsed_text = parse_invoice_fields(text)
print(text)
print(parsed_text)
