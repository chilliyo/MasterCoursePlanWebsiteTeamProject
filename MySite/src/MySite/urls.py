from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^$', 'MyHome.views.home', name='home'),
    url(r'^contact/$', 'MyHome.views.contact', name='contact'),
    url(r'^about/$', 'MySite.views.about', name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
]
