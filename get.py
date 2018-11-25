# -*- coding: UTF-8 -*-
import json
import urllib.request

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
        return picdata
    else:
        print("连图也没有")
        restartmodule.restart_program()

def getpicfile(link, picid):
    "用于获取图片文件"
    import os
    import filetype
    print(link)
    storagedir = os.path.expanduser('~') + '/TUJIANPIC'
    if not os.path.exists(storagedir):
        os.mkdir(storagedir, 755)
    path = storagedir + picid
    urllib.request.urlretrieve(link, path)
    pictype = filetype.guess(path)
    if not os.path.exists(path + '.' + pictype.extension):
        os.rename(path, path + '.' + pictype.extension)
    else:
        os.remove(path)
    return path + '.' + pictype.extension