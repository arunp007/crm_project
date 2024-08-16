from django.urls import path
from.import views

urlpatterns = [
    path('home/<str:uid>/', views.home, name = 'technician_home'),
    path('logout/', views.technician_logout, name = 'technician_logout'),
    path('profile/<str:uid>/', views.technician_profile, name = 'technician_profile'),
    path('profile/delete/<str:uid>/', views.delete_profile, name = 'delete_technician'),
    path('complaints/<str:uid>/', views.complaints, name = 'technician_complaint'),
    path('complaints/create/<int:complaint_id>/', views.add_complaint, name = 'creating_complaint'),
    path('delete_complaint_bill/<int:billing_id>/', views.delete_complaint_bill, name = 'delete_complaint_bill'),
    path('receipt/<int:complaint_id>/', views.receipt, name = 'receipt'),
    path('sales_orders/<str:uid>/', views.sales_order, name = 'technician_sales_order'),
    path('sales_orders/create/<str:uid>/', views.add_sales_order, name = 'creating_sales_order'),
    path('delete_bill/<str:uid>/', views.delete_bill, name = 'technician_delete_bill'),
    path('receipts/<str:uid>/', views.receipt, name = 'technician_receipt'),
]