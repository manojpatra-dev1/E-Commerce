from django.shortcuts import render,redirect, get_object_or_404

from shop.models import Product

# Create your views here.

# =========================
# ADD TO CART
# =========================

def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    # PRODUCT ALREADY EXISTS
    if product_id in cart:

        # MAXIMUM 5 ITEMS
        if cart[product_id]['quantity'] < 5:

            cart[product_id]['quantity'] += 1

    # NEW PRODUCT
    else:

        cart[product_id] = {

            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'image': product.image.url

        }

    request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER'))


# =========================
# REMOVE FROM CART
# =========================

def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        if cart[product_id]['quantity'] > 1:

            cart[product_id]['quantity'] -= 1

        else:

            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


# =========================
# CLEAR CART
# =========================

def clear_cart(request):

    request.session['cart'] = {}

    return redirect('cart')


# =========================
# CART VIEW
# =========================
def cart_view(request):

    cart = request.session.get('cart', {})

    ids = list(cart.keys())

    products = Product.objects.filter(id__in=ids)

    return render(request, 'cart.html', {

        'products': products

    })


# =========================
# PRODUCT DETAIL
# =========================

def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(request, 'product_detail.html', {
        'product': product
    })


# =========================
# CHECKOUT
# =========================

def checkout(request):

    cart = request.session.get('cart', {})

    ids = list(cart.keys())

    ids = [int(i) for i in ids]

    products = Product.get_products_by_id(ids)

    return render(request, 'checkout.html', {
        'products': products,
        'cart': cart
    })

