from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Ribbons, Paints
from .forms import RibbonsCreate, PaintsCreate, TemplatesCreate
from users.decorators import role_required
# Create your views here.

@role_required('director')
def products(request):
    ribbons = Ribbons.objects.all()
    paints = Paints.objects.all()
    context = {
        'ribbons': ribbons,
        'paints': paints
    }
    return render(request, 'products/products.html', context)

@role_required('director')
def ribbon_create(request):
    if request.method == 'POST':
        form = RibbonsCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('orders'))
    else:
        form = RibbonsCreate()
    return render(request, 'products/ribbon_create.html', {'form': form})

@role_required('director')
def paint_create(request):
    if request.method == 'POST':
        form = PaintsCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('orders'))
    else:
        form = PaintsCreate()
    return render(request, 'products/paint_create.html', {'form': form})

@role_required('director')
def template_create(request):
    if request.method == 'POST':
        form = TemplatesCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('orders'))
    else:
        form = TemplatesCreate()
    return render(request, 'products/template_create.html', {'form': form}) 