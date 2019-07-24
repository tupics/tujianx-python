# -*- coding: UTF-8 -*-
from PIL import Image
from io import BytesIO
import os
import requests as req
headers = {'user-agent': 'TujianXPython'}
def gas(url):
    "获取！显示！"
    lres = req.get(url, headers=headers)
    pres = Image.open(BytesIO(lres.content))
    pres.show()
    return pres

def sil(IMGres, PID):
    "存！"
    try:
        localtion = './TUPICS/{0}.{1}'
        IMGres.save(localtion.format(PID, 'jpeg'), 'jpeg')
        return True
    except:
        return False

def ras(path):
    pres = Image.open(path)
    pres.show()
    return pres