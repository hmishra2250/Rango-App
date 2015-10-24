"""him URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from rango import views
from django.conf import settings
from registration.backends.simple.views import RegistrationView    ##override default registrstions

class MyRegistationView(RegistrationView):
    def get_success_url(self,request,user):
        return '/rango/'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls),name = 'admin'),
    url(r'^rango/',include('rango.urls')),
    url(r'^accounts/register/',MyRegistationView.as_view(),name = 'registraion_register'),
    url(r'^accounts/',include('registration.backends.simple.urls')),    ##Django registraion redux app
    url(r'^$',views.index),

]

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		url(r'^media/(?P<path>.*)',
			'serve',
			{'document_root' : settings.MEDIA_ROOT}),
		)