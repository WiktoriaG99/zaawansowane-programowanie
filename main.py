import pytesseract
import cv2


def ocr(path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    img = cv2.imread(path)
    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    data = pytesseract.image_to_string(img_convert, lang='eng', config='--psm 6')
    print(f"Tekst ze zdjęcia o nazwie: {path}: {data} ")

    cv2.imshow('image', img)
    cv2.waitKey()

def ocr_captcha(path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    img = cv2.imread(path)
    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    converted_img = cv2.threshold(cv2.GaussianBlur(img_convert, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.threshold(cv2.bilateralFilter(img_convert, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.threshold(cv2.medianBlur(img_convert, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.adaptiveThreshold(cv2.GaussianBlur(img_convert, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.adaptiveThreshold(cv2.bilateralFilter(img_convert, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.adaptiveThreshold(cv2.medianBlur(img_convert, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    data = pytesseract.image_to_string(converted_img, lang='eng', config='--psm 6')
    print(f"Captcha ze zdjęcia o nazwie: {path}: {data} ")

    cv2.imshow('image', img)
    cv2.waitKey()

ocr('photos/photo1.jpg')
ocr('photos/photo2.jpg')
ocr('photos/photo3.png')
ocr('photos/photo4.png')
ocr('photos/photo5.png')
ocr_captcha('photos/photo6.png')
ocr_captcha('photos/photo7.png')
ocr_captcha('photos/photo8.png')
ocr_captcha('photos/photo9.png')
