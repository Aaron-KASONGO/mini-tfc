from PyPDF2 import PdfFileReader
import requests

class ReaderSearch:

    def __init__(self, pdf):
        self.links = []
        self.doc = PdfFileReader(pdf)
        self.get_metada()

    def get_metada(self):
        self.metadata = self.doc.getDocumentInfo()
        self.numberPages = self.doc.numPages

    def readPDF(self):
        for page in range(self.numberPages):
            pageObj = self.doc.getPage(page)
            text = pageObj.extractText()
            if len(text) > 500:
                self.search_api(text.replace('\n', ' '))
                
        
    def search_api(self, query):
        dico = {}
        url = "https://google-search3.p.rapidapi.com/api/v1/search/q=" + query + " filetype:pdf"

        headers = {
            "X-RapidAPI-Key": "16eac3293amshbe8a4ddc5135c5fp18f098jsn68def8f3a8a8",
            "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
        }

        x = requests.get(url, headers=headers)

        if x.status_code == 200:
            for i in x.json()['results']:
                if 'pdf' in i['link'][-4:]:
                    dico['title'] = i['title']
                    dico['link'] = i['link']
                    self.links.append(dico)

