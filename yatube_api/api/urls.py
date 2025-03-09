from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views


API_VERSION = 'v1'

v1_router = SimpleRouter()

v1_router.register('posts', views.PostViewSet)
v1_router.register('groups', views.GroupViewSet)
v1_router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)
v1_router.register('follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path(f'{API_VERSION}/', include('djoser.urls.jwt')),
    path(f'{API_VERSION}/', include(v1_router.urls)),
]
