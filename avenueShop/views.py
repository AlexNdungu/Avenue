from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Movies
from .forms import MoviesForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticaited_user, allowed_users, admin_only
from usersAvenue.models import Customer, Order

# Create your views here.

def index(request):
    return render(request, 'index.html')

@unauthenticaited_user
def log(request):   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username ,password=password)

        if user is not None:
            login(request, user)
            return redirect('createMovie')

        else:
            messages.info(request, 'Username Or Password is incorrect')    
            return render(request, 'log.html')

    context = {}
    return render(request, 'log.html', context)

def logoutUser(request):
    logout(request)
    return redirect('log')    

@unauthenticaited_user
def sign(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
 
            messages.success(request, 'Account Created For '+username)
            return redirect('log')
    
    context = {'form':form}    
    return render(request, 'sign.html', context)

@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def admin(request):
    return render(request, 'admin/admin.html')

@login_required(login_url='log')
def movieview(request):
    movies = Movies.objects.all()

    return render(request, 'admin/movieview.html', {'movies':movies})   

class MovieDetailView(DetailView):

    model = Movies
    template_name = 'admin/moviedetail.html'   
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mov = Movies.objects.get(pk=self.kwargs.get('pk'))

        return context


@login_required(login_url='log')
def movieresult(request):

    if request.method == 'GET':
        search = request.GET.get('search')
        series = Movies.objects.all().filter(movie=search)
        return render(request, 'admin/resultsearch.html',{'series':series})     

@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def deletemov(request, pk):
    mov = Movies.objects.get(movie=pk)
    if request.method == 'POST':
        mov.delete()
        return redirect('movieview')
    context = {'item':mov}
    return render(request, 'admin/deletemov.html',context)

@login_required(login_url='log')
@admin_only
def createMovie(request):
    form = MoviesForm()
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movieview')

    context = {'form':form}
    return render(request, 'admin/addmov.html',context)    

@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def requestMovie(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    pending = orders.filter(status='Incomplete').count()
    accomplished = orders.filter(status='Complete').count()

    context = {'total_orders':total_orders, 'pending':pending, 'accomplished':accomplished,'orders':orders}

    return render(request, 'admin/requests.html',context)

@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def viewUsers(request):

    customers = Customer.objects.all()
    customer_number = customers.count()

    context = {'customers':customers,'customer_number':customer_number}
    return render(request, 'admin/usersAdm.html',context)    

class ViewSpecifiUser(DetailView):

    model = Customer
    template_name = 'admin/specificUser.html'    
    context_object_name = 'regular'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customers = Customer.objects.get(pk=self.kwargs.get('pk'))

        return context

def admProfile(request):
    return render(request,'admin/profileAdm.html' )