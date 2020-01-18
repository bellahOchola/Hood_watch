from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('hood/', views.hood, name='hood'),
    path('single_hood/<id>', views.single_hood, name='single_hood'),
    path('create-business/<id>', views.create_business, name='create_business'),
    path('search/', views.search_business, name= 'search'),
]