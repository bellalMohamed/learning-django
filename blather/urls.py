from django.conf.urls import include, url
from django.contrib import admin
from blat import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blather.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name="homepage"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
]
