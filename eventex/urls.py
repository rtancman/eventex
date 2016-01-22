from django.conf.urls import include, url
from django.contrib import admin
from eventex.core.views import home
from eventex.subscriptions.views import subscribe, detail

urlpatterns = [
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^inscricao/$', subscribe),
    url(r'^inscricao/(\d+)/$', detail),
    url(r'^admin/', include(admin.site.urls)),
]
