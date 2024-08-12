from django.db import models


class Categorys(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Publication(models.Model):
    Hashtag = models.ManyToManyField(Hashtag, null=True)
    name = models.CharField(max_length=250)
    short_descriptions = models.TextField()
    images = models.ImageField()
    my_date = models.DateField(null=True)
    is_activ = models.BooleanField(null=True)


class Publication_Detail(models.Model):
    Categorys = models.ForeignKey(Categorys, on_delete=models.CASCADE, null=True, related_name='publication')
    Hashtag = models.ManyToManyField(Hashtag, null=True)
    name = models.CharField(max_length=250)
    descriptions = models.TextField()
    images = models.ImageField()
    date = models.DateField(null=True)


class PublicationComment(models.Model):
    Publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)


