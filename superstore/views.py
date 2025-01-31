from django.utils import timezone
# from time import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Customer
# Create your views here.

class CustomerListView(ListView):
    model = Customer
    template_name = "superstore/liste.html"

    paginate_by = 3

class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get('name')
        return Customer.objects.filter(first_name__icontains=name)
    
class CustomerDetailView(DetailView):
    model = Customer
    template_name = "superstore/detail.html"

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        return obj