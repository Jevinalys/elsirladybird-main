from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('book/',views.book, name="book"),
    path('register_user/',views.register_user, name="register_user"),
    path('activate/<uidb64>/<token>',views.VerificationView, name="activate"),
    path('usernameValidation/',views.usernameValidation, name="usernameValidation"),
    path('firstnameValidation/',views.firstnameValidation, name="firstnameValidation"),
    path('secondnameValidation/',views.secondnameValidation, name="secondnameValidation"),
    path('phoneValidation/',views.phoneValidation, name="phoneValidation"),
    path('customerphoneValidation/',views.customerphoneValidation, name="customerphoneValidation"),
    path('emailValidation/',views.emailValidation, name="emailValidation"),
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('sales/',views.sales, name="sales"),
    path('search_sales/',views.search_sales, name="search_sales"),
    path('salesrepo/',views.salesrepo, name="salesrepo"),
    path('export_excel/',views.export_excel, name="export-excel"),
    #path('export_pdf/',views.export_pdf, name="export-pdf"),
    path('bookings/',views.bookings, name="bookings"),
    path('delete_bookings/<str:pk>',views.delete_bookings, name="delete_bookings"),
    path('Inventory/',views.Inventory, name="Inventory"),
    path('customers/',views.customers, name="customers"),
    path('customer_excel/',views.customer_excel, name="customer-excel"),
    path('search_customers/',views.search_customers, name="search_customers"),
    path('addSales/<str:pk>',views.addSales, name="addSales"),
    path('payDebt/<str:pk>',views.payDebt, name="payDebt"),
    path('redeemPoints/<str:pk>',views.redeemPoints, name="redeemPoints"),
    path('addService/',views.addService, name="addService"),
    path('addCustomer/',views.addCustomer, name="addCustomer"),
    path('customer-delete/',views.customer_delete, name="customer-delete"),
    path('service-delete/',views.service_delete, name="service-delete"),
    path('updateCustomer/',views.updateCustomer, name="updateCustomer"),
    path('updateprice/',views.updateprice, name="updateprice"),
    path('updateService/',views.updateService, name="updateService"),
    path('updatetime/',views.updatetime, name="updatetime"),
    path('monthly_servicesales/',views.monthly_servicesales, name="monthly_servicesales"),
    path('monthly_sales_distribution/',views.monthly_sales_distribution, name="monthly_sales_distribution"),
]