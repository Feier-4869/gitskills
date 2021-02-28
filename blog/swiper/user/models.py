from django.db import models


# Create your models here.
# 姓名　年龄　性别　email phone

class User(models.Model):
    # 字段＝models.字段类型（选项）

    SEX = (
        ('0', 'male'),
        ('1', 'female')
    )

    name = models.CharField(max_length=50, unique=True, verbose_name='姓名')
    age = models.IntegerField(default=0, verbose_name='年龄')
    sex = models.CharField(max_length=10, choices=SEX, verbose_name='性别')
    email = models.CharField(max_length=11, verbose_name='邮箱')
    phone = models.CharField(max_length=11, verbose_name='手机')
    avater = models.ImageField(upload_to='upload', verbose_name='头像')

    class Meta:
        # 项目＋子应用
        db_table = 'sp_user'

    def __str__(self):
        return self.name


# 书名　作者　日期　阅读数　评论数
class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="书名")
    author = models.CharField(max_length=100, verbose_name='作者')
    pubdate = models.DateField(auto_now_add=True, verbose_name='日期')
    reads = models.ImageField(default=0, verbose_name='阅读数')
    comments = models.ImageField(default=0, verbose_name='评论数')

    class Meta:
        db_table = 'sp_book'

    def __str__(self):
        return self.name


# 人物名　技能　简介　武器
class Hero(models.Model):
    hname = models.CharField(max_length=100, verbose_name='人物')
    skill = models.CharField(max_length=100, verbose_name='技能')
    intro = models.CharField(max_length=100, verbose_name='简介')
    weapon = models.CharField(max_length=100, verbose_name='武器')
    # related_name表示反向关联
    hbook=models.ForeignKey(Book,related_name='hero',verbose_name='和图书的关系')


    class Meta:
        db_table='sp_hero'

    def __str__(self):
        return self.hname