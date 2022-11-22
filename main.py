import pytesseract
import cv2

def ocr (path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    img = cv2.imread(path)
    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    data = pytesseract.image_to_string(img_convert, lang='eng', config='--psm 6')
    print(f"Tekst ze zdjęcia o nazwie: {path}: {data} ")

    cv2.imshow('image', img)
    cv2.waitKey()

ocr('photos/photo1.jpg')
ocr('photos/photo2.jpg')
ocr('photos/photo3.png')
ocr('photos/photo4.png')
ocr('photos/photo5.png')

