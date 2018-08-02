# Generated by Django 2.0.7 on 2018-07-10 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anthology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '文集',
                'verbose_name': '文集',
            },
        ),
        migrations.CreateModel(
            name='Artical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', models.TextField(verbose_name='正文')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('anthology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Anthology')),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
        migrations.DeleteModel(
            name='Articals',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
