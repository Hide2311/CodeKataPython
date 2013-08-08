# -*- coding: utf-8 -*-

import leap_year

"""
うるう年の判定
入力した4桁の数値がうるう年か判定します
メインクラス
"""

class CalendarMain:
    if __name__ == "__main__":
        input_year = raw_input('input year : ') 

        # 入力チェック。4桁の整数値か
        if input_year.isdigit() == False or len(input_year) != 4:
            print '整数値の4桁で入力してください'
            quit()
        
        lp = leap_year.LeapYear(input_year)
        lp.check_leap_year()