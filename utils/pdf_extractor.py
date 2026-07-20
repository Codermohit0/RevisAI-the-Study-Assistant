import pdfplumber

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            page_text_pdf = page.extract_text()
            if page_text_pdf is None :
                page_text_pdf = ""
            full_text += page_text_pdf
    return  full_text
if __name__ == "__main__":
    result = extract_text_from_pdf("data/Hands-On_Machine_Learning.pdf")
    print(result[:10000])
    