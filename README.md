# pdf_audio
Given a PDF file as an input, the program is meant to convert all the text in the file into audio and provide it as the output.

# packages needed
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyttsx3 (to enable audio output) and PyPDF2 to enable reading data off the file.
```bash
pip install pyttsx3
```
```bash
pip install PyPDF2
```
# variables
1. pagestart - the page number to start reading the text from (it can avoid the cover page and table of contents through this)
2. filename - name of PDF file stored in same directory that you want to read from
3. book - stores data about the pdf like pagenumber, text etc
4. pdfReader - begins process of reading data from the PDF file
5. pages - stores number of pages in order to ensure the speaker stops before the end of the file
6. speaker - accesses the ability to speak the words in the pdf
7. text - stores the text collected from the selected page of the pdf

## contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
