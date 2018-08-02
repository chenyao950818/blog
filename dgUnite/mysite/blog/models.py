from django.db import models
from django.contrib.auth.models import User
class Anthology(models.Model):
    class Meta:
        verbose_name='文集'
        verbose_name_plural=verbose_name
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(u'姓名',max_length=20,null=False)
    last_updated=models.DateTimeField(u'最后更新时间',auto_now=True)
    date_created=models.DateTimeField(u'创建时间',auto_now_add=True)
    def __str__(self):
        return self.name
class Artical(models.Model):
    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name
    title=models.CharField(u'标题', max_length=30,null=False)
    content=models.TextField(u'正文',null=False)
    anthology= models.ForeignKey(Anthology, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(u'最后更新时间',auto_now=True)
    date_created = models.DateTimeField(u'创建时间',auto_now_add=True)
    def __str__(self):
        return self.title

# Create your models here.
