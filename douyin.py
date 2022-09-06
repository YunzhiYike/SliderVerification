import os
import random
import time
from PIL import Image
import cv2
import requests as requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver


# 获取滑块验证图片写入本地
def getCatpcha(verifyBgUrl, verifyPointUrl):
    # 下载图片资源
    pic1 = requests.get(verifyBgUrl).content
    pic2 = requests.get(verifyPointUrl).content
    # 增加保存图片的前缀
    fileFix = int(time.time())
    fileFix = str(fileFix)
    bg = fileFix + 'bg.jpg'
    point = fileFix + 'point.jpg'
    with open(bg, 'wb') as f:  # 要写入本地
        f.write(pic1)
    with open(point, 'wb') as f:  # 要写入本地
        f.write(pic2)
    return bg, point


# 获取滑块最终需要移动到到坐标X位置
def getTargetSliderPointX(verifyBgUrl, verifyPointUrl):
    # 下载图片并返回保存路径
    bgFilePath, pointFilePath = getCatpcha(verifyBgUrl, verifyPointUrl)
    bgImg = cv2.imread(bgFilePath)
    # 变成BRG格式来OpenCV处理
    pointImg = cv2.imread(pointFilePath)
    # 获取图像的边缘，Canny（图，阈值，阈值）
    bgEdge = cv2.Canny(bgImg, 100, 200)
    tpEdge = cv2.Canny(pointImg, 100, 200)
    bgPic = cv2.cvtColor(bgEdge, cv2.COLOR_GRAY2RGB)  # 颜色空间转换函数，cvtColor（图，要变成的格式）
    ptPic = cv2.cvtColor(tpEdge, cv2.COLOR_GRAY2RGB)
    # 缺口匹配
    res = cv2.matchTemplate(bgPic, ptPic, cv2.TM_CCOEFF_NORMED)
    # 寻找最优匹配
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 读取背景图片
    bgImg = Image.open(bgFilePath)
    bgImgSize = bgImg.size
    # 根据图片真实与表面大小的比例进行缩放
    x = max_loc[0] * bgImgSize[1] / bgImgSize[0]
    # 删除下载的文件
    os.unlink(bgFilePath)
    os.unlink(pointFilePath)
    return x

# 移动滑块 web=webdriver distance=水平移动距离x element=滑块xpath语法匹配
def startMove(web, distance, element):
    element = web.find_element(By.XPATH, element)
    # 开始移动
    ActionChains(web).click_and_hold(element).perform()
    time.sleep(0.5)
    while distance > 0:
        if distance > 20:
            # 如果距离大于20，就让他移动快一点
            span = random.randint(60, 70)
        else:
            # 快到缺口了，就移动慢一点
            span = random.randint(45, 50)
        ActionChains(web).move_by_offset(span, 0).perform()
        distance -= span
        time.sleep(random.randint(10, 50) / 100)

    ActionChains(web).move_by_offset(distance, 1).perform()
    ActionChains(web).release(on_element=element).perform()



