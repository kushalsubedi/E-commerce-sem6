from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Product
from .forms import ProductForm, CategoryForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  # for login login_required

# Create your views here.


def home(request):
    user = request.user
    product = Product.objects.all()
    paginator = Paginator(product, 4)
    context = {
        'product': product,
        'user': user,
        'paginator': paginator

    }
    return render(request, 'Home/index.html', context)


@login_required
def create_category(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    form = CategoryForm(request.POST)
    context = {'form': form}
    return render(request, 'Home/create_category.html', context)


@login_required
def create_Product(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            print(form.cleaned_data)
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'Home/create.html', {'form': form})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    context = {'product': product, 'form': form,}
    return render(request, 'Home/product_detail.html', context)


@login_required
def update_product(request, pk):
    if request.user == get_object_or_404(Product, pk=pk).author:
        # or you can Do this if request.user == Product.objects.get(pk=pk).author:
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_detail', pk=product.pk)
            else:
                print(form.errors)

        context = {'form': form}

        return render(request, 'Home/create.html', context)
    else:
        return HttpResponse("<h1> You are not allowed to edit this product </h1>", status=403)


@login_required
def delete_product(request, pk):
    if request.user == Product.objects.get(pk=pk).author:
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect('home')
    else:
        return HttpResponse("<h1> You are not allowed to delete this product </h1>", status=403)



#test 






