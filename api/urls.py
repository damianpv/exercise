from django.conf.urls import patterns, include, url
from rest_framework import routers

from .views import UserViewSet, FriendViewSet, AuthView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'friends', FriendViewSet)

urlpatterns = patterns('',

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/$', AuthView.as_view(), name='authenticate'),

)