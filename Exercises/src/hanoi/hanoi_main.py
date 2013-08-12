# -*- coding: utf-8 -*-

import hanoi

# デコレーションチェック
       
#hanoi(4,'A','B','C')

class HanoiMain:
    if __name__ == "__main__":
        
        count = raw_input('input number : ')
        h = hanoi.Hanoi(count)
                
        h.start();
        