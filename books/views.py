from datetime import date

from django.db.models import F, Q, Sum
from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book, Hero


def to_add(request):
    return render(request, "add_book.html")


def add(request):
    # book = Book()
    # book.title = "西游记"
    # book.pub_date = date(1986, 1, 1)
    # book.read = 10
    # book.comment = 20
    # book.save()
    #
    # hero = Hero(name="孙悟空", gender=0, description="大闹天宫", book=book)
    # hero.save()

    Book.objects.create(title="三国演义", pub_date=date(1990, 1, 1))

    return HttpResponse("OK")

    # return render(request, "add_book.html")


def get(request):
    # # 获取全部数据
    # book_list = Book.objects.all()
    # print("book_list=", book_list)
    #
    # # 获取单个数据
    # book = Book.objects.get(id=1)
    # print("book=", book)
    #
    # # 查询结果数量
    # count = Book.objects.count()
    # print("count=", count)

    # # 查询id为1的图书
    # book = Book.objects.filter(id__exact=1)
    # print("book=", book)
    # book = Book.objects.filter(id=1)
    # print("book=", book)

    # # 查询书名包含'英雄'的图书
    # book = Book.objects.filter(title__contains="英雄")
    # print("book=", book)
    # # 查询书名以'三国'开头的图书
    # book = Book.objects.filter(title__startswith="三国")
    # print("book=", book)
    # # 查询书名以'传'结尾的图书
    # book = Book.objects.filter(title__endswith="传")
    # print("book=", book)

    # # 查询书名不为空的图书
    # books = Book.objects.filter(title__isnull=False)
    # print("books=", books)

    # # 查询id为1或3或5的图书
    # books = Book.objects.filter(id__in=[1, 3, 5])
    # print("books=", books)

    # # 查询id大于3的图书
    # books = Book.objects.filter(id__gt=3)
    # print("books=", books)
    #
    # # 查询id不等于3的图书
    # books = Book.objects.exclude(id=3)
    # print("books=", books)

    # # 查询1980年发表的图书
    # books = Book.objects.filter(pub_date__year=1980)
    # print("books11=", books)
    # # 查询1980年1月1日后发表的图书
    # books = Book.objects.filter(pub_date__gt=date(1980, 1, 1))
    # print("books22=", books)

    # # 查询阅读量大于等于评论量的图书
    # books = Book.objects.filter(read__gt=F("comment"))
    # print("books=", books)
    # # 查询阅读量大于2倍评论量的图书
    # books = Book.objects.filter(read__gt=F("comment") * 2)
    # print("books=", books)

    # # 查询阅读量大于20，并且id小于3的图书
    # books = Book.objects.filter(read__gt=20, id__lt=3)
    # print("books=", books)
    # books = Book.objects.filter(read__gt=20).filter(id__lt=3)
    # print("books=", books)

    # # 查询阅读量大于20的图书，改写为Q对象如下
    # books = Book.objects.filter(Q(read__gt=20))
    # print("books=", books)

    # # 查询阅读量大于20，或id小于3的图书，只能使用Q对象实现
    # books = Book.objects.filter(Q(read__gt=20) | Q(id__lt=3))
    # print("books=", books)

    # # 查询id不等于3的图书
    # books = Book.objects.filter(~Q(id=3))
    # print("books=", books)

    # # 查询图书的总阅读量
    # data = Book.objects.aggregate(Sum("read"))
    # print(type(data))
    # print("books=", data)

    # # 按阅读量升序排列
    # books = Book.objects.all().order_by("read")
    # print("books=", books)
    # # 按阅读量降序排列
    # books = Book.objects.all().order_by("-read")
    # print("books=", books)

    # # 查询id为1的图书中的所有英雄人物
    # book = Book.objects.get(id=1)
    # hero_list = book.hero_set.all()
    # print("hero_list=", hero_list)

    # # 查询id为1的英雄人物所属的图书
    # hero = Hero.objects.get(id=1)
    # book = hero.book
    # print("book=", book.id)

    # # 把英雄名字为‘猪八戒’的改成‘猪悟能’
    # hero = Hero.objects.get(name="猪八戒")
    # hero.name = "猪悟能"
    # hero.save()
    # # 或者
    # count = Hero.objects.filter(name="猪八戒").update(name="猪悟能")
    # print("count=", count)

    #
    # hero = Hero.objects.get(id=19)
    # hero.delete()

    count = Hero.objects.filter(id=19).delete()
    print("count=", count)

    return HttpResponse("OK")
