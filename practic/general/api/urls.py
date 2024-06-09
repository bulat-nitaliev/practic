from rest_framework.routers import SimpleRouter
from general.api.views import IslamViewSet, VredPrivichkiViewSet, UserVievSet, CelViewSet, CommentViewSet

router = SimpleRouter()

router.register('islam', IslamViewSet, 'islam')
router.register('vredprivichki', VredPrivichkiViewSet, 'vredprivichki')
router.register('users', UserVievSet, 'users')
router.register('cel', CelViewSet, 'cel')
router.register('comment', CommentViewSet, 'comment')

urlpatterns = router.urls