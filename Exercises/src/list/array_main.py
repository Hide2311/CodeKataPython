# -*- coding: utf-8 -*

"""
配列の先頭はそのままに、先頭以外の要素をすべて0に置き換える
"""

class ArrayMain:
    if __name__ == "__main__":
        
        arry = [1, 2, 3, 4, 5]
        
        print arry
        
        print '先頭以外を0に置換'
        
        for i in range(len(arry)):
            if i != 0:
                arry[i] = 0

        print arry
        
        
