from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


#注册界面/注册处理
def reg(request):
    if request.method=='GET':
        return render(request, 'blog/注册.html')
    else:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,email=email,password=password)
        if user is not None:
            return redirect('go')
        else:
            return render('注册失败，请重新注册')

#登录界面/登录处理
def go(request):
    if request.method=='GET':
        next_url=request.GET.get('next','')
        return render(request, 'blog/登录.html',{'next':next_url})
    else:
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('账户未激活，请联系管理员！')
        else:
            return HttpResponse('账户不存在，请先注册！')

def goout(request):
    logout(request)
    return redirect('display')
