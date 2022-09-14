#!/usr/bin/python3
#coding=utf-8

import ddddocr


class ykocr(object):
    ocr = ddddocr.DdddOcr(show_ad=False)

    def imgToText(self, imgPath):
        with open(imgPath, 'rb') as f:
            imgs = f.read()
        res = self.ocr.classification(imgs)
        return res
