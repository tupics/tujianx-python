# -*- coding: UTF-8 -*-
import os, sys
class HoldList:
    useindex = '0. 今日图片\n1. 往日图片\n2. 结束\n'
    selinput = '选择一个动作?\n输入数字:\n>'
    doingsort = '\n查询分类...\n'
    nofsort = '目前有{0}个分类, 分别是:\n'
    sortinput = '选择分类(索引数字):\n>'
    picdisplay = '图片ID:{PID}\n图片标题:{p_title}\n简介:\n\n{p_content}\n\n宽度:{width}\n高度:{height}\n投递者:{username}\n链接:{local_url}'
    historytips = '\n这是{0}天前的图片，今天又鸽了'
    showpic = '\n你是不是要看看呢?(Y/N)\n>'
    foundlpic = '\n已发现保存图片\n'
    donotshowpic = '\n好吧你不想看\n'
    savepic = '\n存起来？(./TUPICS)[Y/N]\n>'
    donotsavepic = '\n好吧你不想存\n'
    error = '出现了个天秀的错误'
    Haction = '动作:查看/退出/下一张(Y/E/N)\n>'

    
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
