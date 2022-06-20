from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from conf import settings
from cars.api.urls import router as cars_router


router = DefaultRouter()
router.registry.extend(cars_router.registry)
urlpatterns = [
    path('fff/', admin.site.urls),
    path('api/auth/', include('authentication.api.urls'), name='api_auth'),
    path('api/carwash/', include('carwash.api.urls'), name='api_carwash'),
    path('api/cars/', include('cars.api.urls'), name='api_cars'),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('', include('carwash.urls'), name='carwash'),
    path('auth/', include('authentication.urls'), name='authentication'),
    path('profile/', include('profiles.urls'), name='profiles'),
    path('cars/', include('cars.urls'), name='cars'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)