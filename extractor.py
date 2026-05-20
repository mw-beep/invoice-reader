import pdfplumber



def extract_text_from_pdf(pdf_path):

    with pdfplumber.open(pdf_path) as pdf:

        extracted_text = []
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text is None:
               print (f"no text found on {page_number}")
            else:
                extracted_text.append(text)


        full_text = "\n".join(extracted_text)
    return full_text
