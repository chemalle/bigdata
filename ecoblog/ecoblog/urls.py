"""ecoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from posts import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^chemalle/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_details, name="post_detail"),
    url(r'^simple/$', views.simple, name="simple"),
    url(r'^stocks/$', views.Stocks_Data, name="stocks"),
    url(r'^recommendation/$', views.recommendation, name="recommendation"),
    url(r'^stock2/$', views.stock2, name='udacity'),
    url(r'^ploty/$', views.ploty, name='ploty'),
    url(r'^graph2/$', views.graph_of_the_day, name='graph_of_the_day'),
    url(r'^stock3/$', views.stock3, name='graph'),
    url(r'^valuation/$', views.Enterprise_Valuation, name='valuation'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
