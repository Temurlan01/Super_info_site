from .models import Categorys, Hashtag, Publication, Publication_Detail, PublicationComment, PublicationContact
from modeltranslation.translator import register, TranslationOptions


@register(Categorys)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Hashtag)
class HashtagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('name', 'short_descriptions')


@register(Publication_Detail)
class Publication_DetailTranslationOptions(TranslationOptions):
    fields = ('name', 'descriptions')





