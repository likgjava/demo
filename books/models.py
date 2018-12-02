from django.db import models


# 定义图书模型
class Book(models.Model):
    title = models.CharField(max_length=20, verbose_name="图书名称")
    pub_date = models.DateField(verbose_name="发布日期")
    read = models.IntegerField(default=0, verbose_name="阅读量")
    comment = models.IntegerField(default=0, verbose_name="评论量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        db_table = "t_book"
        verbose_name = "图书"

    def __str__(self):
        return "id={} title={}".format(self.id, self.title)


# 定义英雄人物模型
class Hero(models.Model):
    GENDER_CHOICES = ((0, "male"), (1, "female"))
    name = models.CharField(max_length=20, verbose_name="姓名")
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name="性别")
    description = models.CharField(max_length=200, null=True, verbose_name="描述")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="所属图书")
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = "t_hero"
        verbose_name = "英雄人物"

    def __str__(self):
        return self.name
