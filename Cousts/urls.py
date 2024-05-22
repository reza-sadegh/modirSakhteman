from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.search_min_rep,name='home'),
    # path('', views.HomeView.as_view()),
    path('',views.all_cousts,name='all_cousts'),
    path('cousts/', views.cousts, name='cousts'),
    path('cousts/add/', views.add, name='add'),
    path('cousts/add/addrecord/', views.addrecord, name='addrecord'),
    path('cousts/delete/<int:id>', views.delete, name='delete'),
    path('cousts/update/<int:id>', views.update, name='update'),
    path('cousts/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('search_form/', views.search_form, name='search_form'),
    path('search_min/', views.search_min, name='search_min'),
    path('search_res/', views.search_res, name='search_res'),
    path('search_rep/', views.search_rep, name='search_rep'),
    ]
