from django.urls import path
from.import views

urlpatterns = [
    path('home/<str:uid>/', views.home, name = 'customer_home'),
    path('logout/', views.customer_logout, name = 'customer_logout'),
    path('profile/<str:uid>/', views.customer_profile, name = 'customer_profile'),
    path('profile/delete/<str:uid>/', views.delete_profile, name = 'delete_profile'),
    path('complaints/create/<str:uid>/', views.create_complaint, name = 'create_complaint'),
    path('complaints/<str:uid>/', views.complaints, name = 'complaints'),
    path('sales_orders/<str:uid>/', views.sales_order, name = 'sales_order'),
    path('sales_orders/create/<str:uid>/', views.create_sales_order, name = 'create_sales_order'),
    path('receipts/<str:uid>/', views.receipt, name = 'customer_receipt'),
]