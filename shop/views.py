from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from requests import request

from .models import Product
from .category import Category
from .models import Customer

from django.contrib.auth.hashers import make_password, check_password
import re


# =========================
# HOME PAGE
# =========================


def home(request):

    categories = Category.objects.all()

    # CATEGORY FILTER

    categoryID = request.GET.get('category')

    if categoryID:

        products = Product.get_all_products_by_categoryid(categoryID)

    else:

        products = Product.objects.all()

    # SEARCH FILTER

    search = request.GET.get('search')

    if search:

        products = products.filter(name__icontains=search)

    data = {

        'products': products,
        'categories': categories

    }

    return render(request, 'index.html', data)


# =========================
# SIGNUP VIEW
# =========================

def signup_view(request):

    if request.method == 'GET':
        return render(request, 'signup.html')

    #  POST data
    fname = request.POST.get('fname', '').strip()
    lname = request.POST.get('lname', '').strip()
    email = request.POST.get('email', '').strip()
    mobile = request.POST.get('mobile', '').strip()
    password = request.POST.get('password', '').strip()
    confirm_password = request.POST.get('confirm_password', '').strip()

    context = {
        'value': {
            'first_name': fname,
            'last_name': lname,
            'email': email,
            'mobile': mobile,
        }
    }

    # =========================
    #  VALIDATION LOGIC
    # =========================

    if not fname:
        context['error'] = 'First name is required'

    elif not lname:
        context['error'] = 'Last name is required'

    elif not email:
        context['error'] = 'Email is required'

    elif not mobile:
        context['error'] = 'Mobile number is required'

    elif not password:
        context['error'] = 'Password is required'

    elif not confirm_password:
        context['error'] = 'Please confirm your password'

    elif password != confirm_password:
        context['error'] = 'Passwords do not match'

    #  Password rules
    elif len(password) < 8:
        context['error'] = 'Password must be at least 8 characters long'

    elif not re.search(r'\d', password):
        context['error'] = 'Password must contain at least one number'

    elif not re.search(r'[!@#$%^&*]', password):
        context['error'] = 'Password must contain at least one special character'

    elif not re.search(r'[A-Z]', password):
        context['error'] = 'Password must contain at least one uppercase letter'

    elif not re.search(r'[a-z]', password):
        context['error'] = 'Password must contain at least one lowercase letter'

    #  Duplicate checks
    elif Customer.objects.filter(email=email).exists():
        context['error'] = 'Email already registered'

    elif Customer.objects.filter(mobile=mobile).exists():
        context['error'] = 'Mobile number already registered'

    # =========================
    #  SAVE USER
    # =========================
    else:
        Customer.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            mobile=mobile,
            password=make_password(password)  # 🔐 IMPORTANT
        )

        return redirect('/login')  # better UX

    return render(request, 'signup.html', context)

# =========================
# LOGIN VIEW
# =========================

def login_view(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    else:

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            users = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            users = None

        error_msg = None

        if users:

            check = check_password(password, users.password)

            if check:

                request.session['customer_id'] = users.id

                return redirect('/')

            else:
                error_msg = "Password is incorrect"

        else:
            error_msg = "Email is incorrect"

        return render(request, 'login.html', {
            'error': error_msg
        })


# =========================
# LOGOUT VIEW
# =========================

def logout_view(request):

    request.session.clear()

    return redirect('/login')


