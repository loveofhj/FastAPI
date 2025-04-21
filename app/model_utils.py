import easyocr
import cv2
import numpy as np

reader = easyocr.Reader(['ko', 'en'])

def predict(img_bytes):
    np_img = np.frombuffer(img_bytes, np.uint8)
    image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    results = reader.readtext(image)
    texts = [r[1].replace(' ', '') for r in results]
    return ''.join(texts)
