# -*- coding: utf-8 -*-

import os
from calendar import weekday, monthrange

class OutputCalendar(Exception):
    
    global year, month
    
    def __init__(self, input_year, input_month):
        
        try:
            self.year = int(input_year)
            self.month = int(input_month)
        except Exception:
            print 'input is invalid.'
            quit()
    
    def textOutput(self):
        
        week = ' Mo Tu We Th Fr Sa Su'
        f = open('output_calendar.txt', 'w')
        
        try:
            day = monthrange(self.year, self.month)[1]
            end_month = weekday(self.year, self.month, 1)
                   
            merge_data = '   ' * (end_month + 1) + '  '.join(map(str, range(1, 10))) + ' ' + ' '.join(map(str, range(10, day + 1)))
            
            f.write(week)
            
            for i, e in enumerate(merge_data):
                f.write(e)
                if i % len(week) == 0 or i + 1 == len(merge_data): 
                    f.write(os.linesep)
                    
            return True
        
        except Exception:
            print 'input is invalid.'            
            return False

        finally:
            f.close()
