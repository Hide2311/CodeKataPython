# -*- coding: utf-8 -*-

import random

class NumberGame:
    
    global random_num, flg
    
    def __init__(self):
        self.random_num = random.randint(1, 100)
        
        print self.random_num
        
        self.flg = True
        
    def test(self):
        
        while self.flg:
            try:
                input_num = int(input("answer : "))
            except Exception:
                print u'入力が無効です'
                continue
            
            if input_num < self.random_num:
                print u'上'
            elif input_num > self.random_num:
                print u'下'
            else:
                print u'ok'
                self.flg = False 
    
