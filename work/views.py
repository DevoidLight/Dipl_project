from django.shortcuts import render
from orders.models import Orders
from django.http import HttpResponse

# Create your views here.
def work(request):
    if request.method == 'POST':
        orders = Orders.objects.all()
        for order in orders:
            if order.status == 'Оплачено':
                print('Заказ найден')
                return render(request, 'work/include/order.html', {'order': order})
            else:
                return HttpResponse('<h3>Заказов больше нет</h3>')
    return render(request, 'work/work.html')