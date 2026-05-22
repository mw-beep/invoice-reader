def parse_invoice_fields(text):
    lines = text.splitlines()
    d = {}
    for line in lines:
        clean_line = line.strip()

        if clean_line.startswith('Supplier'):
            d['supplier'] = clean_line.split(':',1)[1].strip()
        elif clean_line.startswith("Invoice number"):
            d["invoice_number"] = clean_line.split(":", 1)[1].strip()

        elif clean_line.startswith("Invoice date"):
            d["invoice_date"] = clean_line.split(":", 1)[1].strip()

        elif clean_line.startswith("Total amount"):
            d["total_amount"] = clean_line.split(":", 1)[1].strip()    
            
            
    return d