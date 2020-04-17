from django.shortcuts import render
from django.http import HttpResponse
from user.models import CommonUser, AdminUser

# Create your views here.
def login(request):

    loginName = request.GET.get("loginName")
    loginPassword = request.GET.get("loginPassword")

    print("zhaoliang:")

    if loginName is None or loginPassword is None:
        return HttpResponse("用户名或密码为空")

    qs = CommonUser.objects.values()

    validateLoginQS = qs.filter(name=loginName)
    if not(validateLoginQS.exists()):
        print("zhaoliang:")
        return HttpResponse("该用户不存在")

    validateQS = qs.filter(name=loginName).filter(password=loginPassword)
    if validateQS.exists():
        return HttpResponse("欢迎登录：" + validateQS.values().first().get("name"))
    else:
        return HttpResponse("用户名或密码不正确")

def logout(reuqest):
    return HttpResponse("欢迎再次光临")