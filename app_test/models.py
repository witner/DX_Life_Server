from django.db import models

# Create your models here.

__all__ = ["Book", "Publisher", "Author"]


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="图书名称")
    CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
    category = models.IntegerField(choices=CHOICES, verbose_name="图书的类别")
    pub_time = models.DateField(verbose_name="图书的出版日期")

    publisher = models.ForeignKey(to="Publisher", on_delete=None)
    author = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField(max_length=32, verbose_name="出版社的名称")

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者的姓名")

    def __str__(self):
        return self.name

