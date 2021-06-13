import pytesseract
from pdf2image import convert_from_path
import os
from PIL import Image


""" pdf convert to png """
def pdf_to_png(pdf_path):
    images = convert_from_path(pdf_path) # images : list file
    images[0].save('./test1.png')

""" save results """
def str_to_txt(text_name, result_text):
    with open(text_name + '.txt', 'w', encoding='utf-8') as f:
        f.write(result_text)

if __name__=='__main__':

    file_name = 'test_1.png'
    pdf_path = os.path.join(os.getcwd(),file_name)
    result_text = pytesseract.image_to_string(Image.open(pdf_path), lang='kor+eng')
    text_name = file_name
    str_to_txt(text_name,result_text)
