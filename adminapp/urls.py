from django.urls import path
from.import views

urlpatterns = [
    path('home/<str:uid>/', views.home, name = 'admin_home'),
    path('logout/', views.admin_logout, name = 'admin_logout'),
    path('customers/<str:uid>/', views.customers, name = 'customers'),
    path('customers/add_customers/<str:uid>/', views.add_customers, name = 'add_customers'),
    path('technicians/<str:uid>/', views.technicians, name = 'technicians'),
    path('technicians/create/<str:uid>/', views.add_technicians, name = 'add_technicians'),
    path('profile/<str:uid>/', views.admin_profile, name = 'admin_profile'),
    path('profile/delete/<str:uid>/', views.delete_admin, name = 'delete_admin'),
    path('sales_orders/<str:uid>/', views.sales_orders, name = 'sales_orders'),
    path('sales_orders/create/<str:uid>/', views.add_sales_order, name = 'add_sales_order'),
    path('delete_bills/<str:uid>/', views.delete_bills, name = 'delete_bills'),
    path('complaints/<str:uid>/', views.complaint, name = 'complaint'),
    path('complaints/create/<int:complaint_id>/', views.add_complaint, name = 'add_complaint'),
    path('receipt_report/<str:uid>/', views.receipt_report, name = 'receipt_report'),
]