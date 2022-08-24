from django.contrib import admin
from django.urls import path

from registros import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.home, name="Home"),
    path('catalogo/',views.catalogo, name="Catalogo"),
    path('opiniones/',views.opiniones, name="Opinion"),
    path("edita/<int:id>/",views.editar, name="Editar"),
    path("elim/<int:id>/",views.eliminar, name="Eliminar"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)