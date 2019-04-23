# 八卦类
class bagua(object):
    def __init__(self, liuyao = "000000", dong = "000000"):
        self.liuyao = liuyao
        self.dong = dong
        # 64卦名 和 八宫卦名
        self.guaming64 = {
            0: "乾为天", 9: "兑为泽", 18: "离为火", 27: "震为雷", 36: "巽为风", 45: "坎为水", 54: "艮为山", 63: "坤为地",
            32: "天风姤", 41: "泽水困", 50: "火山旅", 59: "雷地豫", 4: "风天小畜", 13: "水泽节", 22: "山火贲", 31: "地雷复",
            48: "天山遁", 57: "泽地萃", 34: "火风鼎", 43: "雷水解", 20: "风火家人", 29: "水雷屯", 6: "山天大畜", 15: "地泽临",
            56: "天地否", 49: "泽山咸", 42: "火水未济", 35: "雷风恒", 28: "风雷益", 21: "水火既济", 14: "山泽损", 7: "地天泰",
            60: "风地观", 53: "水山蹇", 46: "山水蒙", 39: "地风升", 24: "天雷无妄", 17: "泽火革", 10: "火泽睽", 3: "雷天大壮",
            62: "山地剥", 55: "地山谦", 44: "风水涣", 37: "水风井", 26: "火雷噬嗑", 19: "雷火丰", 8: "天泽履", 1: "泽天夬",
            58: "火地晋", 51: "雷山小过", 40: "天水讼", 33: "泽风大过", 30: "山雷颐", 23: "地火明夷", 12: "风泽中孚", 5: "水天需",
            2: "火天大有", 11: "雷泽归妹", 16: "天火同人", 25: "泽雷随", 38: "山风蛊", 47: "地水师", 52: "风山渐", 61: "水地比"
        }
        self.baguaming = {0: "乾", 1: "兑", 2: "离", 3: "震", 4: "巽", 5: "坎", 6: "艮", 7: "坤"}
        # 八宫纳支
        self.qian = {1: "子", 2: "寅", 3: "辰", 4: "午", 5: "申", 6: "戌"}
        self.dui = {1: "巳", 2: "卯", 3: "丑", 4: "亥", 5: "酉", 6: "未"}
        self.li = {1: "卯", 2: "丑", 3: "亥", 4: "酉", 5: "未", 6: "巳"}
        self.zhen = {1: "子", 2: "寅", 3: "辰", 4: "午", 5: "申", 6: "戌"}
        self.xun = {1: "丑", 2: "亥", 3: "酉", 4: "未", 5: "巳", 6: "卯"}
        self.kan = {1: "寅", 2: "辰", 3: "午", 4: "申", 5: "戌", 6: "子"}
        self.gen = {1: "辰", 2: "午", 3: "申", 4: "戌", 5: "子", 6: "寅"}
        self.kun = {1: "未", 2: "巳", 3: "卯", 4: "丑", 5: "亥", 6: "酉"}
        # 藏爻
        self.cangyao = {"乾": "000000",	"兑": "001001",	"离": "010010",	"震": "011011",	"巽": "100100",	"坎": "101101",	"艮": "110110",	"坤": "111111"}
        # 地支五行
        self.DZ5x = {"子": "水", "丑": "土", "寅": "木", "卯": "木", "辰": "土", "巳": "火", "午": "火", "未": "土", "申": "金", "酉": "金",
                     "戌": "土", "亥": "水"}
        # 八卦六亲
        self.qian6qin = {"木": "妻财", "火": "官鬼", "土": "父母", "金": "兄弟", "水": "子孙"}
        self.dui6qin = {"木": "妻财", "火": "官鬼", "土": "父母", "金": "兄弟", "水": "子孙"}
        self.li6qin = {"木": "父母", "火": "兄弟", "土": "子孙", "金": "妻财", "水": "官鬼"}
        self.zhen6qin = {"木": "兄弟", "火": "子孙", "土": "妻财", "金": "官鬼", "水": "父母"}
        self.xun6qin = {"木": "兄弟", "火": "子孙", "土": "妻财", "金": "官鬼", "水": "父母"}
        self.kan6qin = {"木": "子孙", "火": "妻财", "土": "官鬼", "金": "父母", "水": "兄弟"}
        self.gen6qin = {"木": "官鬼", "火": "父母", "土": "兄弟", "金": "子孙", "水": "妻财"}
        self.kun6qin = {"木": "官鬼", "火": "父母", "土": "兄弟", "金": "子孙", "水": "妻财"}

        self.nazhi = {}
        self.guanazhi(self.xiaguashu(self.liuyao), self.shangguashu(self.liuyao))

    # 变卦
    def bian6(self):
        self.b6 = ""
        if self.dong != "000000":
            for i in range(0, 6, 1):
                if self.dong[i] == "0":
                    self.b6 = self.b6 + str(int(self.dong[i])+int(self.liuyao[i]))
                elif self.dong[i] == "1":
                    self.b6 = self.b6 + str(int(self.dong[i])-int(self.liuyao[i]))
            return self.b6
        elif self.dong =="000000":
            return  self.liuyao

    # 藏爻伏
    def cangyaofu(self,gs):
        if self.guagong(gs) == "乾":
            return self.cangyao["乾"]
        elif self.guagong(gs) == "兑":
            return self.cangyao["兑"]
        elif self.guagong(gs) == "离":
            return self.cangyao["离"]
        elif self.guagong(gs) == "震":
            return self.cangyao["震"]
        elif self.guagong(gs) == "巽":
            return self.cangyao["巽"]
        elif self.guagong(gs) == "坎":
            return self.cangyao["坎"]
        elif self.guagong(gs) == "艮":
            return self.cangyao["艮"]
        elif self.guagong(gs) == "坤":
            return self.cangyao["坤"]


    # 卦数
    def guashu(self, gf):
        return int(gf, 2)
    # 上卦数
    def shangguashu(self, sgs):
        return int(sgs[3:], 2)
    # 下卦数
    def xiaguashu(self, xgs):
        return int(xgs[:3], 2)

    def guaming(self, gs):
        return self.guaming64[gs]

    # 卦宫

    def guagong(self, gs):
        if gs in [0, 32, 48, 56, 60, 62, 58, 2]:
            return "乾"
        elif gs in [9, 41, 57, 49, 53, 55, 51, 11]:
            return "兑"
        elif gs in [18, 50, 34, 42, 46, 44, 40, 16]:
            return "离"
        elif gs in [27, 59, 43, 35, 39, 37, 33, 25]:
            return "震"
        elif gs in [36, 4, 20, 28, 24, 26, 30, 38]:
            return "巽"
        elif gs in [45, 13, 29, 21, 17, 19, 23, 47]:
            return "坎"
        elif gs in [54, 22, 6, 14, 10, 8, 12, 52]:
            return "艮"
        elif gs in [63, 31, 15, 7, 3, 1, 5, 61]:
            return "坤"

    # 卦类 六合 六冲 归魂 游魂

    def gualei(self, gs):
        if gs in [56, 41, 50, 59, 13, 22, 31, 7]:
            return "六合卦"
        elif gs in [0, 9, 18, 27, 36, 45, 54, 63, 3, 24]:
            return "六冲卦"
        elif gs in [58, 51, 40, 33, 30, 23, 12, 5]:
            return "游魂卦"
        elif gs in [2, 11, 16, 25, 38, 47, 52, 61]:
            return "归魂卦"
        else:
            return "　　　"

    # 卦纳支

    def guanazhi(self, xgs, sgs):
        if self.baguaming[xgs] == "乾" or self.baguaming[xgs] == "震":
            self.nazhi = {1: self.qian[1], 2: self.qian[2], 3: self.qian[3]}
        elif self.baguaming[xgs] == "兑":
            self.nazhi = {1: self.dui[1], 2: self.dui[2], 3: self.dui[3]}
        elif self.baguaming[xgs] == "离":
            self.nazhi = {1: self.li[1], 2: self.li[2], 3: self.li[3]}
        elif self.baguaming[xgs] == "巽":
            self.nazhi = {1: self.xun[1], 2: self.xun[2], 3: self.xun[3]}
        elif self.baguaming[xgs] == "坎":
            self.nazhi = {1: self.kan[1], 2: self.kan[2], 3: self.kan[3]}
        elif self.baguaming[xgs] == "艮":
            self.nazhi = {1: self.gen[1], 2: self.gen[2], 3: self.gen[3]}
        elif self.baguaming[xgs] == "坤":
            self.nazhi = {1: self.kun[1], 2: self.kun[2], 3: self.kun[3]}

        if self.baguaming[sgs] == "乾" or self.baguaming[sgs] == "震":
            self.nazhi.update({4: self.qian[4], 5: self.qian[5], 6: self.qian[6]})
        elif self.baguaming[sgs] == "兑":
            self.nazhi.update({4: self.dui[4], 5: self.dui[5], 6: self.dui[6]})
        elif self.baguaming[sgs] == "离":
            self.nazhi.update({4: self.li[4], 5: self.li[5], 6: self.li[6]})
        elif self.baguaming[sgs] == "巽":
            self.nazhi.update({4: self.xun[4], 5: self.xun[5], 6: self.xun[6]})
        elif self.baguaming[sgs] == "坎":
            self.nazhi.update({4: self.kan[4], 5: self.kan[5], 6: self.kan[6]})
        elif self.baguaming[sgs] == "艮":
            self.nazhi.update({4: self.gen[4], 5: self.gen[5], 6: self.gen[6]})
        elif self.baguaming[sgs] == "坤":
            self.nazhi.update({4: self.kun[4], 5: self.kun[5], 6: self.kun[6]})
        return self.nazhi

    # 卦纳支 对应的五行

    def guawuxing(self, xgs, sgs):
        self.gwx = {}
        for i in range(1, 7, 1):
            self.gwx.update({i: self.DZ5x[self.guanazhi(xgs, sgs)[i]]})
        return self.gwx

    # 通过卦的纳支 和 卦宫算六亲

    def gualiuqin(self, guagong, xgs, sgs):
        self.glq = {}
        if guagong == "乾":
            for i in range(1, 7, 1):
                self.glq.update({i: self.qian6qin[self.guawuxing(xgs, sgs)[i]]})
            return self.glq
        elif guagong == "兑":
            for i in range(1, 7, 1):
                self.glq.update({i: self.dui6qin[self.guawuxing(xgs, sgs)[i]]})
            return self.glq
        elif guagong == "离":
            for i in range(1, 7, 1):
                self.glq.update({i: self.li6qin[self.guawuxing(xgs, sgs)[i]]})
            return self.glq
        elif guagong == "震":
            for i in range(1, 7, 1):
                self.glq.update({i: self.zhen6qin[self.guawuxing(xgs, sgs)[i]]})
            return self.glq
        elif guagong == "巽":
            for i in range(1, 7, 1):
                self.glq.update({i: self.xun6qin[self.guawuxing(xgs, sgs)[i]]})
            return self.glq
        elif guagong == "坎":
            for i in range(1, 7, 1):
                self.glq.update({i: self.kan6qin[self.guawuxing(xgs, sgs)[i]]})
            return self.glq
        elif guagong == "艮":
            for i in range(1, 7, 1):
                self.glq.update({i: self.gen6qin[self.guawuxing(xgs, sgs)[i]]})
            return self.glq
        elif guagong == "坤":
            for i in range(1, 7, 1):
                self.glq.update({i: self.kun6qin[self.guawuxing(xgs, sgs)[i]]})
            return self.glq
        else:
            return None



    # 卦世应
    def guashiying(self, gs):
        if gs in [0, 9, 18, 27, 36, 45, 54, 63]:
            return {1: 2*"　", 2: 2*"　", 3: "　应", 4: 2*"　", 5: 2*"　", 6: "　世"}
        if gs in [32, 41, 50, 59, 4, 13, 22, 31]:
            return {1: "　世", 2: 2*"　", 3: 2*"　", 4: "　应", 5: 2*"　", 6: 2*"　"}
        if gs in [48, 57, 34, 43, 20, 29, 6, 15]:
            return {1: 2*"　", 2: "　世", 3: 2*"　", 4: 2*"　", 5: "　应", 6: 2*"　"}
        if gs in [56, 49, 42, 35, 28, 21, 14, 7, 2, 11, 16, 25, 38, 47, 52, 61]:
            return {1: 2*"　", 2: 2*"　", 3: "　世", 4: 2*"　", 5: 2*"　", 6: "　应"}
        if gs in [60, 53, 46, 39, 24, 17, 10, 3, 58, 51, 40, 33, 30, 23, 12, 5]:
            return {1: "　应", 2: 2*"　", 3: 2*"　", 4: "　世", 5: 2*"　", 6: 2*"　"}
        if gs in [62, 55, 44, 37, 26, 19, 8, 1]:
            return {1: 2*"　", 2: "　应", 3: 2*"　", 4: 2*"　", 5: "　世", 6: 2*"　"}

    # 卦阴阳符号
    def guafu(self):
        self.yingyangfu = {}
        for i in range(1, 7):
            if self.liuyao[i - 1] == "1":
                self.yingyangfu.update({i: "■■　　■■"})
            elif self.liuyao[i - 1] == "0":
                self.yingyangfu.update({i: "■■■■■■"})

        if int(self.dong, 2) == 0:
            for i in range(7, 13):
                self.yingyangfu.update({i: ""})
        elif int(self.dong, 2) != 0:
            for i in range(7, 13):
                if self.bian6()[i-7] == "1":
                    self.yingyangfu.update({i: "■■　　■■"})
                elif self.bian6()[i-7] == "0":
                    self.yingyangfu.update({i: "■■■■■■"})

        return self.yingyangfu

    # 动爻位置
    def dywz(self):
        self.dyfh = {1: 4*"　", 2: 4*"　", 3: 4*"　", 4: 4*"　", 5: 4*"　", 6: 4*"　"}
        if int(self.dong, 2) != 0:
            for i in range(1, 7, 1):
                if self.dong[i-1] == "1":
                    if self.liuyao[i-1] == "1":
                        self.dyfh[i] = "　×→　"
                    elif self.liuyao[i-1] == "0":
                        self.dyfh[i] = "　○→　"
                elif self.dong[i-1] == "0":
                    self.dyfh[i] = 4 * "　"
            return self.dyfh
        elif int(self.dong, 2) == 0:
            self.dyfh = {1: "", 2: "", 3: "", 4: "", 5: "", 6: ""}
            return self.dyfh


    #主卦
    def zhugua(self):
        self.zg = {1: "", 2: "", 3: "", 4: "", 5: "", 6: ""}
        for i in  range(1, 7, 1):
            self.zg[i] = self.gualiuqin(self.guagong(self.guashu(self.liuyao)), self.xiaguashu(self.liuyao), + \
                self.shangguashu(self.liuyao))[i] + self.guanazhi(self.xiaguashu(self.liuyao), + \
                self.shangguashu(self.liuyao))[i] + self.guawuxing(self.xiaguashu(self.liuyao), + \
                self.shangguashu(self.liuyao))[i]
        return self.zg

    # 变卦
    def biangua(self):
        self.bg = {1: "", 2: "", 3: "", 4: "", 5: "", 6: ""}
        if int(self.dong, 2) == 0:
            return self.bg
        elif int(self.dong, 2) != 0:
            for i in range(1, 7, 1):
                self.bg[i] = self.gualiuqin(self.guagong(self.guashu(self.liuyao)), self.xiaguashu(self.bian6()),
                                            self.shangguashu(self.bian6()))[i] + \
                             self.guanazhi(self.xiaguashu(self.bian6()), self.shangguashu(self.bian6()))[i] + \
                             self.guawuxing(self.xiaguashu(self.bian6()), self.shangguashu(self.bian6()))[i]
            return self.bg

    # 藏卦
    def canggua(self):
        self.cg = {}
        self.cgg = {1: 4*"　", 2: 4*"　", 3: 4*"　", 4: 4*"　", 5: 4*"　", 6: 4*"　"}
        self.cf = self.cangyaofu(self.guashu(self.liuyao))

        self.z1 = self.guanazhi(self.xiaguashu(self.liuyao), self.shangguashu(self.liuyao))[1]
        self.z4 = self.guanazhi(self.xiaguashu(self.liuyao), self.shangguashu(self.liuyao))[4]
        self.c1 = self.guanazhi(self.xiaguashu(self.cf), self.shangguashu(self.cf))[1]
        self.c4 = self.guanazhi(self.xiaguashu(self.cf), self.shangguashu(self.cf))[4]

        for i in range(1, 7, 1):
            self.cg[i] = self.gualiuqin(self.guagong(self.guashu(self.liuyao)), self.xiaguashu(self.cf),
                                            self.shangguashu(self.cf))[i] + \
                             self.guanazhi(self.xiaguashu(self.cf), self.shangguashu(self.cf))[i] + \
                             self.guawuxing(self.xiaguashu(self.cf), self.shangguashu(self.cf))[i]

        if self.z1 == self.c1 and self.z4 == self.c4:
            return self.cgg
        elif self.z1 == self.c1 and self.z4 != self.c4:
            for i in range(4, 7, 1):
                self.cgg[i] = self.cg[i]
            return self.cgg
        elif self.z1 != self.c1 and self.z4 == self.c4:
            for i in range(1, 4, 1):
                self.cgg[i] = self.cg[i]
            return self.cgg
        elif self.z1 != self.c1 and self.z4 != self.c4:
            return self.cg


# 以下是主程序

if __name__ == '__main__':
    baa = bagua(liuyao="000000", dong="100001")

    print("藏卦", baa.canggua())
    print("卦符",baa.guafu())
    print("主卦", baa.zhugua())
    print("动爻位置", baa.dywz())
    print("变卦", baa.biangua())



