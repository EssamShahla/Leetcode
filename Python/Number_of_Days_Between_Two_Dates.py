class Solution(object):
    def daysBetweenDates(self, date1, date2):
        from datetime import datetime
        format = "%Y-%m-%d"
        date1_obj = datetime.strptime(date1, format)
        date2_obj = datetime.strptime(date2, format)
        delta = date2_obj - date1_obj
        return abs(delta.days)