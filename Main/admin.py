from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from Main.models import Publication, Publication_Detail, Hashtag, Categorys, PublicationComment, PublicationContact


@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ["id", "name"]


@admin.register(Publication_Detail)
class Publication_DetailAdmin(TranslationAdmin):
    list_display = ["id", "name"]


@admin.register(Hashtag)
class HashtagAdmin(TranslationAdmin):
    list_display = ["id", "title"]


@admin.register(Categorys)
class CategorysAdmin(TranslationAdmin):
    list_display = ["id", "title"]

@admin.register(PublicationComment)
class PublicationCommentAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(PublicationContact)
class PublicationContactAdmin(admin.ModelAdmin):
    list_display = ["name"]
