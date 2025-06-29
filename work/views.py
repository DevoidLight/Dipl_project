from django.shortcuts import render
from orders.models import Orders
from django.http import HttpResponse, JsonResponse
from users.decorators import role_required

# Create your views here.
@role_required('printer', 'gluer', 'packer')
def work(request):
    if request.method == 'POST':
        orders = Orders.objects.all()
        if request.user.role == 'printer':
            for order in orders:
                print(order.status)
                if order.status == 'paid':
                    order.printer = request.user
                    order.status = 'printing'
                    order.save()
                    return render(request, 'work/include/order.html', {'order': order})
            
        if request.user.role == 'gluer':
            for order in orders:
                if order.status == 'gluing' and order.rhinestones:
                    order.gluer = request.user
                    order.save()
                    return render(request, 'work/include/gluer.html', {'order': order})
        if request.user.role == 'packer':
            for order in orders:
                if order.status == 'packing':
                    order.packer = request.user
                    order.save()
                    return render(request, 'work/include/packer.html', {'order': order})
        return HttpResponse('<h3>Заказов больше нет</h3>')
    if request.user.role == 'printer':
        orders_count = Orders.objects.filter(status='paid').count()
        context = {'orders_count': orders_count}
    if request.user.role == 'gluer':
        orders_count = Orders.objects.filter(status='gluing').count()
        context = {'orders_count': orders_count}
    if request.user.role == 'packer':
        orders_count = Orders.objects.filter(status='packing').count()
        context = {'orders_count': orders_count}
    return render(request, 'work/work.html', context)

def endprint(request, order_id):
    order = Orders.objects.get(id=order_id)
    if order.status  == 'packer':
        order.status = 'done'
    if order.status == 'gluind':
        order.status = 'packer'
    if order.status == 'printing':
        ribbon = order.ribbon
        ribbon.length = ribbon.length - (order.count * 2)
        paint = order.paint
        paint.length = paint.length - (order.count * 2)
        ribbon.save()
        paint.save()
        if order.rhinestones:
            order.status = 'gluing'
        else:
            order.status = 'packer'
    order.save()
    return JsonResponse({'status': 'succes'})
