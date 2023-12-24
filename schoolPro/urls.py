"""schoolPro URL Configuration

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
from django.conf import settings
# from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
# import re_path
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(("schoolApp.urls", 'schoolApp'), namespace='schoolApp')),
    re_path(r'^Transport/', include(("Transport.urls", 'transport'), namespace='transport')),
    re_path(r'^api/', include(("schoolApp.apiUrls", 'schoolApp'), namespace='schoolAppApi')),
    re_path(r'^apiT/', include(("Transport.apiUrls", 'transportApi'), namespace='transportApi')),
    re_path(r'^Students/', include(("students.urls", 'students'), namespace='students')),
    re_path(r'^SchoolTableApi/', include(("schoolApp.datatableApi.urls", 'schoolApp'), namespace='SchoolTableApi')),
    re_path('', include('pwa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)