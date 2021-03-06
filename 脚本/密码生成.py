# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:35:38 2019

@title: password generation

@author: 饭未眠

@email: ifansay.chn@qq.com
"""
import string
import random
import datetime
import pathlib
import os
import winsound
from functools import reduce


worddict = {'1': string.digits,
            '2': string.ascii_lowercase,
            '3': string.ascii_uppercase,
            '4': string.punctuation,
            '5': '_'
            }


def infoInput():
    tags = input('请输入账号归属(最长15位,英文):')[:15]
    account = input('请输入账号(最长30位,英文):')[:30]
    passlong = int(input('请输入密码长度:'))
    mode = input('请输入密码组成类型(1.数字2.小写字母3.大写字母4.英文标点5.下划线,4包含5,5仅用于特殊要求)')
    file = input('请输入保存文件名称:')
    return tags, account, passlong, mode, file


def longCheck(long):
    if long < 8:
        print('密码最短6位')
    elif long > 35:
        print('密码最长35位')


def passwordProduct(mode, long):
    src = ''
    for no in mode:
        src += worddict[no]
    password = random.sample(src, sorted([6, long, 35])[1])  # 随机取n位,排序取中值
    str_password = ''.join(password)  # 将列表转化为字符串
    return str_password


def passwordCheck(mode, password):
    wordcheck = {}
    for no in mode:
        wordcheck[no] = len([i for i in password if i in worddict[no]])
    VerifyResult = reduce(lambda x, y: x * y, wordcheck.values())
    return VerifyResult


def passwordSave(tags, account, password, date, filename='个人'):
    path, code_file = os.path.split(os.path.realpath(__file__))
    file = '%s\\password\\%s密码.txt' % (path, filename)
    fileCheck = pathlib.Path(file).is_file()
    f = open(file, 'a+', encoding='utf-8')
    if not fileCheck:
        f.writelines('App&Web'.ljust(20, ' '))
        f.writelines('AccountNo'.ljust(35, ' '))
        f.writelines('Passwords'.ljust(40, ' '))
        f.writelines('CreatTime\n')
    f.writelines(tags.ljust(20, ' '))
    f.writelines(account.ljust(35, ' '))
    f.writelines(password.ljust(40, ' '))
    f.writelines(date.strftime('%Y/%m/%d %H:%M:%S'))
    f.writelines('\n')
    f.close()


def main():
    try:
        tags, account, long, mode, file = infoInput()
        longCheck(long)
        while True:
            word = passwordProduct(mode, long)
            result = passwordCheck(mode, word)
            if result > 0:
                passwordSave(tags, account, word, datetime.datetime.today(), file)
                print(tags, "的密码为:", word, '\n密码已存入文件')
                break
    except ValueError as e:
        print('ValueError', e)


if __name__ == '__main__':
    main()
    winsound.Beep(1000, 300)  # 其中400表示声音大小,1000表示发生时长,1000为1秒
    # input('\npress any key to exit')
