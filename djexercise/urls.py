from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'home.views.home_view', name='go_home'),
    url(r'^json/$', 'home.views.json_view', name='go_json'),
    url(r'^accounts/profile/', 'home.views.profile_view', name='go_profile'),
    url(r'^logout/$', 'home.views.logout_view', name='go_logout'),

    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'', include('api.urls'))
)
