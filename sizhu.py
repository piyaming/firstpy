#!/usr/bin/python3
import time
from datetime import date

class sizhu(object):
    def __init__(self, year, month, day, hou, minu):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hou = int(hou)
        self.minu = int(minu)
        self.t0 = time.mktime((1970, 1, 2, 0, 0, 0, 0, 0, 0))
        self.t1 = time.mktime((self.year, self.month, self.day, self.hou, self.minu, 0, 0, 0, 0))
        self.gan = {2: "甲", 3: "乙", 4: "丙", 5: "丁", 6: "戊", 7: "己", 8: "庚", 9: "辛", 0: "壬", 1: "癸"}
        self.zhi = {1: "未", 2: "申", 3: "酉", 4: "戌", 5: "亥", 6: "子", 7: "丑", 8: "寅", 9: "卯", 10: "辰", 11: "巳", 0: "午"}
        self.C = {2: 3.87, 3: 5.63, 4: 4.81, 5: 5.25,	6: 5.678, 7: 7.108,	8: 7.5,	9: 7.646, 10: 8.318, 11: 7.438,	12: 7.18, 1: 5.4055}
        self.jq = {}

    def ri(self):
        self.richa = int((self.t1-self.t0)/(24*60*60))
        self.shii = self.hou + self.minu / 100
        # print(self.shii)
        if self.shii > 23:
            return self.gan[(self.richa+1) % 10 ], self.zhi[(self.richa+1) % 12]
        else:
            return self.gan[self.richa % 10], self.zhi[self.richa % 12]

    def yue(self):
        if self.t1 < self.jieqi()[1]:
            self.yuez = "子"
        elif self.t1 < self.jieqi()[2]:
            self.yuez = "丑"
        elif self.t1 <self.jieqi()[3]:
            self.yuez = "寅"
        elif self.t1 <self.jieqi()[4]:
            self.yuez = "卯"
        elif self.t1 <self.jieqi()[5]:
            self.yuez = "辰"
        elif self.t1 <self.jieqi()[6]:
            self.yuez = "巳"
        elif self.t1 <self.jieqi()[7]:
            self.yuez = "午"
        elif self.t1 <self.jieqi()[8]:
            self.yuez = "未"
        elif self.t1 <self.jieqi()[9]:
            self.yuez = "申"
        elif self.t1 <self.jieqi()[10]:
            self.yuez = "酉"
        elif self.t1 <self.jieqi()[11]:
            self.yuez = "戌"
        elif self.t1 <self.jieqi()[12]:
            self.yuez = "亥"
        else:
            self.yuez = "子"

        if self.nian()[0] == "甲" or self.nian()[0] == "己":
            self.yueg = {"寅":"丙",	"卯":"丁",	"辰":"戊",	"巳":"己",	"午":"庚",	"未":"辛",	"申":"壬",	"酉":"癸",	"戌":"甲",	"亥":"乙",	"子":"丙",	"丑":"丁"}
        elif self.nian()[0] == "乙" or self.nian()[0] == "庚":
            self.yueg = {"寅":"戊",	"卯":"己",	"辰":"庚",	"巳":"辛",	"午":"壬",	"未":"癸",	"申":"甲",	"酉":"乙",	"戌":"丙",	"亥":"丁",	"子":"戊",	"丑":"己"}
        elif self.nian()[0] == "丙" or self.nian()[0] == "辛":
            self.yueg = {"寅":"庚",	"卯":"辛",	"辰":"壬",	"巳":"癸",	"午":"甲",	"未":"乙",	"申":"丙",	"酉":"丁",	"戌":"戊",	"亥":"己",	"子":"庚",	"丑":"辛"}
        elif self.nian()[0] == "丁" or self.nian()[0] == "壬":
            self.yueg = {"寅":"壬",	"卯":"癸",	"辰":"甲",	"巳":"乙",	"午":"丙",	"未":"丁",	"申":"戊",	"酉":"己",	"戌":"庚",	"亥":"辛",	"子":"壬",	"丑":"癸"}
        elif self.nian()[0] == "戊" or self.nian()[0] == "癸":
            self.yueg = {"寅":"甲",	"卯":"乙",	"辰":"丙",	"巳":"丁",	"午":"戊",	"未":"己",	"申":"庚",	"酉":"辛",	"戌":"壬",	"亥":"癸",	"子":"甲",	"丑":"乙"}

        return self.yueg[self.yuez], self.yuez

    def nian(self):
        if self.t1 < self.jieqi()[2]:
            return self.gan[(self.year-1970-3) % 10], self.zhi[(self.year-1970+3) % 12]
        elif self.t1 >=self.jieqi()[2]:
            return self.gan[(self.year-1970-2) % 10], self.zhi[(self.year-1970+4) % 12]

    def shi(self):
        self.shii = self.hou + self.minu/100
        if self.shii < 1 :
            self.shiz = "子"
        elif self.shii < 3:
            self.shiz = "丑"
        elif self.shii < 5:
            self.shiz = "寅"
        elif self.shii < 7:
            self.shiz = "卯"
        elif self.shii < 9:
            self.shiz = "辰"
        elif self.shii < 11:
            self.shiz = "巳"
        elif self.shii < 13:
            self.shiz = "午"
        elif self.shii < 15:
            self.shiz = "未"
        elif self.shii < 17:
            self.shiz = "申"
        elif self.shii < 19:
            self.shiz = "酉"
        elif self.shii < 21:
            self.shiz = "戌"
        elif self.shii < 23:
            self.shiz = "亥"
        else:
            self.shiz = "子"

        if self.ri()[0] == "甲" or self.ri()[0] == "己":
            self.shig = {"子":"甲",	"丑":"乙",	"寅":"丙",	"卯":"丁",	"辰":"戊",	"巳":"己",	"午":"庚",	"未":"辛",	"申":"壬",	"酉":"癸",	"戌":"甲",	"亥":"乙"}
        elif self.ri()[0] == "乙" or self.ri()[0] == "庚":
            self.shig = {"子":"丙",	"丑":"丁",	"寅":"戊",	"卯":"己",	"辰":"庚",	"巳":"辛",	"午":"壬",	"未":"癸",	"申":"甲",	"酉":"乙",	"戌":"丙",	"亥":"丁"}
        elif self.ri()[0] == "丙" or self.ri()[0] == "辛":
            self.shig = {"子":"戊",	"丑":"己",	"寅":"庚",	"卯":"辛",	"辰":"壬",	"巳":"癸",	"午":"甲",	"未":"乙",	"申":"丙",	"酉":"丁",	"戌":"戊",	"亥":"己"}
        elif self.ri()[0] == "丁" or self.ri()[0] == "壬":
            self.shig = {"子":"庚",	"丑":"辛",	"寅":"壬",	"卯":"癸",	"辰":"甲",	"巳":"乙",	"午":"丙",	"未":"丁",	"申":"戊",	"酉":"己",	"戌":"庚",	"亥":"辛"}
        elif self.ri()[0] == "戊" or self.ri()[0] == "癸":
            self.shig = {"子":"壬",	"丑":"癸",	"寅":"甲",	"卯":"乙",	"辰":"丙",	"巳":"丁",	"午":"戊",	"未":"己",	"申":"庚",	"酉":"辛",	"戌":"壬",	"亥":"癸"}

        return self.shig[self.shiz], self.shiz

    def jieqi(self):
        self.jq = {1: time.mktime((self.year, 1, int((self.year - 2000) * 0.2422 + self.C[1]) - int(
            ((self.year - 2000) - 1) / 4), 0, 0, 0, 0, 0, 0))}

        for i in range(2, 13):
            self.jq.update({i: time.mktime((self.year, i, int(((self.year - 2000)*0.2422+self.C[i])-int((self.year - 2000-1) / 4)), 0, 0, 0, 0, 0, 0))})
        return self.jq

    def xinqi(self):
        self.xq = {1: "星期一", 2: "星期二", 3: "星期三", 4: "星期四", 5: "星期五", 6: "星期六", 7: "星期日"}
        return self.xq[date(self.year, self.month, self.day).isoweekday()]

if __name__ == '__main__':
    year = input("输入年份：")
    month = input("输入月份：")
    day = input("输入日期：")
    hours = input("输入小时：")
    minute = input("输入分钟：")
    td = sizhu(year, month, day, hours, minute)
    # td = sizhu(time.localtime()[0], time.localtime()[1],time.localtime()[2], time.localtime()[3], time.localtime()[4])
    print(td.jieqi())
    print("年：", td.nian())
    print("月：", td.yue())
    print("日：", td.ri())
    print("时：", td.shi())
    print(td.xinqi())



    # 将当前时间变
    # tt = time.localtime(time.time())
    # print(tt.tm_year)
    # print(time.localtime())

