from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    context = {
        "city": "北京",
        "dict": {
            "name": "西游记",
            "author": "吴承恩"
        },
        "list": [1, 2, 3, 4],
        "book_list": [
            {"name": "西游记", "author": "吴承恩"},
            {"name": "三国演义", "author": "罗贯中"},
            {"name": "水浒传", "author": "施耐庵"},
        ]
    }


    return HttpResponse("hello world!")
    # return HttpResponse("<h1>hello world!</h1>")
    # return render(request, "index.html", context)

def weather(request, year, city):
    print("city=", city)
    print("year=", year)
    return HttpResponse(city + ":" + year)


def weather2(request):
    print("request.GET=", request.GET)
    city = request.GET.get("city")
    year = request.GET.get("year")
    year_list = request.GET.getlist("year")

    print("city=", city)
    print("year=", year)
    print("year_list=", year_list)
    return HttpResponse("OK")
