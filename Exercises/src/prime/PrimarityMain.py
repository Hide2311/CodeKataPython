# -*- coding: utf-8 -*-

import PrimarityNumber

"""
素数判定
MainClass
"""

class MainClass:    
    if __name__ == "__main__":
        count = raw_input('input number : ') 
        if count.isdigit() == False or int(count) == 0:
            print '整数値、又は0以上を入力してください'
            quit()
    
        pn = PrimarityNumber.PrimarityNumber(count);

        if pn.primarity_check():
            print '素数です'
        else:
            print '素数じゃない'
