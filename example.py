import sxtwl

Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏",
        "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
        "立冬", "小雪", "大雪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
       "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
       "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]
XiZ = ['摩羯', '水瓶', '双鱼', '白羊', '金牛', '双子', '巨蟹', '狮子', '处女', '天秤', '天蝎', '射手']
WeekCn = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]

day = sxtwl.fromSolar(2021, 12, 21)

s = "农历:%d年%s%d月%d日" % (day.getLunarYear(False),
                        '闰' if day.isLunarLeap() else '', day.getLunarMonth(), day.getLunarDay())
print(s)

yTG = day.getYearGZ()
print("以立春为界的年干支", Gan[yTG.tg] + Zhi[yTG.dz])
print("以立春为界的生肖:", ShX[yTG.dz])

# 月干支
mTG = day.getMonthGZ()
print("月干支", Gan[mTG.tg] + Zhi[mTG.dz])

# 日干支
dTG = day.getDayGZ()
print("日干支", Gan[dTG.tg] + Zhi[dTG.dz])

# 时干支
for hour in range(24):
    # 第一个参数为该天的天干，第二个参数为小时
    hTG = sxtwl.getShiGz(dTG.tg, hour)
    print("%d时天干地支:" % (hour), Gan[hTG.tg] + Zhi[hTG.dz])

# 当日是否有节气
if day.hasJieQi():
    print('节气：%s' % jqmc[day.getJieQi()])
    # 获取节气的儒略日数
    jd = day.getJieQiJD()
    # 将儒略日数转换成年月日时秒
    t = sxtwl.JD2DD(jd)

    # 注意，t.s是小数，需要四舍五入
    print("节气时间:%d-%d-%d %d:%d:%d" % (t.Y, t.M, t.D, t.h, t.m, round(t.s)))
else:
    print("当天不是节气日")
