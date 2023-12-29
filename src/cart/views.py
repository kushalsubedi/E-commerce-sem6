from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Cart
from Home.models import Product

# Create your views here.


def cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.products.add(product)

        cart.save()

        print(f"Added to cart: {product.name} (ID: {product.id})")
    else:
        print("User is not authenticated. Cannot add to cart.")

    if product in cart.products.all():
        print(f"{product.name} is in cart.")
        return redirect('cart')
    return redirect('home')


def cart(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:  # Catch the Cart.DoesNotExist exception
            cart = None  # Set cart to None when no cart is available

        context = {
            'cart': cart
        }

        return render(request, 'Home/cart.html', context)
    else:
        return render(request, 'Home/404.html', {'status': 404})


def cart_updates(request,pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.products.remove(product)

        cart.save()

        print(f"Added to cart: {product.name} (ID: {product.id})")
    else:
        print("User is not authenticated. Cannot add to cart.")

    if product in cart.products.all():
        print(f"{product.name} is in cart.")
        return redirect('cart')
    return redirect('home')
