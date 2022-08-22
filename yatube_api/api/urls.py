from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'v1/posts', PostViewSet)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/follow', FollowViewSet, basename='follows',)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
