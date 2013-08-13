# -*- coding: utf-8 -*-

import hanoi

class HanoiMain:
    if __name__ == "__main__":
        
        count = raw_input('input number : ')
        h = hanoi.Hanoi(count)
                
        h.start();
        