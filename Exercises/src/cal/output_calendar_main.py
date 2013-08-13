# -*- coding: utf-8 -*-

import output_calendar

class OutputCalendarMain:
    if __name__ == "__main__":
        input_year = raw_input('input year : ')
        input_month = raw_input('input month : ')
        
        oc = output_calendar.OutputCalendar(input_year, input_month)
        oc.textOutput()