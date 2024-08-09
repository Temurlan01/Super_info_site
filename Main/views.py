from django.shortcuts import render
from django.views.generic import TemplateView

from Main.models import Publication, Publication_Detail


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
            context = {
                'Publication_list': Publication.objects.filter(is_activ=True),

                     }
            return context


class ContactView(TemplateView):
    template_name = 'contact.html'


class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
            publication_pk = kwargs['pk']
            context = {
                'Publication_Detail': Publication_Detail.objects.get(id=publication_pk),

                    }
            return context