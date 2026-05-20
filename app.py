from extractor import extract_text_from_pdf

pdf_path = input("Enter PDF path: ")
text = extract_text_from_pdf(pdf_path)

print("\nEXTRACTED TEXT:\n")
print(text)