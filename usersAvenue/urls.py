from django.urls import path
from . import views

urlpatterns = [
    path('adminUser/', views.adminUser, name='adminUser'),
    path('orderCustomer/', views.orderCustomer, name='orderCustomer'),
    path('profileUser/', views.profileUser, name='profileUser'),
    path('profAccount/', views.profAccount, name='profAccount'),
]