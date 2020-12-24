import tkinter
from tkinter import ttk
#import bluetooth as bt


class Start(object):
    def __init__(self,):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("智能车控制系统")
        self.root.geometry('960x540')
        self.root.maxsize(960, 540)
        self.root.minsize(960, 540)

        """以下为串口连接的选择按钮"""
        self.frame1 = tkinter.Frame(self.root, width=150, height=140, borderwidth=1, relief='sunken')
        self.com_num_label = tkinter.Label(self.frame1, text='串口号', font=('黑体', 12))
        self.com_num=tkinter.StringVar()
        self.combobox = ttk.Combobox(self.frame1, width=6,textvariable=self.com_num)
        self.combobox['values'] = ('COM3', 'COM4', 'COM5', 'COM6', 'COM7')
        self.combobox.current(4)
        self.com_baud_label = tkinter.Label(self.frame1, text='波特率', font=('黑体', 12))
        self.baud_rate = tkinter.StringVar()
        self.baud_rate.set('9600')
        self.baud_entry = tkinter.Entry(self.frame1, font=('黑体', 12),width=7,textvariable=self.baud_rate)
        #self.open_com_button = tkinter.Button(self.frame1, command=lambda: bt.open_com(self.com_num.get(),self.baud_rate.get(),self.return_text), text="打开串口", font=('黑体', 12), width=12,
        #                                       height=1)
        #self.close_com_button = tkinter.Button(self.frame1,font=('黑体', 12), width=12,
        #                                      height=1,command=bt.close_com, text="关闭串口")



        """以下为小车行进的控制按钮"""
        self.go_forward_button = tkinter.Button(self.root, text="前进", font=('黑体', 12), width=6,height=3)
        self.go_backward_button = tkinter.Button(self.root, text="后退", font=('黑体', 12), width=6,height=3)
        #self.car_break_button = tkinter.Button(self.root, command=bt.car_break, text="停车", font=('黑体', 12), width=6,
        #                                        height=3)
        self.turn_left_button = tkinter.Button(self.root, text="左转", font=('黑体', 12), width=6,height=3)
        self.turn_right_button = tkinter.Button(self.root, text="右转", font=('黑体', 12), width=6,height=3)
        self.left_speed_label=tkinter.Label(self.root, text = '左轮转速', font = ('黑体', 12))
        self.left_speed = tkinter.StringVar()
        self.left_speed.set('130')
        self.left_speed_entry = tkinter.Entry(self.root, font=('黑体', 12), width=8, textvariable=self.left_speed)
        self.right_speed_label = tkinter.Label(self.root, text='右轮转速', font=('黑体', 12))
        self.right_speed = tkinter.StringVar()
        self.right_speed.set('130')
        self.right_speed_entry = tkinter.Entry(self.root, font=('黑体', 12), width=8, textvariable=self.right_speed)
        self.speed_label = tkinter.Label(self.root, text='原地转速', font=('黑体', 12))
        self.speed = tkinter.StringVar()
        self.speed.set('140')
        self.speed_entry = tkinter.Entry(self.root, font=('黑体', 12), width=8, textvariable=self.speed)
        #self.go_forward_button.bind("<Button-1>", lambda event: bt.go_forward(self.left_speed.get(),self.right_speed.get()))
        #self.go_forward_button.bind("<ButtonRelease>", bt.car_break)
        #self.go_backward_button.bind("<Button-1>", lambda event: bt.go_backward(self.left_speed.get(),self.right_speed.get()))
        #self.go_backward_button.bind("<ButtonRelease>", bt.car_break)
        #self.turn_left_button.bind("<Button-1>",lambda event: bt.turn_left(self.speed.get()))
        #self.turn_left_button.bind("<ButtonRelease>", bt.car_break)
        #self.turn_right_button.bind("<Button-1>", lambda event: bt.turn_right(self.speed.get()))
        #self.turn_right_button.bind("<ButtonRelease>", bt.car_break)



        """以下为小车抓取货物的控制按钮"""
        self.tight_angle_label = tkinter.Label(self.root, text='夹紧力度', font=('黑体', 12))
        self.tight_angle = tkinter.StringVar()
        self.tight_angle.set('37')
        self.tight_angle_entry = tkinter.Entry(self.root, font=('黑体', 12), width=7, textvariable=self.tight_angle)
        #self.hold_tight = tkinter.Button(self.root, command=lambda:bt.hold_tight(self.tight_angle.get()), text="夹紧", font=('黑体', 12), width=6,
        #                                        height=3)
        #self.hold_loose = tkinter.Button(self.root, command=bt.hold_loose, text="张开", font=('黑体', 12), width=6,
        #                                 height=3)
        #self.hold_up = tkinter.Button(self.root, command=bt.hold_up, text="抬起", font=('黑体', 12), width=6,
        #                                 height=3)
        #self.hold_down = tkinter.Button(self.root, command=bt.hold_down, text="放下", font=('黑体', 12), width=6,
         #                             height=3)

        """以下为相机旋转的控制按钮"""
        self.camera_turn_label=tkinter.Label(self.root, text = '相机旋转', font = ('黑体', 12))
        self.angle = tkinter.StringVar()
        self.angle.set('179')
        self.angle_entry = tkinter.Entry(self.root, font=('黑体', 12), width=7, textvariable=self.angle)
        #self.camera_turn = tkinter.Button(self.root, command=lambda:bt.camera_turn(self.angle.get()), text="旋转", font=('黑体', 12), width=5,
        #                                height=1)


        """以下为串口通讯返回框"""
        self.return_text=tkinter.Text(self.root,width=68,height=16)
        """以下为串口通讯输入框"""
        self.order = tkinter.StringVar()
        self.order_text = tkinter.Entry(self.root, font=('黑体', 12), width=53,textvariable=self.order)
        #self.send_out_button=tkinter.Button(self.root,font=('黑体',12),text='发送',
        #                                    command=lambda: bt.send_out(self.order.get()),width=5,height=1)
        """以下为循迹模式控制窗口"""
        self.frame2 = tkinter.Frame(self.root, width=150, height=180, borderwidth=1, relief='sunken')
        #self.start_tracking_button = tkinter.Button(self.frame2,font=('黑体', 12), width=12,
        #                                      height=1,command=bt.start_tracking, text="开始循迹")
        #self.stop_tracking_button = tkinter.Button(self.frame2, font=('黑体', 12), width=12,
        #                                            height=1, command=bt.stop_tracking, text="停止循迹")
        self.tracking_Kp_label = tkinter.Label(self.frame2, text='比例系数', font=('黑体', 12))
        self.tracking_Kp = tkinter.StringVar()
        self.tracking_Kp.set('35')
        self.tracking_Kp_entry = tkinter.Entry(self.frame2, font=('黑体', 12), width=8, textvariable=self.tracking_Kp)
        self.backward_speed_label = tkinter.Label(self.frame2, text='行进速度', font=('黑体', 12))
        self.backward_speed = tkinter.StringVar()
        self.backward_speed.set('200')
        self.backward_speed_entry = tkinter.Entry(self.frame2, font=('黑体', 12), width=8, textvariable=self.backward_speed)
        self.exposure_time_label = tkinter.Label(self.frame2, text='曝光时间', font=('黑体', 12))
        self.exposure_time = tkinter.StringVar()
        self.exposure_time.set('30')
        self.exposure_time_entry = tkinter.Entry(self.frame2, font=('黑体', 12), width=8,textvariable=self.exposure_time)
        self.change_setting_button = tkinter.Button(self.frame2, font=('黑体', 12), width=8,height=1,text="更改配置",
        command=lambda: bt.change_tracking_setting(self.tracking_Kp.get(),self.backward_speed.get(),self.exposure_time.get()))

        """以下为小车避障的控制按钮"""
        self.frame3 = tkinter.Frame(self.root, width=300, height=200, borderwidth=1, relief='sunken')
        #self.start_record_button = tkinter.Button(self.frame3, font=('黑体', 12), width=6,
        #                                            height=3, command=bt.start_record, text="记录")
        #self.start_repeat_button = tkinter.Button(self.frame3, font=('黑体', 12), width=6,
        #                                          height=3, command=bt.start_repeat, text="复现")
        #self.stop_obstacle_button = tkinter.Button(self.frame3, font=('黑体', 12), width=6,
        #                                         height=3, command=bt.stop_obstacle, text="停止")
        self.Krp_label = tkinter.Label(self.frame3, text='旋转比例', font=('黑体', 12))
        self.Krp = tkinter.StringVar()
        self.Krp.set('10')
        self.Krp_entry = tkinter.Entry(self.frame3, font=('黑体', 12), width=8, textvariable=self.Krp)
        self.Krd_label = tkinter.Label(self.frame3, text='旋转差分', font=('黑体', 12))
        self.Krd = tkinter.StringVar()
        self.Krd.set('120')
        self.Krd_entry = tkinter.Entry(self.frame3, font=('黑体', 12), width=8, textvariable=self.Krd)
        self.revolve_speed_label = tkinter.Label(self.frame3, text='旋转速度', font=('黑体', 12))
        self.revolve_speed = tkinter.StringVar()
        self.revolve_speed.set('140')
        self.revolve_speed_entry = tkinter.Entry(self.frame3, font=('黑体', 12), width=8,
                                                  textvariable=self.revolve_speed)
        self.Kwp_label = tkinter.Label(self.frame3, text='行进比例', font=('黑体', 12))
        self.Kwp = tkinter.StringVar()
        self.Kwp.set('25')
        self.Kwp_entry = tkinter.Entry(self.frame3, font=('黑体', 12), width=8, textvariable=self.Kwp)
        self.Kwd_label = tkinter.Label(self.frame3, text='行进差分', font=('黑体', 12))
        self.Kwd = tkinter.StringVar()
        self.Kwd.set('25')
        self.Kwd_entry = tkinter.Entry(self.frame3, font=('黑体', 12), width=8, textvariable=self.Kwd)
        self.ward_speed_label = tkinter.Label(self.frame3, text='行进速度', font=('黑体', 12))
        self.ward_speed = tkinter.StringVar()
        self.ward_speed.set('130')
        self.ward_speed_entry = tkinter.Entry(self.frame3, font=('黑体', 12), width=8,
                                                 textvariable=self.ward_speed)
        #self.change_obstacle_button = tkinter.Button(self.frame3, font=('黑体', 12), width=8, height=1, text="更改配置",
        #                                            command=lambda: bt.change_obstacle_setting(self.Krp.get(),self.Krd.get(),self.revolve_speed.get(),self.Kwp.get(),self.Kwd.get(),self.ward_speed.get()))


    # 完成布局
    def gui_arrange(self):
        """完成布局"""
        """以下为串口连接的选择按钮布局"""
        self.frame1.place(relx=0.01,rely=0.01)
        self.com_num_label.place(relx=0.05,rely=0.03)
        self.combobox.place(relx=0.5, rely=0.03)
        self.com_baud_label.place(relx=0.05, rely=0.25)
        self.baud_entry.place(relx=0.5, rely=0.25)
        #self.open_com_button.place(relx=0.15,rely=0.5)
        #self.close_com_button.place(relx=0.15,rely=0.75)
        """以下为小车行进的控制按钮布局"""
        self.go_forward_button.place(relx=0.8, rely=0.05)
        self.go_backward_button.place(relx=0.8, rely=0.33)
        #self.car_break_button.place(relx=0.8, rely=0.19)
        self.turn_left_button.place(relx=0.72, rely=0.19)
        self.turn_right_button.place(relx=0.88, rely=0.19)
        self.left_speed_label.place(relx=0.72,rely=0.47)
        self.right_speed_label.place(relx=0.88, rely=0.47)
        self.left_speed_entry.place(relx=0.72, rely=0.52)
        self.right_speed_entry.place(relx=0.88, rely=0.52)
        self.speed_label.place(relx=0.72,rely=0.35)
        self.speed_entry.place(relx=0.72,rely=0.4)

        """以下为小车抓取货物的控制按钮布局"""
        self.tight_angle_label.place(relx=0.75, rely=0.88)
        self.tight_angle_entry.place(relx=0.83, rely=0.88)
        #self.hold_tight.place(relx=0.75,rely=0.6)
        #self.hold_loose.place(relx=0.85, rely=0.6)
        #self.hold_up.place(relx=0.75, rely=0.75)
        #self.hold_down.place(relx=0.85, rely=0.75)
        """以下为串口通讯输入框的布局"""
        self.return_text.place(relx=0.2,rely=0.01)
        """以下为串口通讯输入框的布局"""
        self.order_text.place(relx=0.2,rely=0.42)
        #self.send_out_button.place(relx=0.65,rely=0.42)
        """以下为相机旋转的控制按钮的布局"""
        self.camera_turn_label.place(relx=0.75,rely=0.94)
        self.angle_entry.place(relx=0.83, rely=0.94)
        #self.camera_turn.place(relx=0.9,rely=0.94)
        """以下为循迹模式控制窗口的布局"""
        self.frame2.place(relx=0.01, rely=0.28)
        #self.start_tracking_button.place(relx=0.15,rely=0.01)
        #self.stop_tracking_button.place(relx=0.15, rely=0.2)
        self.tracking_Kp_label.place(relx=0.01,rely=0.4)
        self.tracking_Kp_entry.place(relx=0.5, rely=0.4)
        self.backward_speed_label.place(relx=0.01, rely=0.53)
        self.backward_speed_entry.place(relx=0.5, rely=0.53)
        self.exposure_time_label.place(relx=0.01, rely=0.66)
        self.exposure_time_entry.place(relx=0.5, rely=0.66)
        self.change_setting_button.place(relx=0.25,rely=0.82)
        """以下为小车避障的控制按钮的布局"""
        self.frame3.place(relx=0.01, rely=0.62)
        #self.start_record_button.place(relx=0.1, rely=0.01)
        #self.start_repeat_button.place(relx=0.7, rely=0.01)
        #self.stop_obstacle_button.place(relx=0.4,rely=0.01)
        self.Krp_label.place(relx=0.01, rely=0.33)
        self.Krp_entry.place(relx=0.25, rely=0.33)
        self.Krd_label.place(relx=0.49, rely=0.33)
        self.Krd_entry.place(relx=0.72, rely=0.33)
        self.revolve_speed_label.place(relx=0.01, rely=0.45)
        self.revolve_speed_entry.place(relx=0.25, rely=0.45)
        self.Kwp_label.place(relx=0.01, rely=0.57)
        self.Kwp_entry.place(relx=0.25, rely=0.57)
        self.Kwd_label.place(relx=0.49, rely=0.57)
        self.Kwd_entry.place(relx=0.72, rely=0.57)
        self.ward_speed_label.place(relx=0.01, rely=0.69)
        self.ward_speed_entry.place(relx=0.25, rely=0.69)
        #self.change_obstacle_button.place(relx=0.4, rely=0.85)





def main():
    # 初始化对象
    clever_car = Start()
    # 进行布局
    clever_car.gui_arrange()
    # 主程序执行
    tkinter.mainloop()


if __name__ == '__main__':
    main()
