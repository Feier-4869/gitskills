import time
from .atm import ATM


if __name__ == '__main__':
    ATM.welcome()
    while True:
        print(ATM.userDict)
        time.sleep(1)
        num = ATM.choice()
        if num == "1":
            print("登录")
            ATM.login()
        elif num == "2":
            print("开户")
            ATM.openUser()
        elif num == "3":
            print("查询")
            ATM.search()
        elif num == "4":
            print("取款")
            ATM.getmoney()
        elif num == "5":
            print("存款")
            ATM.setmoney()
        elif num == "6":
            print("解锁")
            ATM.unlockcard()
        elif num == "7":
            print("转账")
            ATM.tansmoney()
        elif num == "8":
            print("改密")
        elif num == "9":
            print("锁卡")
            ATM.lockcard()
        elif num == "0":
            print("退出")
            break
        else:
            print("输入有误请重新输入...")

