"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ouedkniss import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('createClient/', views.createClient),
    path('login/', views.loginView),
    path('logout/', views.logoutView),
    path('delete/<int:id>/', views.deleteClient),
    path('update/<int:id>/', views.updatePage),
    path('products/', views.ProductView),
    path('cart/', views.cartView),
    path('catalog/', views.catalogView),
    path('createOrder/<int:productid>/<str:status>/', views.orderView),
    path('confirmOrder/<int:orderid>/<str:status>/', views.confirmOrder),
]
