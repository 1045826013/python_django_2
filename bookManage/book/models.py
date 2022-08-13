from django.db import models

# Create your models here.
"""
    属性名 = models.类型（）
    verbose_name admin站点的名字
    ID 系统默认生成
    
    改变表的名称 ： 
      默认是子应用名_类名（小写）
      修改表名
      
"""
class BookInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    #修改表名
    class Meta:
        db_table = 'bookInfo'
        verbose_name = '书籍管理'
class PeopleInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    #定一个有序字典
    GENDER_CHOICE = ((1,'male'),(2,'female'))
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'
