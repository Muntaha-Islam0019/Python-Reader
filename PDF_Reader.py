import pyttsx3
import PyPDF2

book = open('Selections of Favourite Poems.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)

page_count = pdf_reader.numPages

speaker = pyttsx3.init()

for page_number in range(1, page_count):
    page = pdf_reader.getPage(1)
    text = page.extractText()

    speaker.setProperty('rate', 100)
    speaker.say(text)
    speaker.runAndWait()
