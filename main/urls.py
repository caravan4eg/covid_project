from django.contrib import admin
from django.urls import path, include

# media upload
from django.conf import settings
from django.conf.urls.static import static
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import routers
from api.views import PostViewSet, ProjectViewSet, FactViewSet

router = routers.DefaultRouter()
router.register('facts', FactViewSet)
router.register('posts', PostViewSet)
router.register('projects', ProjectViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include('get_data.urls'))

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
