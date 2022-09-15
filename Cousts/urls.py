from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home,name='home'),
    # path('', views.HomeView.as_view()),
    path('',views.all_cousts,name='all_cousts'),
    path('cousts/', views.cousts, name='cousts'),
    path('cousts/add/', views.add, name='add'),
    path('cousts/add/addrecord/', views.addrecord, name='addrecord'),
    path('cousts/delete/<int:id>', views.delete, name='delete'),
    path('cousts/update/<int:id>', views.update, name='update'),
    path('cousts/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('searchform/', views.search_form, name='search_forms'),
    path('searchmin/', views.search_min, name='search_min'),
    path('search_res/', views.search_res, name='search_res'),
    path('search_rep/', views.search_rep, name='search_rep'),
    ]
