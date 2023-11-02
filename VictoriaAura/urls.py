from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


from backend.views import ImgViewSet,GameDisciplineViewSet,NewsViewSet,UserViewSet,TeamViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'img', ImgViewSet)
router.register('game-discipline',GameDisciplineViewSet)
router.register('news',NewsViewSet)
router.register('user',UserViewSet)
router.register("team",TeamViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
