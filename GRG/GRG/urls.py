from django.conf.urls import patterns, include, url
from account.views import regist

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GRG.views.home', name='home'),
    # url(r'^GRG/', include('GRG.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
   # (r'^login/$',longin),
    (r'^regist/$',regist),
    (r'^test/$',test),
)
