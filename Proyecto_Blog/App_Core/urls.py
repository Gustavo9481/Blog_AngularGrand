from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from App_Core import views

# ............................. App Core | urls .............................. 󰌠



urlpatterns = [
        path('', views.home, name='HOME'),
        path('articulo/<str:titulo>', views.articulo, name="ARTICULO"),
        path('articulos_all/', views.articulos_all, name="ARTICULOS_ALL"),
        path('contacto/', views.contacto, name="CONTACTO"),
        path('sobre-mi/', views.sobre_mi, name="SOBRE-MI"),
        path('admin/', views.administrador, name="ADMIN"),
]

if settings.DEBUG:                                                        # 🠶 01

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
