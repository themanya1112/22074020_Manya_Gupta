from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('redirect/<str:short_code>/', views.redirect_original, name='redirect_original'),
    path('list/', views.short_url_list, name='short_url_list'),
]
