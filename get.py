# -*- coding: UTF-8 -*-
import urllib.request
import json
import restartmodule
def getpicinfo(cate,act):
    "用于获取图片信息"
    cate = urllib.parse.quote(cate)
    webpath = "https://dp.chimon.me/api/" + act + ".php?sort=" + cate
    data = urllib.request.urlopen(webpath)
    decodedata = json.loads(data.read())
    if decodedata['status'] == 'ok':
        picdata = decodedata['pictures'][0]
        print('PID: '+ picdata['PID'] + '\n' + picdata['p_title'] + '\n' + picdata['p_content'] + '提交者:' + picdata['username'] + '\n' + '链接:' + picdata['p_link'] + '\n' + '分类:' + picdata['TNAME'])
        global piclink
        piclink = picdata['p_link']
        global picid
        picid = picdata['PID']
    else:
        print("连图也没有")
        restartmodule.restart_program()

def getpicfile(link, picid):
    "用于获取图片文件"
    import os
    import filetype
    if not os.path.exists(os.environ['HOME'] + "TUJIANPIC"):
        os.mkdir(os.environ['HOME'] + '/TUJIANPIC', 755)
    path = os.environ['HOME'] + "/TUJIANPIC/" + picid
    urllib.request.urlretrieve(link, path)
    pictype = filetype.guess(path)
    os.rename(path, path + pictype.extension)
    global pathfnish
    pathfnish = path + pictype.extension