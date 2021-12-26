# liuyaopaipan tool
import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QDialog

import GUI
import bagua
import dialog
import shensha
import sizhu


class paipan(QWidget, GUI.Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        GUI.Ui_Form.__init__(self)
        self.setupUi(self)
        self.yaof = ["0", "0", "0", "0", "0", "0"]
        self.dy = ["0", "0", "0", "0", "0", "0"]
        self.pushButton.clicked.connect(self.yaofb)
        self.pushButton_2.clicked.connect(self.yaofb_2)
        self.pushButton_3.clicked.connect(self.yaofb_3)
        self.pushButton_4.clicked.connect(self.yaofb_4)
        self.pushButton_5.clicked.connect(self.yaofb_5)
        self.pushButton_6.clicked.connect(self.yaofb_6)
        self.pushButton_7.clicked.connect(self.paigua)
        self.pushButton_8.clicked.connect(self.qinkong)
        self.pushButton_9.clicked.connect(self.copyall)
        self.pushButton_10.clicked.connect(self.about)

        self.comboBox.activated.connect(self.biangz)
        self.comboBox_2.activated.connect(self.biangz)
        self.comboBox_3.activated.connect(self.biangz)
        self.comboBox_4.activated.connect(self.biangz)
        self.comboBox_5.activated.connect(self.biangz)

        self.comboBox_7.activated.connect(self.cb7)
        self.comboBox_8.activated.connect(self.cb8)

        self.comboBox.setCurrentIndex(time.localtime()[0] - 1980)
        self.comboBox_2.setCurrentIndex(time.localtime()[1] - 1)
        self.comboBox_3.setCurrentIndex(time.localtime()[2] - 1)
        self.comboBox_4.setCurrentIndex(time.localtime()[3])
        self.comboBox_5.setCurrentIndex(time.localtime()[4])

        self.SZ = sizhu.sizhu(time.localtime()[0], time.localtime()[1], time.localtime()[2], time.localtime()[3],
                              time.localtime()[4])
        self.comboBox_6.setCurrentText(self.SZ.yue()[1])
        self.comboBox_7.setCurrentText(self.SZ.ri()[0])
        self.comboBox_8.setCurrentText(self.SZ.ri()[1])

    def about(self):
        self.dia = Dia()
        self.dia.show()

    def copyall(self):
        self.plainTextEdit.selectAll()
        self.plainTextEdit.copy()

    def cb7(self):
        if self.comboBox_7.currentText() in ["甲", "丙", "戊", "庚", "壬"] and self.comboBox_8.currentText() not in ["子",
                                                                                                                "寅",
                                                                                                                "辰",
                                                                                                                "午",
                                                                                                                "申",
                                                                                                                "戌"]:
            self.comboBox_8.setCurrentText("子")
        elif self.comboBox_7.currentText() in ["乙", "丁", "己", "辛", "癸"] and self.comboBox_8.currentText() not in ["丑",
                                                                                                                  "卯",
                                                                                                                  "巳",
                                                                                                                  "未",
                                                                                                                  "酉",
                                                                                                                  "亥"]:
            self.comboBox_8.setCurrentText("丑")

    def cb8(self):
        if self.comboBox_8.currentText() in ["子", "寅", "辰", "午", "申", "戌"] and self.comboBox_7.currentText() not in [
            "甲", "丙", "戊", "庚", "壬"]:
            self.comboBox_7.setCurrentText("甲")
        elif self.comboBox_8.currentText() in ["丑", "卯", "巳", "未", "酉", "亥"] and self.comboBox_7.currentText() not in [
            "乙", "丁", "己", "辛", "癸"]:
            self.comboBox_7.setCurrentText("乙")

    def qinkong(self):
        self.plainTextEdit.clear()
        self.lineEdit.clear()
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.pushButton.setText("■■■■■■")
        self.pushButton_2.setText("■■■■■■")
        self.pushButton_3.setText("■■■■■■")
        self.pushButton_4.setText("■■■■■■")
        self.pushButton_5.setText("■■■■■■")
        self.pushButton_6.setText("■■■■■■")
        self.yaof = ["0", "0", "0", "0", "0", "0"]
        self.dy = ["0", "0", "0", "0", "0", "0"]
        self.comboBox.setCurrentIndex(time.localtime()[0] - 1980)
        self.comboBox_2.setCurrentIndex(time.localtime()[1] - 1)
        self.comboBox_3.setCurrentIndex(time.localtime()[2] - 1)
        self.comboBox_4.setCurrentIndex(time.localtime()[3])
        self.comboBox_5.setCurrentIndex(time.localtime()[4])

        self.comboBox_6.setCurrentText(self.SZ.yue()[1])
        self.comboBox_7.setCurrentText(self.SZ.ri()[0])
        self.comboBox_8.setCurrentText(self.SZ.ri()[1])

    def biangz(self):
        self.SZ2 = sizhu.sizhu(self.comboBox.currentText(), self.comboBox_2.currentText(),
                               self.comboBox_3.currentText(), self.comboBox_4.currentText(),
                               self.comboBox_5.currentText())
        self.comboBox_6.setCurrentText(self.SZ2.yue()[1])
        self.comboBox_7.setCurrentText(self.SZ2.ri()[0])
        self.comboBox_8.setCurrentText(self.SZ2.ri()[1])

    def yaofb(self):
        if self.pushButton.text() == "■■■■■■":
            self.pushButton.setText("■■　　■■")
            self.yaof[0] = "1"
        else:
            self.pushButton.setText("■■■■■■")
            self.yaof[0] = "0"

    def yaofb_2(self):
        if self.pushButton_2.text() == "■■■■■■":
            self.pushButton_2.setText("■■　　■■")
            self.yaof[1] = "1"
        else:
            self.pushButton_2.setText("■■■■■■")
            self.yaof[1] = "0"

    def yaofb_3(self):
        if self.pushButton_3.text() == "■■■■■■":
            self.pushButton_3.setText("■■　　■■")
            self.yaof[2] = "1"
        else:
            self.pushButton_3.setText("■■■■■■")
            self.yaof[2] = "0"

    def yaofb_4(self):
        if self.pushButton_4.text() == "■■■■■■":
            self.pushButton_4.setText("■■　　■■")
            self.yaof[3] = "1"
        else:
            self.pushButton_4.setText("■■■■■■")
            self.yaof[3] = "0"

    def yaofb_5(self):
        if self.pushButton_5.text() == "■■■■■■":
            self.pushButton_5.setText("■■　　■■")
            self.yaof[4] = "1"
        else:
            self.pushButton_5.setText("■■■■■■")
            self.yaof[4] = "0"

    def yaofb_6(self):
        if self.pushButton_6.text() == "■■■■■■":
            self.pushButton_6.setText("■■　　■■")
            self.yaof[5] = "1"
        else:
            self.pushButton_6.setText("■■■■■■")
            self.yaof[5] = "0"

    def paigua(self):
        # 六个爻的符号
        self.liuy = ""
        self.liuy = self.liuy.join(self.yaof)

        # 动爻符号选择
        self.dy = ["0", "0", "0", "0", "0", "0"]
        if self.checkBox_1.isChecked():
            self.dy[0] = "1"
        if self.checkBox_2.isChecked():
            self.dy[1] = "1"
        if self.checkBox_3.isChecked():
            self.dy[2] = "1"
        if self.checkBox_4.isChecked():
            self.dy[3] = "1"
        if self.checkBox_5.isChecked():
            self.dy[4] = "1"
        if self.checkBox_6.isChecked():
            self.dy[5] = "1"
        self.dd = ""
        self.dd = self.dd.join(self.dy)

        # 实例化排盘
        GG = bagua.bagua(self.liuy, self.dd)
        SS = shensha.shensha(self.comboBox_6.currentText(), self.comboBox_7.currentText(),
                             self.comboBox_8.currentText())
        self.SZ2 = sizhu.sizhu(self.comboBox.currentText(), self.comboBox_2.currentText(),
                               self.comboBox_3.currentText(), self.comboBox_4.currentText(),
                               self.comboBox_5.currentText())
        self.plainTextEdit.clear()
        if self.SZ2.yue()[1] == self.comboBox_6.currentText() and self.SZ2.ri()[0] == self.comboBox_7.currentText() and \
                self.SZ2.ri()[1] == self.comboBox_8.currentText():
            self.paiguashijian = self.comboBox.currentText() + "年" + self.comboBox_2.currentText() + "月" + self.comboBox_3.currentText() + \
                                 "日" + self.comboBox_4.currentText() + "点" + self.comboBox_5.currentText() + "分" + "　" + self.SZ2.xinqi() + "\n" + "干支：" + \
                                 self.SZ2.nian()[0] + self.SZ2.nian()[1] + "年　" + \
                                 self.SZ2.yue()[0] + self.SZ2.yue()[1] + "月　" + self.SZ2.ri()[0] + self.SZ2.ri()[
                                     1] + "日　" + self.SZ2.shi()[0] + self.SZ2.shi()[1] + "时"
        else:
            self.paiguashijian = self.comboBox_6.currentText() + "月" + "　　" + self.comboBox_7.currentText() + self.comboBox_8.currentText() + "日"

        self.plainTextEdit.appendPlainText("占事：" + self.lineEdit.text())
        self.plainTextEdit.appendPlainText("时间：" + self.paiguashijian)
        self.plainTextEdit.appendPlainText(
            "神煞：" + "华盖-" + SS.huagai() + "　将星-" + SS.jiangxing() + "　劫煞-" + SS.jiesha() + "　天医-" + SS.tianyi() + "　天禧-" + SS.tianxi() + "　桃花-" + SS.taohua() + "　谋星-" + SS.mouxing())
        self.plainTextEdit.appendPlainText(
            3 * "　" + "禄神-" + SS.lvshen() + "　羊刃-" + SS.yangren() + "　文昌-" + SS.wenchang() + "　马星-" + SS.maxing() + "　灾煞-" + SS.zaisha() + "　贵人-" + SS.guiren())

        if int(self.dd, 2) == 0:
            self.plainTextEdit.appendPlainText(
                7 * "　" + self.comboBox_6.currentText() + "月" + 7 * "　" + self.comboBox_7.currentText() + self.comboBox_8.currentText() + "日" + SS.xunkong())
            self.plainTextEdit.appendPlainText(
                "六神" + 2 * "　" + "藏爻" + "　" + GG.guaming(GG.guashu(self.liuy)) + "　" + GG.guagong(
                    GG.guashu(self.liuy)) + "宫")
            for i in range(6, 0, -1):
                self.plainTextEdit.appendPlainText(
                    SS.liushen()[i] + "　" + GG.canggua()[i] + GG.guafu()[i] + GG.zhugua()[i] +
                    GG.guashiying(GG.guashu(self.liuy))[i] + GG.dywz()[i] + GG.biangua()[i] + GG.guafu()[i + 6])
            self.plainTextEdit.appendPlainText(7 * "　" + GG.gualei(GG.guashu(self.liuy)))
        elif int(self.dd, 2) != 0:
            self.plainTextEdit.appendPlainText(
                7 * "　" + self.comboBox_6.currentText() + "月" + 14 * "　" + self.comboBox_7.currentText() + self.comboBox_8.currentText() + "日" + SS.xunkong())
            self.plainTextEdit.appendPlainText(
                "六神" + 2 * "　" + "藏爻" + "　" + GG.guaming(GG.guashu(self.liuy)) + "　" + GG.guagong(
                    GG.guashu(self.liuy)) + "宫" + 10 * "　" + GG.guaming(GG.guashu(GG.bian6())) + "　" + GG.guagong(
                    GG.guashu(GG.bian6())) + "宫")
            for i in range(6, 0, -1):
                self.plainTextEdit.appendPlainText(
                    SS.liushen()[i] + "　" + GG.canggua()[i] + GG.guafu()[i] + GG.zhugua()[i] +
                    GG.guashiying(GG.guashu(self.liuy))[i] + GG.dywz()[i] + GG.biangua()[i] + GG.guafu()[i + 6])
            self.plainTextEdit.appendPlainText(
                7 * "　" + GG.gualei(GG.guashu(self.liuy)) + 13 * "　" + GG.gualei(GG.guashu(GG.bian6())))


class Dia(QDialog, dialog.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        dialog.Ui_Dialog.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gua = paipan()
    gua.show()
    sys.exit(app.exec_())
