from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from MyHome.views import home, contact
from MySite.views import about

urlpatterns = [
    #url(r'^$', 'MyHome.views.home', name='home'),
    url(r'^$', home, name='home'),
    #url(r'^contact/$', 'MyHome.views.contact', name='contact'),
    url(r'^contact/$', contact, name='contact'),
    #url(r'^about/$', 'MySite.views.about', name='about'),
    url(r'^about/$', about, name='about'),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
