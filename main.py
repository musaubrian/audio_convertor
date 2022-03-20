from gtts import gTTS
import PyPDF2

language = 'en'
# cycles through the "book" saving the text to a full_text variable
with open('./book_to_convert.pdf', 'rb') as book:

    full_text = ""
    reader = PyPDF2.PdfFileReader(book)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content

# initialize the text to speech
convert_to_speech = gTTS(text=full_text, lang=language, slow=False)

# saved to
convert_to_speech.save('./mp3/output.mp3')
