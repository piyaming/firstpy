#!/usr/bin/python3
import time
from datetime import date
import sxtwl


class sizhu(object):

    def __init__(self, year, month, day, hou, minu):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hou = int(hou)
        self.minu = int(minu)
        self.Dday = sxtwl.fromSolar(self.year, self.month, self.day)
        self.Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        self.Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        self.WeekCn = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]

    def ri(self):
        dTG = self.Dday.getDayGZ()
        return self.Gan[dTG.tg], self.Zhi[dTG.dz]

    def yue(self):
        mTG = self.Dday.getMonthGZ()
        return self.Gan[mTG.tg], self.Zhi[mTG.dz]

    def nian(self):
        yTG = self.Dday.getYearGZ()
        return self.Gan[yTG.tg], self.Zhi[yTG.dz]

    def shi(self):
        hTG = sxtwl.getShiGz(self.Dday.getDayGZ().tg, self.hou)
        return self.Gan[hTG.tg], self.Zhi[hTG.dz]

    def xinqi(self):
        return self.WeekCn[self.Dday.getWeek()]


if __name__ == '__main__':
    year = input("输入年份：")
    month = input("输入月份：")
    day = input("输入日期：")
    hours = input("输入小时：")
    minute = input("输入分钟：")
    td = sizhu(year, month, day, hours, minute)
    # td = sizhu(1984, 2, 25, 6, 10)
    print("年：", td.nian())
    print("月：", td.yue())
    print("日：", td.ri())
    print("时：", td.shi())
    print(td.xinqi())
