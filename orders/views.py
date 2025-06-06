import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import OrderCreateForm
from django.urls import reverse
from .models import Orders

# Create your views here.
def home(request):
    orders = Orders.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Orders.objects.get(id=data.get('id'))
        order.status = data.get('status')
        order.save()
    return render(request, 'home.html', {'orders': orders})


def create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print('post')
        if form.is_valid():
            print('valid success')
            form.save()
            return redirect(reverse('home'))
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'form': form})