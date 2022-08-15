from django.shortcuts import render
from django.http import  HttpRequest
from django.http import HttpResponse
from book.models import BookInfo
from book.models import PeopleInfo
# Create your views here.
def index(request):
    #获取表数据
    books = BookInfo.objects.all()

    return HttpResponse(books)
########增加数据#########3
#BookInfo对象
#增加数据方法1
'''
book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount='10'
)
book.save()
#增加数据方法2
#objects
'''
BookInfo.objects.create(
    name='测试开发入门',
    pub_date='2020-3-4',
    readcount='1'
)
'''

######查询########3
#方式1
try:
    book = BookInfo.objects.get(id=5) #只能返回唯一的数据，存在多条数据满足条件报错
    book.name =  '运维开发入门'
    #book.save()
except BookInfo.DoesNotExist:
    print('get return data not exist')
#方式2
BookInfo.objects.filter(id=7).update(name='爬虫入门',commentcount = '5')


######删除###########
#1逻辑删除 is_delete = true
#2物理删除
book = BookInfo.objects.filter(name = 'Django').delete() #filter 可返回 满足条件的多条数据


#####查询#######3
#get    查询单一对象 不存在抛出DoesNoExist异常 查询到多个MultipleObjectsReturned异常
try:
    book = BookInfo.objects.get(id = 10) #简写
    book = BookInfo.objects.get(id__exact=10) #完整形式
    book = BookInfo.objects.get(pk = 1)  #pk 即primary key 主键
except BookInfo.DoesNotExist:
    print("查询结果不存在")

#all
BookInfo.objects.all();
#count 查询结果数量
count = BookInfo.objects.all().count()
count2 = BookInfo.objects.count()

######过滤查询#######33
#filter(属性名__运算符关键字 = 值) 即 where #返回 列表
BookInfo.objects.filter(id=3)
#书名包含入门
BookInfo.objects.filter(name__contains='入门')
# 书名为空的行
BookInfo.objects.filter(name__isnull=True)
#查询编号为 1 3 5 的图书
BookInfo.objects.filter(id__in=(1,3,5))
BookInfo.objects.filter(id__in=[1,3,5])
#查询编号大于5  大于gt (great)  小于lt (less) 小于等于lte (equal)
try:
    BookInfo.objects.filter(id__gt=5)
except BookInfo.DoesNotExist:
    print("id = 5数据不存在")
#查询编号不等于三的书籍 #exclude 排除符合条件的剩下的
BookInfo.objects.exclude(id=3)
#查询1980年发布的图书
BookInfo.objects.filter(pub_date__year=1980)
#查询1990年1月1号后发布的的图书
BookInfo.objects.filter(pub_date__gt="1990-1-1")

from django.db.models import  F
#F  用与两个属性的比较 filter(属性名__运算符关键字 = F（'第二个属性名'）)
#阅读量大于两倍评论量的书籍
BookInfo.objects.filter(commentcount__gte=F('readcount')*2)

#并且查询
#查询阅读了大于20 并且 编号小于三
BookInfo.objects.filter(readcount__gt=20).filter(id__lt = 3)
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

#或查询 filter(Q(属性名__运算符关键字=值）｜Q(属性名__运算符关键字=值） ｜ ... )
#且查询 filter(Q(属性名__运算符关键字=值）& Q(属性名__运算符关键字=值） & ... )
#非查询 filter(～Q(属性名__运算符关键字=值）｜ ～Q(属性名__运算符关键字=值） & ... )
from django.db.models import  Q
#阅读了大于20 id 小于3
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt = 3))
from django.db.models import Sum,Count
#####聚合函数######
#数据的行数
BookInfo.objects.filter(name__contains='入门').count
BookInfo.objects.aggregate(Sum("readcount"))

#排序函数 -字段名 逆序
BookInfo.objects.all().order_by('-readcount')

###极联查询######333
#系统根据外键 在主表中自动添加peopleinfo_set=[PeopleInfo,PeopleInfo,....]
book = BookInfo.objects.get(id=3) #必须用get函数
book.peopleinfo_set.all()

###查询人物表对应的书籍
people = PeopleInfo.objects.get(id =1)
people.book.name

###查询图书， 要求人物为郭靖
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
###查询图书，要求人物描述包含'八'
BookInfo.objects.filter(peopleinfo__description__contains='八')

###查询书名为天龙八部的所有人物
#book = BookInfo.objects.get(name = '天龙八部')
#book.peopleinfo_set.all()
#查询书籍名为天龙八部的所有人物
peoples = PeopleInfo.objects.filter(book__name='天龙八部') #结果集为列表
peoples[1].name
for people in peoples:
    print(people.name)
'''




