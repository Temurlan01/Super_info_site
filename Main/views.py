from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import redirect
from Main.models import Publication, Publication_Detail, PublicationComment, PublicationContact

from Main.telegram_bot import bot


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        publications = Publication.objects.all()

        paginator = Paginator(publications, 3)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context = {
            'Page_obj': page_obj
                    }
        return context


class HomeSearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs, ):
        search_word = self.request.GET['search']
        context = {
            'Publication_list': Publication.objects.filter(is_activ=True).filter(
            Q(name__icontains=search_word) | Q(short_descriptions__icontains=search_word),
            )
        }
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'


class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
            publication_pk = kwargs['pk']
            context = {
                'Publication_Detail': Publication_Detail.objects.get(
                    id=publication_pk),
                'Publication_list': Publication.objects.all(),

                    }
            return context


class CreatePublicationCommentView(View):

    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication_Detail.objects.get(id=publication_pk)

        comment_text = request.POST['comment_text']
        name = request.POST['name']

        PublicationComment.objects.create(Publication_Detail=publication, text=comment_text, name=name, )
        bot.send_message(chat_id=6197731316, text='для вашей публикации написали комментарий'),

        return redirect('Publication_Detail_url', pk=publication_pk)


class CreatePublicationContactView(View):

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        Email = request.POST.get('Email')
        Subject = request.POST.get('Subject')
        Message = request.POST.get('Message')


        PublicationContact.objects.create(name=name, Email=Email, Subject=Subject, Message=Message)
        bot.send_message(chat_id=6197731316, text='С вами ктото хочет связатся '),
        return redirect('contact_list')






