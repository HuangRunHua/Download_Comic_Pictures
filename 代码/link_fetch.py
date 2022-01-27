import requests
import numpy as np
from sympy import *
from bs4 import BeautifulSoup
np.seterr(divide='ignore', invalid='ignore')

"""
本程序用于下载金田一37岁事件薄的图片链接
链接: https://www.maofly.com/manga/10736.html

在使用本程序时需要在Chrome或Safari上预先加载好图片再将网页内容下载保存为html文件
html文件内容应当如下:
<div class="img-content" style="display:flex;flex-direction: column;">
	<img class="img-fluid show-pic" src="https://mao.mhtupian.com/uploads/img/26847/348716/01.jpg">
	<img src="https://mao.mhtupian.com/uploads/img/26847/348716/02-03.jpg" class="img-fluid">
    ......
</div>
"""

def get_all_links(path):
    # 打开并读取php文件
    phpFile = open(path, 'r', encoding='utf-8')
    phpHandle = phpFile.read()
    soup = BeautifulSoup(phpHandle, 'lxml')

    for img in soup.select('img'):
        print(img["src"])


get_all_links('网页/03.html')
