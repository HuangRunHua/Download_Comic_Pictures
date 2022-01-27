import requests
import numpy as np
from sympy import *
from bs4 import BeautifulSoup
np.seterr(divide='ignore', invalid='ignore')

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    'Referer': "https://www.baidu.com",
}

"""
本程序用于下载金田一37岁事件薄的图片
链接: https://www.maofly.com/manga/10736.html

在使用本程序时需要在Chrome或Safari上预先加载好图片再将网页内容下载保存为html文件
html文件内容应当如下:
<div class="img-content" style="display:flex;flex-direction: column;">
	<img class="img-fluid show-pic" src="https://mao.mhtupian.com/uploads/img/26847/348716/01.jpg">
	<img src="https://mao.mhtupian.com/uploads/img/26847/348716/02-03.jpg" class="img-fluid">
    ......
</div>
"""

def get_all_pics(path):
    # 打开并读取php文件
    phpFile = open(path, 'r', encoding='utf-8')
    phpHandle = phpFile.read()
    soup = BeautifulSoup(phpHandle, 'lxml')
    # 用于保存图片的命名
    pic_index = 1

    for img in soup.select('img'):
        pic_name = str(pic_index) + ".jpg"
        f = open(pic_name,'wb')
        f.write(requests.get(img['src'], headers=headers).content)
        pic_index = pic_index + 1
        f.close()


get_all_pics('网页/03.html')
