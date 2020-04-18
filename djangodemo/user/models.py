from django.db import models
import datetime

#由于没有 generate getter/setter 快捷方式，所以都定义成 public
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
    age = models.IntegerField()

    #注册日期
    registryDate = models.DateTimeField()

    #注销日期
    cancelDate = models.DateTimeField()

    #状态，0--已注销 1--正常
    status = models.CharField(max_length=1)

    class Meta:
        unique_together = ('name', 'status',)



    def saveByRequest(self, request, registry):
        self.name = request.POST.get("name");
        self.password = request.POST.get("password")
        self.phone = request.POST.get("phone")

        if self.name is None or self.password is None or self.phone is None:
            return False, "必填信息未填写"

        if registry == True:
            self.registryDate = datetime.datetime.now()
            self.status = "1"

        self.age = request.POST.get("age")
        self.sex = request.POST.get("sex")

        self.save();

        return True, self.id

    def deleteByRequest(self, request, cancel):
        id = request.GET.get("id")
        idQS = CommonUser.objects.get(id=id)
        if idQS is None:
            return False, "删除失败" + id
        if cancel == True:
            idQS.cancelDate = datetime.datetime.now()
        idQS.status = 0
        idQS.save()
        return True, "删除成功"




class AdminUser(models.Model):

    #管理员编号，全局唯一
    no = models.CharField(max_length=10)

    # 账户名称
    name = models.CharField(max_length=100)

    # 账户密码
    password = models.CharField(max_length=12)

    # 联系电话
    phone = models.IntegerField()

    #住址
    address = models.CharField(max_length=200)

    def saveByRequest(self, request):
        self.name = request.POST.get("name");
        self.password = request.POST.get("password")
        self.phone = request.POST.get("phone")

        if self.name is None or self.password is None or self.phone is None:
            return False, "必填信息未填写"

        self.no = NumberFactory.getNewNo()
        self.age = request.POST.get("age")
        self.sex = request.POST.get("sex")

        self.save();

        return True, self.id

class NumberFactory(models.Model):

    #上次 no 值
    currentNo = models.IntegerField()
    #上次日期
    lastDate = models.DateField()
    #编号前缀
    prefix = models.CharField(max_length=20)

    suffixSize = models.IntegerField(default=4)

    def getNewNo(self):
        last = NumberFactory.objects.get(0);
        newDate = datetime.date()

        if newDate < last.lastDate:
            return False, "数据库中数据错误，上次更新日期大于当前日期"

        if newDate > last.lastDate:
            self.resetNumberFactory(newDate, 0)

        newNo = self.getNo(last.prefix, last.currentNo, last.suffixSize)

        self.currentNo = last.currentNo + 1
        self.save()

        return newNo


    def resetNumberFactory(self, newDate, currentNo):
        self.lastNo = currentNo
        self.lastDate = newDate
        self.prefix = newDate.year + newDate.month + newDate.day
        self.save()


    def getNo(self, prefix, no, suffixSize):
        if prefix is None:
            prefix = self.prefix

        if no is None:
            no = self.currentNo

        if suffixSize is None:
            suffixSizer = self.suffixSize

        list = [0] * (suffixSize - len(str(no)))
        list.append(str(no))

        return "".join(list)





