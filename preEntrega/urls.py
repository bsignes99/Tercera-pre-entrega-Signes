"""
URL configuration for preEntrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pawPatrol.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", inicio, name= "inicio"),
    
    path("heroes/", heroes, name= "heroes"),
    path("villanos/", villanos, name= "villanos"),
    path("vehiculos/", vehiculos, name= "vehiculos"),
    
    path("comencemos/", comencemos, name= "comencemos"),
    path("padre/", padre),
    path("padre/", padre),
    path("heroes/formheroe/", agregarHeroe, name= "formheroe"),
    path("villanos/formheroe/", agregarVillano, name= "formvillano"),
    path("vehiculos/formvehiculo/", agregarVehiculo, name= "formvehiculo"),
    path("vehiculos/vehiculossig/", vehiculodos, name= "vehiculodos"),
    path("heroes/heroessig/", heroesdos, name= "heroesdos"),
    path("heroes/heroessig/buscar", buscarheroe, name= "buscar"),



    path('imagenes/', imagenes),
    path("resultados/", resultados),



    

]
