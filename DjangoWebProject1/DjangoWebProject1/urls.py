"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
import app
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    url(r'^anketa$', app.views.anketa, name='anketa'),
    url(r'^registration$',app.views.registration, name='registration'),
    url(r'^blog', app.views.blog, name='blog'),
    url(r'^newpost$', app.views.newpost, name='newpost'),
    url(r'^videopost$', app.views.videopost, name='videopost'),
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
