import pytesseract
from PIL import Image
from translate import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image = Image.open ('12ab.jpg')

text = pytesseract.image_to_string(image, lang='eng')

translator= Translator(to_lang="fr",from_lang="eng")

translated_text =translator.translate(text)

print('original text:',text)
print('Translated text:',translated_text)
