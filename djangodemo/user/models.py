from django.db import models

class CommonUser(models.Model):

    #账户名称，全局唯一
    name = models.CharField(max_length=100)

    #账户密码
    password = models.CharField(max_length=12)

    #联系电话
    phone = models.IntegerField

    #账户余额
    accountBalance = models.FloatField()

    #性别
    sex = models.CharField(max_length=1)

    #年龄
    age = models.IntegerField

    #注册日期
    registryDate = models.DateTimeField

    #注销日期
    cancelDate = models.DateTimeField

    #状态，0--已注销 1--正常
    status = models.CharField(max_length=1)


class AdminUser(models.Model):

    #管理员编号，全局唯一
    no = models.CharField(max_length=10)

    # 账户名称
    name = models.CharField(max_length=100)

    # 账户密码
    password = models.CharField(max_length=12)

    # 联系电话
    phone = models.IntegerField

    #住址
    address = models.CharField(max_length=200)



