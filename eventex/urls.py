from django.conf.urls import include, url
from django.contrib import admin
from eventex.core.views import home


urlpatterns = [
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
]
