from django.db.models import Count, Sum
from .models import Orders

def generate_director_report(start_date, end_date):
    if start_date and end_date:
        orders = Orders.objects.filter(
            status='done',
            created_at__range=(start_date, end_date)
        )
    else:
        orders = Orders.objects.filter(status='done')

    total_orders = orders.count()
    total_revenue = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0

    managers_stats = orders.values(
        'manager__id', 'manager__first_name', 'manager__last_name'
    ).annotate(
        total_orders=Count('id'),
        total_revenue=Sum('total_price')
    ).order_by('-total_orders')

    printers_stats = orders.exclude(printer__isnull=True).values(
        'printer__id', 'printer__first_name', 'printer__last_name'
    ).annotate(
        total_orders=Count('id'),
    ).order_by('-total_orders')

    gluers_stats = orders.exclude(gluer__isnull=True).filter(rhinestones=True).values(
        'gluer__id', 'gluer__first_name', 'gluer__last_name'
    ).annotate(
        total_orders=Count('id'),
        total_rhinestones=Sum('count_rhinestones')
    ).order_by('-total_orders')

    packers_stats = orders.exclude(packer__isnull=True).values(
        'packer__id', 'packer__first_name', 'packer__last_name'
    ).annotate(
        total_orders=Count('id'),
    ).order_by('-total_orders')

    report = {
        'period': f'{start_date} - {end_date}',
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'managers': list(managers_stats),
        'printers': list(printers_stats),
        'gluers': list(gluers_stats),
        'packers': list(packers_stats),
    }

    return report