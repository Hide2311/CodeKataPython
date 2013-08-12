# -*- coding: utf-8 -*-

import SquareRoot

"""
平方根を求める
MainClass
"""

class SquareMain:
    if __name__ == "__main__":
        # 小数点を文字列と判定するため入力チェックは外す！ 
        number = input('input number : ')      
        sr = SquareRoot.SquareRoot(number)
        sr.calculate_square()