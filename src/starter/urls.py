from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'movies.views.home', name='home'),
    url(r'^details/$', 'movies.views.details', name='details'),
    url(r'^popularity/$', 'movies.views.popularity', name='popularity'),
    url(r'^freshness/$', 'movies.views.freshness', name='freshness'),
    url(r'^MPAA/$', 'movies.views.MPAA', name='MPAA'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.TEMPLATE_URL,
                          document_root=settings.TEMPLATE_ROOT)