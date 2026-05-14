from pathlib import Path
from pypdf import PdfReader


class DocumentLoader:

    def load_txt(self, file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.read()

    def load_pdf(self, file_path):

        pdf = PdfReader(file_path)

        text = ""

        for page in pdf.pages:

            text += page.extract_text()

        return text

    def load_documents(self, directory):

        documents = []

        path = Path(directory)

        for file in path.iterdir():

            if file.suffix == ".txt":

                text = self.load_txt(file)

                documents.append(text)

            elif file.suffix == ".pdf":

                text = self.load_pdf(file)

                documents.append(text)

        return documents