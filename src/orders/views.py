from django.shortcuts import render
from django.views.generic import ListView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import Order
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrderListView(View,LoginRequiredMixin):
    def get(self,request):
        orders = Order.objects.all()
        return render(request,'orders/order_list.html',{'orders':orders})
