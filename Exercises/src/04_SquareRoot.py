# -*- coding: utf-8 -*-

"""
平方根を求める
入力した値の平方根を求めます
"""

class SquareRoot:
    
    float_count = 0.0
    
    # コンストラクタ
    def __init__(self): 
        # 値の入力 & float型に変換
        self.float_count = float(input('input number : '))
    
    # 平方根の計算
    def calculate_square(self):
        square_root = self.float_count / 2.0
        last_square = 0.0
        
        while square_root != last_square:
            last_square = square_root
            square_root = (square_root + self.float_count / square_root) / 2.0
        
        print self.float_count, ':',  square_root

# -------------------------------------------------------- #

# 小数点を文字列と判定するため入力チェックは外す！
"""
if count.isdigit() == False or float(count) == 0:
    print '整数値、又は0以上を入力してください'
    quit()
"""

sr = SquareRoot()
sr.calculate_square()