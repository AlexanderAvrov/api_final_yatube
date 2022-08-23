from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet)
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(r'v1/groups', GroupViewSet)
router_v1.register(r'v1/follow', FollowViewSet, basename='follows',)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
