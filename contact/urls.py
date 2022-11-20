from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('', views.ContactListView.as_view(), name = 'home'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('search/', views.search, name='search'),
    path('contact_profile/<int:pk>',views.contact_profile, name ='contact-profile'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
