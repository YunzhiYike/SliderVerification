from ykocr import ykocr

if __name__ == '__main__':
    ocr = ykocr()
    res = ocr.imgToText('1.png')
    print(res)
