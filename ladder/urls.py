from rest_framework import routers
from .views import TagViewSet,UserViewSet,LadderViewSet,UnitViewSet,LinkViewSet,LearningStatusViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'ladder',LadderViewSet)
router.register(r'unit',UnitViewSet)
router.register(r'tag',TagViewSet)
router.register(r'link',LinkViewSet)
router.register(r'learningstatus',LearningStatusViewSet)
