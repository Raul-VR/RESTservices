# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('usuarios',views.usuarios, name='usuarios'),
#     path('partidas',views.partidas, name='partidas'),
# ]
#     # path('', views.index, name='index'), 
#     # path('', include('videojuego.urls')),
#     # path('lorem', views.lorem, name='lorem')
# ]

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.usuariosViewSet)
router.register(r'partidas', views.partidasViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]