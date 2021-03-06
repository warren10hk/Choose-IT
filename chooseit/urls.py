"""chooseit URL Configuration

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
from . import views
from appuser import views as appview
from phone import views as phoneview
from estrating import views as estratingview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^apply/', appview.register),
    url(r'^login/', appview.loginfunc),
    url(r'^logout/', appview.logoutfunc),
    url(r'^choosemyphone/', phoneview.choosemyphone),
    url(r'^phonedis/(?P<pid>[-\d]+)$', phoneview.displayone),
    url(r'^filter/', phoneview.filterfunc),
    url(r'^allphones/', phoneview.returnall),
    url(r'^diff/', phoneview.diff),
    url(r'ajax/getpic', phoneview.returnpic),
    url(r'^ajax/getmodel/$', phoneview.returnmodel),
    url(r'^ajax/getmcontent/$',phoneview.returnmcontent),
    url(r'^ajax/getallmodel',phoneview.returnallmodel),
    url(r'^estimaterating/',estratingview.estimateRating)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
