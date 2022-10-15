# def _init():  # 初始化
#     global gv
#     gv = {}
class GlobalVar:
    gv={}

def set_value(key, value):
    # 定义一个全局变量
    GlobalVar.gv[key] = value


def get_value(key):
    # 获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return int(GlobalVar.gv[key])
    except:
        print('读取' + key + '失败\r\n')

def printDay(key):
    print("remainDay in variable.py:",GlobalVar.gv[key])
