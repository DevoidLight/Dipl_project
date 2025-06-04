from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html')


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