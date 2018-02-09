"""CSCdropdown URL Configuration

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
from location import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^country/(?P<id>\d+)/$', views.state_view),
    url(r'^state/(?P<id>\d+)/$', views.city_view),
    url(r'^(?P<conid>\d+)/(?P<sid>\d+)/(?P<cid>\d+)/$', views.location_view),
     url(r'^(?P<conid>\d+)/(?P<sid>\d+)/$', views.location_view2),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)