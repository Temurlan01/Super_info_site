from Super_info_core import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from Main.views import HomeView, ContactView, PublicationDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', HomeView.as_view(), name='Home_list'),
    path('contact/', ContactView.as_view(), name='contact_list'),
    path('Publication-detail/<int:pk>/', PublicationDetailView.as_view(), name='Detail_url'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)