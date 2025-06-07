from django.shortcuts import render
from orders.models import Orders
from django.http import HttpResponse, JsonResponse
from users.decorators import role_required

# Create your views here.
@role_required('printer', 'gluer', 'director')
def work(request):
    if request.method == 'POST':
        orders = Orders.objects.all()
        if request.user.role == 'printer':
            for order in orders:
                print(order.status)
                if order.status == 'paid':
                    order.printer = request.user
                    order.save()
                    return render(request, 'work/include/order.html', {'order': order})
            return HttpResponse('<h3>Заказов больше нет</h3>')
        if request.user.role == 'gluer':
            for order in orders:
                print(order.status)
                print(order.rhinestones)
                if order.status == 'printing' and order.rhinestones:
                    order.gluer = request.user
                    order.save()
                    return render(request, 'work/include/gluer.html', {'order': order})

    return render(request, 'work/work.html')

def endprint(request, order_id):
    order = Orders.objects.get(id=order_id)
    if order.status == 'paid':
        order.status = 'printing'
    if order.status == 'printing':
        order.status = 'gluing'
    order.save()
    return JsonResponse({'status': 'succes'})
