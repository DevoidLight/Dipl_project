import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .forms import OrderCreateForm
from django.urls import reverse
from .models import Orders
from users.decorators import role_required
from .reports import generate_director_report
from django.template.loader import render_to_string

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
        return JsonResponse({'status': 'success'})

    status_filter = request.GET.get('status')
    
    if status_filter:
        if status_filter != 'all':
            orders = Orders.objects.filter(status=status_filter)
        return render(request, 'order/include/orders_filter.html', {'orders': orders})
    
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

@role_required('director', 'manager')
def order_edit(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    if request.method == 'POST':
        form = OrderCreateForm(data=request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderCreateForm(instance=order)
    return render(request, 'order/edit.html', {'form': form})


@role_required('director', 'manager')
def order_delete(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    order.delete()
    return redirect('orders')