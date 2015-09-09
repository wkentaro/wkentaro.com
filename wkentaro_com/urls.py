from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'wkentaro_com.views.index', name='index'),
    url(r'^about/$', 'wkentaro_com.views.about', name='about'),
    url(r'^research/$', 'wkentaro_com.views.research', name='research'),
    url(r'^admin/', include(admin.site.urls)),
)
