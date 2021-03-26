from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('login/', views.log, name='log' ),
    path('logout/', views.logoutUser, name='logout' ),
    path('signin/', views.sign, name = 'sign' ),
    path('admime/', views.admin, name = 'admin' ),
    path('createMovie/', views.createMovie, name= 'createMovie' ),
    path('movieview/', views.movieview, name= 'movieview' ),
    path('movieresult/', views.movieresult, name= 'movieresult' ),
    path('deletemov/<str:pk>/', views.deletemov, name= 'deletemov' ),
    path('moviedetail/<str:pk>/', views.MovieDetailView.as_view(), name= 'moviedetail' ),
    path('requestMovie/', views.requestMovie, name= 'requestMovie' ),
    path('viewUsers/', views.viewUsers, name= 'viewUsers' ),
    path('userDetails/<str:pk>/', views.ViewSpecifiUser.as_view(), name= 'userDetails' ),
    path('admProfile/', views.admProfile, name= 'admProfile' ),
]