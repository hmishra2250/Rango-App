from django.conf.urls import patterns,url
from rango import views

urlpatterns = [
	url(r'^$',views.index, name = 'index'),
	url(r'^index/$',views.index, name = 'index2'),
	url(r'^about/$',views.about, name = 'about'),
	url(r'^add_category/$',views.add_category, name = "add_category"),
	url(r'^category/(?P<category_name_url>[\w\-]+)/$',views.category,name = 'category'),
    url(r'^category/(?P<category_name_url>[\w\-]+)/add_page/$',views.add_page,name = 'add page'),
    url(r'^add_category/$',views.add_category, name = "add_category"),
    url(r'^restricted/$',views.restricted, name = "restricted"),
    #url(r'^logout/$',views.user_logout, name = "logout"),
    #url(r'^register/$',views.register, name = "register"),
	#url(r'^login/$',views.user_login, name= "login"),	#deprecated due to django redux :P
]