# -*- coding: utf-8 -*-

"""
素数判定
入力した値が素数かどうか判定します
"""

class PrimNumber:
    int_count = 0
    
    # コンストラクタ
    def __init__(self, count):
        self.int_count = int(count)
     
    # 素数判定
    def primarity_check(self):
        add_number = 2
        flg = True
        
        while add_number < self.int_count:
            if self.int_count % add_number == 0:
                flg = False
                break
            add_number += 1
            
        return flg