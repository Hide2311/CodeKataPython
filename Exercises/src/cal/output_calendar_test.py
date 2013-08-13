# -*- coding: utf-8 -*-

import pytest
import output_calendar

@pytest.mark.parametrize(("num", "num1"),[(2013,8),(201,8),(2013,80),('2013','8')])

def test_is_root(num, num1):
    oc = output_calendar.OutputCalendar(num, num1)
    assert oc.textOutput() is True