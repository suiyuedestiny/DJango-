from django.db import models

# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题', max_length=32)

    def __str__(self):
        return self.title




class UserInfo(models.Model):
    """员工表"""
    username = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    creat_time = models.DateTimeField(verbose_name='入职时间')
    depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)
    gener_choices = (
        (1, '男'),
        (2, '女'),
    )
    gener = models.SmallIntegerField(verbose_name="性别", choices=gener_choices)


class PrettyNum(models.Model):
    """ 靓号表 """
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    price = models.IntegerField(verbose_name='价格')
    lever_choices = (
        (1, '一级靓号'),
        (2, '二级靓号'),
        (3, '三级靓号'),
        (4, '四级靓号'),
    )
    status_choices = (
        (1, '未售卖'),
        (2, '已售卖'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=lever_choices, default=1)
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=2)
