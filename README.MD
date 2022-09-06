# 移动滑块验证识别库

## 说明：滑块验证码识别库基于[Python](https://www.python.org/)+[Selenium](https://www.selenium.dev/)+`谷歌内核驱动`打造，本项目遵循开源本心和易用、实用、好用的原则。在此说明，请勿非法使用否则后果自负！


## 支持平台
- [x] 抖音
- [ ] 快手
- [ ] 腾讯
- [ ] 百度
- [ ] 京东


## 使用教程

### 抖音
```python

if __name__ == '__main__':
    # 移动滑块背景图片地址
    h1 = 'https://p9-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/488881e7216246249a5d81cddcb69c43~tplv-188rlo5p4y-2.jpeg'
    # 移动滑块图片地址
    h2 = 'https://p9-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/e7bcbd4bb0374580a2358e029f83b84f~tplv-188rlo5p4y-1.png'
    # 识别获取X移动距离
    x = getTargetSliderPointX(h1, h2)
    options = webdriver.ChromeOptions()
    web = webdriver.Chrome(options=options)
    web.get('https://www.douyin.com/')
    # ...... 此处省略其他操作
    startMove(web, x, '//*[@id="secsdk-captcha-drag-wrapper"]/div[2]')

```

