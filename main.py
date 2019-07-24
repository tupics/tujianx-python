#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from Utils import Menu
from Utils import Lookup
from Utils import Pic
import sys, os

I = Menu.HoldList()

print(I.useindex)
sel = input(I.selinput)
if sel == '0':
    # 今日部分
    print(I.doingsort)
    Sorts = Lookup.Sort()
    print(I.nofsort.format(Sorts['count']))
    ListIndex = 0
    for s in Sorts['result']:
        print('{0}. {1}'.format(ListIndex, s['T_NAME']))
        ListIndex += 1
    sort = input(I.sortinput)
    RTID = Sorts['result'][int(sort)]['TID']
    Today = Lookup.TodayInfo(RTID)
    if Today:
        if Today[1] == 0:
            print(I.todaydisplay.format_map([Today[0]]))
        else:
            print(I.historytips.format(Today[1]))
            print(I.todaydisplay.format_map(Today[0]))
        IFShow = input(I.showpic)
        if IFShow == 'Y' or IFShow == 'y' or IFShow == '' or IFShow == '1':
            path = './TUPICS/{0}.jpeg'.format(Today[0]['PID'])
            if os.path.exists(path):
                print(I.foundlpic)
                ims = Pic.ras(path)
                NEXTsave = False
            else:
                ims = Pic.gas(Today[0]['local_url'])
                NEXTsave = True
            if NEXTsave:
                IFSave = input(I.savepic)
                if IFSave == 'Y' or IFSave == 'y' or IFSave == '' or IFSave == '1':
                    if not Pic.sil(ims, Today[0]['PID']):
                        print(I.error)
                        sys.exit()
                else:
                    print(I.donotsavepic)
        else:
            print(I.donotshowpic)
