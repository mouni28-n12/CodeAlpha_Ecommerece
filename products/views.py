from django.shortcuts import render, redirect
from .models import Product


def product_list(request):
    query = request.GET.get('q', '')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):
        cart = {}

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def cart(request):
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):
        cart = {}

    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        quantity = cart.get(str(product.id), 0)
        item_total = product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

        total += item_total

    return render(
        request,
        'products/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):
        cart = {}

    product_id = str(product_id)

    cart[product_id] = cart.get(product_id, 0) + 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):
        cart = {}

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] -= 1

        if cart[product_id] <= 0:
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):
        cart = {}

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def checkout(request):
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):
        cart = {}

    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        quantity = cart.get(str(product.id), 0)
        item_total = product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

        total += item_total

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        request.session['cart'] = {}

        return render(
            request,
            'products/order_success.html',
            {
                'name': name,
                'email': email,
                'address': address,
                'total': total
            }
        )

    return render(
        request,
        'products/checkout.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )