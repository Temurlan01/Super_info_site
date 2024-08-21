from django.contrib import admin

from Main.models import Publication, Publication_Detail, Hashtag, Categorys, PublicationComment




@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Publication_Detail)
class Publication_DetailAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    list_display = ["title"]

@admin.register(PublicationComment)
class PublicationCommentAdmin(admin.ModelAdmin):
    list_display = ["name"]