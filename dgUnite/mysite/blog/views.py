from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import Anthology,Artical
import time
import random
import json

def display(request):
    article=Artical.objects.all()
    return render(request,'blog/首页.html',{'article':article})

@login_required(login_url='go')
def write(request):
    ant_list=Anthology.objects.filter(user=request.user)
    data={'ant_list':ant_list}
    if ant_list:
        active_ant_id=request.GET.get('active_ant_id',ant_list[0].id)
        data['active_ant_id']=int(active_ant_id)
        art_list=Artical.objects.filter(anthology_id=active_ant_id)
        if art_list:
            active_art_id = request.GET.get('active_art_id', art_list[0].id)
            art_current=Artical.objects.get(pk=active_art_id)
            data.update({
                'art_list':art_list,
                'art_current':art_current
            })
    return render(request,'blog/博客写作.html', data)
    # return render(request,'blog/博客写作.html',{'ant_list':ant_list})

def article(request):
    return render(request,'blog/文章页面.html')

#创建文集
def text_create(request):
    name=request.POST['name']
    anthology=Anthology.objects.create(user=request.user,name=name)
    if anthology is not None:
        return HttpResponse('创建成功')
    else:
        return HttpResponse('创建失败')

#更新文集
def text_update(request):
    id=request.POST['id']
    name=request.POST['name']
    Anthology.objects.filter(id=id).update(name=name)
    return redirect('write')

#删除文集
def text_delete(request):
    ant_id = request.GET['id']
    Anthology.objects.get(id = ant_id).delete()
    return redirect('write')

#创建文章
def article_create(request):
    ant_id=request.POST['ant_id']
    article_new=Artical.objects.create(anthology_id=ant_id,title=time.strftime("%Y-%m-%d"))
    if article_new is not None:
        return HttpResponse(json.dumps({
            'ant_id':ant_id,
            'art_id':article_new.id
        }), content_type='application/json')
    else:
        return HttpResponse('创建失败')

#文章发布
def article_post(request):
    art_id=request.POST['art_id']
    ant_id=request.POST['ant_id']
    title=request.POST['title']
    content=request.POST['content']
    res=Artical.objects.update_or_create(id=art_id,anthology_id=ant_id,defaults={'title':title,'content':content})
    if res is not None:
        return HttpResponse('发布成功')
    else:
        return HttpResponse('发布失败')

#删除文章
def article_del(request):
    art_id=request.GET['id']
    Artical.objects.get(id=art_id).delete()
    return redirect('write')

#处理文章发布中的图片ajax上传
def upload_ajax(request):
    if request.method == 'POST':
        file = FileSystemStorage()
        filename = str(int(time.time()*1000)) + str(random.randint(1000, 9999)) + '.png'
        file.save(file.location + '/' + filename, content=request.FILES['img'])
        res = {
            "errno": 0,
            "data": [
                file.base_url + filename
            ]
        }
    return HttpResponse(json.dumps(res), content_type="application/json")













