from django.urls import path
from . import views

from django.conf import settings #para mostrar la media
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('compras',views.compra_h,name='compras'),
    path('compras/create',views.create_compra,name='create'),
    path('hojas',views.hojas,name='hojas'),
    path('hojas/crear',views.crear_hoja,name='crear'),
    path('hojas/editar',views.editar_hoja,name='editar'),
    path('eliminar/<int:id>',views.eliminar_hoja,name='eliminar'),
    path('editar/<int:id>',views.editar_hoja,name='editar')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)