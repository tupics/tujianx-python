# -*- coding: UTF-8 -*-
import requests as req
import json
from datetime import date
headers = {'user-agent': 'TujianXPython'}
Api = 'https://v2.api.dailypics.cn'

def Sort():
    "获取分类"
    url = '{0}/sort'.format(Api)
    return req.get(url, headers=headers).json()

def TodayInfo(TID):
    "本日图片"
    url = '{0}/today?sort={1}'.format(Api, TID)
    Info = req.get(url, headers=headers).json()
    if len(Info) > 0:
        Todaydate = date.today()
        Photodate = date.fromisoformat(Info[0]['p_date'])
        if Todaydate == Photodate:
            Info.append(0)
        else:
            distance = Todaydate - Photodate
            Info.append(distance.days)
        return Info
    else:
        return False

def List(TID, Page):
    url = '{0}/list?page={1}&size=3&sort={2}&op=asc'.format(Api, Page, TID)
    return req.get(url, headers=headers).json()