from django.urls import path

from . import views

urlpatterns=[
    path('', views.home, name=''),
    path('logout', views.logout_user, name='logout'),
    path('api', views.api, name='api'),
    path('<slug>',views.account),
    
]