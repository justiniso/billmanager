from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bills.views.dashboard', name='dashboard'),
    url(r'^create/$', 'bills.views.create', name='create'),
    # url for all bills /bills/
    url(r'^bills/(\d+)/$', 'bills.views.show_bill', name='bill'),
    url(r'^bills/(\d+)/delete/$', 'bills.views.delete_bill', name='delete_bill'),
    url(r'^users/(\d+)/add/$', 'bills.views.add_user', name='add_user'),
    url(r'^login/$', 'bills.views.login', name='login'),
    url(r'^register/$', 'bills.views.register', name='register'),
    url(r'^logout/$', 'bills.views.logout', name='logout'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
