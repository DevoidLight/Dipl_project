import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import OrderCreateForm
from django.urls import reverse
from .models import Orders
from users.decorators import role_required
from .reports import generate_director_report

# Create your views here.
def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('login'))
    if user.role in ('printer', 'gluer', 'packer'):
        return redirect(reverse('work'))
    if user.role in ('manager', 'director'):
        return redirect(reverse('orders'))
    
@role_required('director')
def director_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        report_data = generate_director_report(start_date, end_date)
    else:
        report_data = generate_director_report(None, None)
    
    return render(request, 'order/director_report.html', report_data)

@role_required('manager', 'director')
def orders(request):
    orders = Orders.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Orders.objects.get(id=data.get('id'))
        order.status = 'paid'
        order.save()
    return render(request, 'order/orders.html', {'orders': orders})

@role_required('manager', 'director')
def create(request):
    if request.method == 'POST':
        form = OrderCreateForm(data=request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.manager = request.user
            order.save()
            return redirect(reverse('home'))
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'form': form})