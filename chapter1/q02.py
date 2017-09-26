# -*- coding: utf-8 -*-

if __name__ == '__main__':
    str1 = u'パトカー'
    str2 = u'タクシー'
    result = ''
    for (a, b) in zip(str1, str2):
        result += a + b
    print(result)
