from django.urls import path

import lettings.views as views

urlpatterns = [
    path('lettings/', views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
