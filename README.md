# IMG_to_Audio

I have created to separate python files 
1.Which converts image to text 2.Text to audio,I have implemented it separately to Know the outputs of image to text for check.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tess.

```bash
pip install pytesseract
```

## Usage

```python
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img = Image.open('download.png')
text = pytesseract.image_to_string(img)
```