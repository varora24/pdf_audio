import pyttsx3 #python library to convert text to speech
import PyPDF2 #python library to interact with pdf files

#customise these values
pagestart = 000 #insert page number from which you want to start reading here
filename = 'xxx.pdf' #insert name of file being read


book = open(filename, 'rb') #imports data from book and stores in the variable
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages #total number of pages in the book - used for program to know when to stop

speaker = pyttsx3.init() #initialises voice
for num in range(pagestart, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()