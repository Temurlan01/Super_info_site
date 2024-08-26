from xml.etree.ElementInclude import include
from Super_info_core import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from Main.views import HomeView, ContactView, PublicationDetailView, HomeSearchView, CreatePublicationCommentView, CreatePublicationContactView






urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', HomeView.as_view(), name='Home_list'),
    path('home/search', HomeSearchView.as_view(), name='home_search_url'),
    path('contact/', ContactView.as_view(), name='contact_list'),
    path('Publication-detail/<int:pk>/', PublicationDetailView.as_view(), name='Publication_Detail_url'),
    path('Publication-detail/<int:pk>/create-comment/', CreatePublicationCommentView.as_view()),
    path('contact/create-comment/', CreatePublicationContactView.as_view()),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)