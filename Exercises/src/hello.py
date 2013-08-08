# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 2:
    print u"引数を入力してください。"
    quit()

count = int(sys.argv[1])
for i in range(0, count):
    print "Hello World!", i + 1


