class PDFLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pdf(self):
        from PyPDF2 import PdfReader

        text = ""
        with open(self.file_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()