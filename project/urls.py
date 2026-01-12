from django.contrib import admin
from django.urls import path
from portfolio import views  # ← Isso importa a view do app portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_world),  # ← Isso define a página principal
]
