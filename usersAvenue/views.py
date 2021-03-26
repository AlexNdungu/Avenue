from django.shortcuts import render, redirect
from .forms import OrderForm, AccountForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from avenueShop.decorators import unauthenticaited_user, allowed_users, admin_only
from .models import Customer
# Create your views here.

@login_required(login_url='log')
@allowed_users(allowed_roles=['customer'])
def adminUser(request):
    return render(request, 'user/adminuser.html')   
    
@login_required(login_url='log')
@allowed_users(allowed_roles=['customer'])
def orderCustomer(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = request.user
            new_order.save()
            return redirect('movieview')
            
    context = {'form':form}
    return render(request, 'user/order.html',context)  
    
@login_required(login_url='log')
@allowed_users(allowed_roles=['customer'])
def profileUser(request):

    context = {}
    return render(request, 'user/profileUser.html', context)      

@login_required(login_url='log')
@allowed_users(allowed_roles=['customer'])
def profAccount(request):

    customer = request.user.customer
    form = AccountForm(instance=customer)

    if request.method == 'POST':
        form = AccountForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'user/profUserSet.html',context)    