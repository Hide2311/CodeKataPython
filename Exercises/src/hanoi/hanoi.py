# -*- coding: utf-8 -*-

class Hanoi:
    
    global int_count
    
    def __init__(self, count):
        try:
            self.int_count = int(count);
        except Exception:
            print '入力が無効です'
            quit()
    
    def hanoi(self, n, from_, to, via):
        if n == 1:
            print u'%d 番の円盤を %s から %s へ移動' % (n, from_, to)
        else:
            self.hanoi(n - 1, from_, via, to)
            print u'%d 番の円盤を %s から %s へ移動' % (n, from_, to)
            self.hanoi(n - 1, via, to, from_)
            
    def start(self):
        
        try:
            self.hanoi(self.int_count, 'A', 'B', 'C')
        except RuntimeError:
            print '数値が大き過ぎます'
            return None
        