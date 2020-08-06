import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img = Image.open('download.png')
text = pytesseract.image_to_string(img)
# Open a file with access mode 'a'
with open("sample.txt", "w",encoding="utf-8") as file_object:
    # Append 'hello' at the end of file
    file_object.write(text)
#print(text)
