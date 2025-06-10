from .models import Orders
from django.db.models import Sum

def generate_director_report(start_date, end_date):

    orders = Orders.objects.filter(
        status='done',
        created_at__range=(start_date, end_date)
    )

    total_orders = orders.count()
    total_revenue = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0

    return {
        'period': f'{start_date} - {end_date}',
        'total_orders': total_orders,
        'total_revenue': total_revenue,
    }

