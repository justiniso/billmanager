from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bills.views.dashboard', name='dashboard'),
    url(r'^create/$', 'bills.views.create', name='create'),
    url(r'^login/$', 'bills.views.login', name='login'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
