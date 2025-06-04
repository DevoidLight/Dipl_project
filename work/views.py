from django.shortcuts import render
from orders.models import Orders

# Create your views here.
def work(request):
    return render(request, 'work/work.html')