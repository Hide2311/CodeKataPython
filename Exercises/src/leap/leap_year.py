# -*- coding: utf-8 -*-

"""
うるう年の判定
入力した4桁の数値がうるう年か判定します
判定クラス
"""

class LeapYear:
    
    # 入力された数値のint型を格納
    int_year = 0
    
    # コンストラクタ
    def __init__(self, year):
        self.int_year = int(year)
    
    # 閏年の判定
    def check_leap_year(self):
        
        # 4で割り切れ、100で割り切れないか。又は400で割り切れるか。
        if self.int_year % 4 == 0 and self.int_year % 100 != 0 or self.int_year % 400 == 0:
            print self.int_year, '年はうるう年です'
        else:
            print self.int_year, '年はうるう年ではありません'
            
        return True