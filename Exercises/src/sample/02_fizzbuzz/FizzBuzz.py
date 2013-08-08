# -*- coding: utf-8 -*-

"""
・なんか偉い人が考えた問題
・ルールは以下の通り
    ⅰ. 1から順番に数を表示する
    ⅱ. その数が3で割り切れるなら"Fizz"、5で割り切れるなら"Buzz"、両方で割り切れるなら"FizzBuzz"と表示する
・要するに"1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz ･･･"と出力される
・プログラマかどうかがわかるんだとさ
・実行例
※実際は1行で表示
 ------------------------------------------------------------------------
| 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17        |
| Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 |
 ------------------------------------------------------------------------
"""

for i in range(1, 35):
    if i % 3 == 0 and i % 5 == 0:
        print "FizzBuzz",
    else:        
        if i % 3 == 0:
            print "Fizz", 
        else:
            if i % 5 == 0:
                print "Buzz",
            else:
                print i,