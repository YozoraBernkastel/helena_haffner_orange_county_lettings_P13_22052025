from django.urls import path

import profiles.views as views

urlpatterns = [
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]
