
import random

from at import Card





class ATM:
    #存储用户的字典
    userDict = {}
    # 存储登录状态
    islogin = None

    @staticmethod
    def welcome():
        print('''
    **********************
    *                    *
    *  welcome to bank   *
    *                    *
    **********************
        ''')

    @staticmethod
    def choice():
        print('''
    **********************
    *  1.登陆   2.开户    *
    *  3.查询   4.取款    *
    *  5.存款   0.退出    *
    *  7.转账   8.改密    *
    *  9.锁卡   6.解锁    *
    **********************
        ''')
        num = input("请输入您要选择的项目：")
        return num

    @classmethod
    def getCardNum(cls):
        while True:
            cardnum = ""
            for x in range(6):
                cardnum += str(random.randrange(10))
            if cardnum not in cls.userDict:
                return cardnum


    @classmethod
    def openUser(cls):
        idcard = input("请输入您的身份证号码：")
        name = input("请输入您的姓名：")
        phonenum = input("请输入您的电话号码：")
        psd = input("请设置您的密码：")
        psd2 = input("请重复确认您的密码：")
        if psd == psd2:
            money = int(input("请输入您的预存款："))
            if money>0:
                cardnum = cls.getCardNum()
                card = Card(cardnum,psd,money)
                user = User(idcard,name,phonenum,card)
                cls.userDict[cardnum] = user
                print("开户成功,您的卡号为%s，请牢记..."%cardnum)
            else:
                print("预存金额有误开户失败！！")
        else:
            print("两次密码输入不一致，开户失败")

    @classmethod
    def login(cls):
        cardnum = input("请输入您的卡号：")
        # 判断卡号是否存在
        if cardnum in cls.userDict:
            # 判断卡是否锁定
            if not cls.userDict.get(cardnum).card.islock:
                # 三次输入密码的机会
                for x in range(1,4):
                    psd = input("请输入您的密码：")
                    if psd == cls.userDict.get(cardnum).card.password:
                        print("恭喜你登录成功！！！")
                        cls.islogin = cardnum
                        break
                    else:
                        print("密码错误,您还剩余%d次机会"%(3-x))
                else:
                    #三次输入错误，将卡锁定
                    cls.userDict.get(cardnum).card.islock = True
                    print("三次密码输入错误，卡已锁定...")

            else:
                print("卡已锁定！！！")
        else:
            print("卡号不存在！！！")

    @classmethod
    def search(cls):
        if cls.islogin:
            print("您当前的余额为%d"%cls.userDict.get(cls.islogin).card.money)
        else:
            print("请登录后查询")

    @classmethod
    def getmoney(cls):
        if cls.islogin:
            mon = int(input("请输入取款金额："))
            user = cls.userDict.get(cls.islogin)
            if mon>0 and mon<=user.card.money:
                user.card.money -= mon
                print("取款成功！！")
            else:
                print("取款金额有误或者余额不足...")
        else:
            print("请登录后取款...")

    @classmethod
    def setmoney(cls):
        if cls.islogin:
            mon = int(input("请输入存款的金额："))
            if mon>0:
                cls.userDict.get(cls.islogin).card.money += mon
                print("存款成功！！！")
            else:
                print("存款金额有误")
        else:
            print("请登录后存款...")

    @classmethod
    def lockcard(cls):
        if cls.islogin:
            idcard = input("请输入您的身份证号码：")
            if cls.userDict.get(cls.islogin).idcard == idcard:
                cls.userDict.get(cls.islogin).card.islock = True
                print("卡已锁定...")
                # 清除登录状态
                cls.islogin = None
            else:
                print("身份有误，锁卡失败！！")
        else:
            print("请登录后锁卡...")

    @classmethod
    def unlockcard(cls):
        cardnum = input("请输入您的卡号：")
        if cardnum in cls.userDict:
            user = cls.userDict.get(cardnum)
            if not user.card.islock:
                print("卡未锁定，无需解锁...")
            else:
                idcard = input("请输入您的身份证号码：")
                if idcard == user.idcard:
                    user.card.islock = False
                    print("解锁成功！！！")
                else:
                    print("身份有误，解锁失败...")
        else:
            print("卡号不存在...")

    @classmethod
    def tansmoney(cls):
        if cls.islogin:
            cardnum2 = input("请输入对方的卡号：")
            user = cls.userDict.get(cls.islogin)
            if cardnum2 in cls.userDict:
                mon = int(input("请输入转账金额："))
                if mon>0 and mon <= user.card.money:
                    user.card.money -= mon
                    cls.userDict.get(cardnum2).card.money += mon
                    print("恭喜你转账成功！！！")
                else:
                    print("金额有误或者不足，转账失败！！！")
            else:
                print("此账户不存在，请查证后转账...")
        else:
            print("请登录后转账....")







