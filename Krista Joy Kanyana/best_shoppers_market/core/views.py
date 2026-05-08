from django.shortcuts import render
from .forms import ProductForm
from .models import Product


def landing(request):
    return render(request, 'index.html')


def onlandform(request):
    products = Product.objects.all().order_by('-id')
    success  = False

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success  = True
            products = Product.objects.all().order_by('-id')
            form     = ProductForm()
    else:
        form = ProductForm()

    return render(request, 'onlandform.html', {
        'form':     form,
        'products': products,
        'success':  success,
    })
