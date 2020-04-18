from django.shortcuts import render
from django.http import HttpResponse
from user.models import CommonUser, AdminUser

# Create your views here.
def login(request):

    loginName = request.GET.get("loginName")
    loginPassword = request.GET.get("loginPassword")

    if loginName is None or loginPassword is None:
        return HttpResponse("用户名或密码为空")

    qs = CommonUser.objects.values()

    validateLoginQS = qs.filter(name=loginName, status=1)
    if not(validateLoginQS.exists()):
        return HttpResponse("该用户不存在")

    validateQS = qs.get(name=loginName, password=loginPassword)
    if validateQS.exists():
        return HttpResponse("欢迎登录：" + validateQS.name)
    else:
        return HttpResponse("用户名或密码不正确")

def logout(reuqest):
    return HttpResponse("欢迎再次光临")


def registry(request):
    registryName = request.POST.get("name")
    commonUser = None
    try:
        CommonUser.objects.get(name=registryName, status=1)
    except:
        pass

    if commonUser is not None:
        return HttpResponse("该用户名已存在")

    flag, result = CommonUser().saveByRequest(request, True)
    if flag == True:
        result = "注册成功"
    return HttpResponse(result)


def cancel(request):
    flag, result = CommonUser().deleteByRequest(request, True)
    if flag == True:
        result = "注销成功"
    else:
        result = "注销失败"
    return HttpResponse(result)
