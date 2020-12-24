import serial
import upper_computer as uc
import time

ser=serial.Serial()
record_flag=0



def open_com(com_num,baud_rate,return_window):
    global ser
    ser = serial.Serial(com_num, baud_rate, timeout = 2)  # windows系统连接串行口
    if ser.is_open:
        return_window.insert('insert', '串口已打开' + '\r\n')
    else:
        return_window.insert('insert', '打开失败' + '\r\n')

def close_com():
    global ser
    ser.close()

def go_forward(left_speed,right_speed):#前进
    global ser
    hex_ls = str(hex(int(left_speed)))[2:]
    if len(hex_ls) < 2:
        hex_ls = '0' + hex_ls
    hex_rs = str(hex(int(right_speed)))[2:]
    if len(hex_rs) < 2:
        hex_rs = '0' + hex_rs
    order = bytes.fromhex('55 D1 '+hex_ls+' '+hex_rs+' 00 00 FF')
    ser.write(order)

def go_backward(left_speed,right_speed):#后退
    global ser
    hex_ls = str(hex(int(left_speed)))[2:]
    if len(hex_ls) < 2:
        hex_ls = '0' + hex_ls
    hex_rs = str(hex(int(right_speed)))[2:]
    if len(hex_rs) < 2:
        hex_rs = '0' + hex_rs
    order = bytes.fromhex('55 D2 ' + hex_ls + ' ' + hex_rs + ' 00 00 FF')
    ser.write(order)

def car_break(event=None):#停车
    global ser
    order = bytes.fromhex('55 D3 00 00 00 00 FF')
    ser.write(order)
    global record_flag
    if record_flag:
        order=bytes.fromhex('55 DF 00 00 00 00 FF')
        time.sleep(1)
        ser.write(order)
        time.sleep(1)


def turn_left(speed):#左转
    global ser
    hex_speed = str(hex(int(speed)))[2:]
    if len(hex_speed) < 2:
        hex_speed = '0' + hex_speed
    order = bytes.fromhex('55 D4 '+hex_speed+' 00 00 00 FF')
    ser.write(order)

def turn_right(speed):#右转
    global ser
    hex_speed = str(hex(int(speed)))[2:]
    if len(hex_speed) < 2:
        hex_speed = '0' + hex_speed
    order = bytes.fromhex('55 D5 '+hex_speed+' 00 00 00 FF')
    ser.write(order)

def hold_tight(_tight_angle):#夹紧
    global ser
    tight_angle = str(hex(int(_tight_angle)))[2:]
    if len(tight_angle) < 2:
        tight_angle = '0' + tight_angle
    order = bytes.fromhex('55 D6 '+tight_angle+' 00 00 00 FF')
    ser.write(order)

def hold_loose():#张开
    global ser
    order = bytes.fromhex('55 D7 5A 00 00 00 FF')
    ser.write(order)

def hold_up():#抬起
    global ser
    order = bytes.fromhex('55 D8 00 00 00 00 FF')
    ser.write(order)

def hold_down():#放下
    global ser
    order = bytes.fromhex('55 D9 5A 00 00 00 FF')
    ser.write(order)

def camera_turn(angle):
    global ser
    hex_angle=str(hex(int(angle)))[2:]
    if len(hex_angle)<2:
        hex_angle='0'+hex_angle
    order = bytes.fromhex('55 DA '+hex_angle+' 00 00 00 FF')
    ser.write(order)

def start_tracking():#开始循迹
    global ser
    order = bytes.fromhex('55 DC 01 00 00 00 FF')
    ser.write(order)

def stop_tracking():#停止循迹
    global ser
    order = bytes.fromhex('55 DC 00 00 00 00 FF')
    ser.write(order)
    time.sleep(0.1)
    order = bytes.fromhex('55 D3 00 00 00 00 FF')
    ser.write(order)

def change_tracking_setting(_kp,_speed,_time):#更改循迹部分的参数设置
    global ser
    kp = str(hex(int(_kp)))[2:]
    if len(kp) < 2:
        kp = '0' + kp
    speed = str(hex(int(_speed)))[2:]
    if len(speed) < 2:
        speed = '0' + speed
    exposure_time = str(hex(int(_time)))[2:]
    if len(exposure_time) < 2:
        exposure_time = '0' + exposure_time
    order = bytes.fromhex('55 DB ' + kp+' '+speed+' '+exposure_time + ' 00 FF')
    ser.write(order)

def start_record():#开始记录
    global ser
    order = bytes.fromhex('55 DD B1 00 00 00 FF')
    ser.write(order)
    global record_flag
    record_flag = 1
    order = bytes.fromhex('55 E0 00 00 00 00 FF')
    time.sleep(1.5)
    ser.write(order)
    time.sleep(1.5)


def start_repeat():#开始复现
    global ser
    order = bytes.fromhex('55 DD A1 00 00 00 FF')
    ser.write(order)
    global record_flag
    record_flag = 0


def stop_obstacle():#停止记录或复现
    global ser
    order = bytes.fromhex('55 DD C1 00 00 00 FF')
    ser.write(order)
    global record_flag
    record_flag = 0
    time.sleep(1.5)

def change_obstacle_setting(_krp,_krd,_revolve_speed,_kwp,_kwd,_ward_speed):#更改避障部分的参数设置
    global ser
    krp = str(hex(int(_krp)))[2:]
    if len(krp) < 2:
        krp = '0' + krp
    krd = str(hex(int(_krd)))[2:]
    if len(krd) < 2:
        krd = '0' + krd
    revolve_speed = str(hex(int(_revolve_speed)))[2:]
    if len(revolve_speed) < 2:
        revolve_speed = '0' + revolve_speed
    kwp = str(hex(int(_kwp)))[2:]
    if len(kwp) < 2:
        kwp = '0' + kwp
    kwd = str(hex(int(_kwd)))[2:]
    if len(kwd) < 2:
        kwd = '0' + kwd
    ward_speed = str(hex(int(_ward_speed)))[2:]
    if len(ward_speed) < 2:
        ward_speed = '0' + ward_speed
    order = bytes.fromhex('55 DE ' + krp+' '+krd+' '+revolve_speed+' 00 FF')
    ser.write(order)
    time.sleep(1)
    order = bytes.fromhex('55 D0 ' + kwp + ' ' + kwd + ' ' + ward_speed + ' 00 FF')
    ser.write(order)

def send_out(entry_order):#发送
    global ser
    order = bytes.fromhex(entry_order)
    ser.write(order)
