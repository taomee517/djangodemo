from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand

# Create your views here.
# 用于创建视图


def index(request):
    # 返回String
    # return HttpResponse("Hello,World!")

    # 返回视图渲染
    return render(request, 'carbrand/index.html')


def brand_list(request):
    # 去模板里取数据
    brands = Brand.objects.all()
    print(brands)
    # 将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'carbrand/brandList.html', {'brands': brands})


