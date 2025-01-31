from django.urls import path

from superstore.views import CustomerDetailView, CustomerListSearchView, CustomerListView



urlpatterns = [
    path('', CustomerListView.as_view()),
    path('<str:name>', CustomerListSearchView.as_view()),
    path('customer/<int:pk>', CustomerDetailView.as_view()),
]
