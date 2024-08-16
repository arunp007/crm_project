from django.urls import path
from.import views

urlpatterns = [
    path('admin_login/', views.admin_login, name = 'admin_login'),
    path('admin_signup/', views.admin_signup, name = 'admin_signup'),
    path('customer_login/', views.customer_login, name = 'customer_login'),
    path('customer_signup/', views.customer_signup, name = 'customer_signup'),
    path('technician_login/', views.technician_login, name = 'technician_login'),
    path('technician_signup/', views.technician_signup, name = 'technician_signup'),
]