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
