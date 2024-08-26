from django.db import models


class Categorys(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name="Название")

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name="Название")

    def __str__(self):
        return self.title


class Publication(models.Model):
    Hashtag = models.ManyToManyField(Hashtag, null=True)
    name = models.CharField(max_length=250, verbose_name="Название")
    short_descriptions = models.TextField(verbose_name="Краткое описание")
    images = models.ImageField(verbose_name="Изображение")
    my_date = models.DateField(null=True)
    is_activ = models.BooleanField(null=True)


class Publication_Detail(models.Model):
    Categorys = models.ForeignKey(Categorys, on_delete=models.CASCADE, null=True, related_name='publication', verbose_name="Категория")
    Hashtag = models.ManyToManyField(Hashtag, null=True, verbose_name="Хэштег")
    name = models.CharField(max_length=250, verbose_name="Название")
    descriptions = models.TextField(verbose_name="Описание")
    images = models.ImageField(verbose_name="Изаброжение")
    date = models.DateField(null=True)


class PublicationComment(models.Model):
    Publication_Detail = models.ForeignKey(Publication_Detail, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateField(auto_now_add=True)


class PublicationContact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    Email = models.EmailField(null=True, blank=True)
    Subject = models.TextField(null=True, blank=True)
    Message = models.TextField(null=True, blank=True)


