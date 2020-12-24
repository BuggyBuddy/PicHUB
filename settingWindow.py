# coding=utf-8
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import shutil

class Settings(QWidget):
    def __init__(self):
        super(Settings, self).__init__()
        self.resize(600, 750)
        self.setWindowTitle("设置")
        self.roll_area=QScrollArea(self)
        self.roll_area.resize(600,750)
        self.setting_title=QLabel('设置',self)
        self.setting_title.setFont(QFont("Microsoft YaHei",20))
        self.play_title=QLabel('播放设置',self)
        self.play_title.setFont(QFont("Microsoft YaHei",16))
        self.mode_title=QLabel('播放模式',self)
        self.mode_title.setFont(QFont("Microsoft YaHei",12))
        self.single_button = QRadioButton('单个播放', self)
        self.single_button.setFont(QFont("Microsoft YaHei",12))
        self.loop_button = QRadioButton('循环播放', self)
        self.loop_button.setFont(QFont("Microsoft YaHei",12))
        self.time_title=QLabel('时间间隔',self)
        self.time_title.setFont(QFont("Microsoft YaHei",12))
        self.time_edit = QComboBox(self)
        self.time_edit.addItems(['30s','5min','15min','30min','1h'])
        self.mem_title=QLabel('存储设置',self)
        self.mem_title.setFont(QFont("Microsoft YaHei",16))
        self.addr_title=QLabel('存储地址',self)
        self.addr_title.setFont(QFont("Microsoft YaHei",12))
        self.addr_edit = QLabel('',self)
        self.addr_edit.resize(240,28)
        self.addr_button = QPushButton('浏览…',self)
        self.cache_title = QLabel('当前系统缓存：',self)
        self.cache_title.setFont(QFont("Microsoft YaHei",12))
        self.cache_label = QLabel('5GB',self)
        self.cache_label.setFont(QFont("Microsoft YaHei",12))
        self.cache_button = QPushButton('清除缓存',self)
        self.exit_button = QPushButton('保存并退出此对话框',self)
        self.dairy_title=QLabel('更新日志',self)
        self.dairy_title.setFont(QFont("Microsoft YaHei",20))
        self.dairy='''
    你知道吗，长颈鹿喝咖啡的时候，在嘴边是热的，咖啡还没到肚子里就凉了。你不知道,你只在乎你自己。
    你知道吗，乌拉圭的人口有345.7万，同时仅澳大利亚就有4700万袋鼠，如果袋鼠决定入侵乌拉圭，那么每一个乌拉圭人都要打14只袋鼠。你不知道，你不在乎，你只关心你自己。
    你说得对，但是梵蒂冈人口只有801人，同时仅女权吧就有17.8万只极端女拳带师。如果拳师决定入侵梵蒂冈，每个梵蒂冈人要打222只拳师，你不知道，你不在乎，你只关心乌拉圭。
    你说得对，但是北苏丹人口只有2人，同时仅澳大利亚就有4700万只袋鼠。如果袋鼠决定入侵北苏丹，北苏丹去梵蒂冈请外援，梵蒂冈去乌拉圭请外援，每名士兵依然得面对14只袋鼠，即使艰难取胜，北苏丹与梵蒂冈都可能灭亡。你不知道，你不在乎，你只关心梵蒂冈。
    你说得对。如果肖战粉丝入侵香港，那么每个香港人就需要应对近3个肖战粉丝；如果澳大利亚的袋鼠决定入侵中国，那么每一个中国人都要吃3.3%只袋鼠；如果拳师决定入侵梵蒂冈，每个梵蒂冈人要打222只拳师；如果袋鼠决定入侵乌拉圭，那么每一个乌拉圭人都要打14只袋鼠。而我，只有一个人。在这里看你们的回答，差点被笑死。本想着要努力纠正作息，早睡早起，却还是熬到现在，头发也没有几根了，眼角还长出了皱纹。我的作业尚未写完，明天一早还有课。未来的工作还没有着落。年纪也慢慢变大了，容颜逐渐逝去，钱包却没有变鼓。奋斗的步伐根本赶不上家人老去的速度。你关心乌拉圭人、梵蒂冈人、香港人，还有自己要吃多少只袋鼠，却不知道我有多么苦恼。你什么都不知道，你只关心你自己。
    你说得对，但是圣马力诺共和国不仅人口少他们甚至连领袖都没有，同时仅澳大利亚就有4700万只袋鼠。如果袋鼠决定入侵北苏丹，北苏丹去梵蒂冈请外援，梵蒂冈去乌拉圭请外援，乌拉圭去圣马力诺共和国请外援，每名士兵依然得面对14只袋鼠，即使艰难取胜，北苏丹与梵蒂冈与圣马力诺共和国都可能灭亡。你不知道，你不在乎，你只关心你的乌拉圭。
    你说的对，但中国的人口有14亿，同时仅澳大利亚就有4700万只袋鼠，如果袋鼠决定入侵中国，那么每一个中国人都要吃3.3%只袋鼠。你不知道，你不在乎，你只关心圣马力诺共和国。
    你说得对，但是香港只有700万人，肖战却有2000万粉丝，如果肖战粉丝入侵香港，那个一个香港人就需要应对近3个肖战粉丝，你不知道你不在乎，你只在乎你要吃多少袋鼠。
    你说得对，但是梵蒂冈的人口只有801人，同时，仅拥核国家就有1.9万枚核弹。如果拥核国家决定核击梵蒂冈，那么每一个梵蒂冈人要扛23枚核弹，你不知道，你不在乎，你只知道乌拉圭！
    '''       
        self.dairy_label=QLabel(self.dairy,self)
        self.dairy_label.setFixedWidth(550)
        self.dairy_label.setFont(QFont("Microsoft YaHei",12))
        self.dairy_label.setWordWrap(True)
        self.makelayout()
        self.roll_area.setWidget(self.roll_group)
        self.logic_init()
        

    def makelayout(self):
        self.roll_area.move(0,0)
        self.roll_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.cache_layout = QHBoxLayout()
        self.time_layout = QHBoxLayout()
        self.addr_layout = QGridLayout()
        self.roll_layout.addWidget(self.setting_title)
        self.roll_layout.addWidget(self.play_title)
        self.button_layout.addWidget(self.mode_title)
        self.button_layout.addWidget(self.single_button)
        self.button_layout.addWidget(self.loop_button)
        self.roll_layout.addLayout(self.button_layout)
        self.time_layout.addWidget(self.time_title)
        self.time_layout.addWidget(self.time_edit)
        self.roll_layout.addLayout(self.time_layout)
        self.roll_layout.addWidget(self.mem_title)
        self.addr_layout.addWidget(self.addr_title,0,0,1,1)
        self.addr_layout.addWidget(self.addr_edit,0,1,2,1)
        self.addr_edit.resize(240,28)
        self.addr_layout.addWidget(self.addr_button,0,3,1,1)
        self.roll_layout.addLayout(self.addr_layout)
        self.cache_layout.addWidget(self.cache_title)
        self.cache_layout.addWidget(self.cache_label)
        self.cache_layout.addWidget(self.cache_button)
        self.roll_layout.addLayout(self.cache_layout)
        self.roll_layout.addWidget(self.exit_button)
        self.roll_layout.addWidget(self.dairy_title)
        self.roll_layout.addWidget(self.dairy_label)
        self.roll_group = QGroupBox()
        self.roll_group.setLayout(self.roll_layout)


    def logic_init(self):
        self.single_button.toggled.connect(self.single_func)
        self.loop_button.toggled.connect(self.loop_func)
        self.addr_button.clicked.connect(self.brouse_addr)
        self.exit_button.clicked.connect(self.save_and_quit)
        self.time_edit.currentIndexChanged.connect(self.reset_time)
        self.cache_button.clicked.connect(self.clear_cache)


    def single_func(self):
        return


    def loop_func(self):
        return

    def brouse_addr(self):
        pathname = QFileDialog.getExistingDirectory(self)
        self.addr_edit.setText(pathname)
        print(self.addr_edit.text())
        return

    def save_and_quit(self):
        QMessageBox.about(self, '提示', '更改成功！')
        self.close()

    def reset_time(self):
        newtime = self.time_edit.currentText()
        print(newtime)

    def clear_cache(self):
        QMessageBox.about(self,'提示','缓存已清除！')

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = Settings()
    my.show()
    sys.exit(app.exec_())