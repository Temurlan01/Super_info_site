from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.db.models import Q
from django.shortcuts import redirect
from Main.models import Publication, Publication_Detail, PublicationComment, Hashtag


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
            context = {
                'Publication_list': Publication.objects.filter(is_activ=True),


                     }
            return context


class HomeSearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs, ):
        search_word = self.request.GET['search']
        context = {
            'Publication_list': Publication.objects.filter(is_activ=True).filter(
            Q(name__icontains=search_word) | Q(short_descriptions__icontains=search_word) | Q(Hashtag=search_word),
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
        publication = Publication.objects.get(id=publication_pk)

        comment_text = request.POST['comment_text']

        PublicationComment.objects.create(
            Publication=publication, text=comment_text,)

        return redirect('Detail_url', pk=publication_pk)