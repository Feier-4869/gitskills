class Card:
    """
    創建卡片
    """
    def __init__(self,cardnum,password,money,islock=False):
        self.cardnum=cardnum
        self.password=password
        self.money=money
        self.islock=islock