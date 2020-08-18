from django.shortcuts import render, redirect
from shop.models import Product, Contact, Subscribers, ProductImgae, Order, OrderItem, Customer
from math import ceil
from django.forms import modelformset_factory
from .forms import ContactForm, SubscriberForm,CheckoutForm,PaymentForm,HelpForm,CustomerForm
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .filters import ProductFilter
from django.db.models import Q

def index(request):
    all_products = []
    category_pro = Product.objects.values('category', 'id')
    cats = {i['category'] for i in category_pro}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        all_products.append([prod, range(1, nslides), nslides])

    if request.user.is_authenticated:
        # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
            customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''

    parm = {'all_products': all_products,
            'cart_items':cart_items}
    return render(request, 'shop/index.html', parm)

def searchmatch(query, item):
    # return tru if query matches the query
    if query in item.decs.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    all_products = []
    category_pro = Product.objects.values('category', 'id')
    cats = {i['category'] for i in category_pro}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchmatch(query, item)]

        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        if len(prod) != 0:
            all_products.append([prod, range(1, nslides), nslides])

    parm = {'all_products': all_products, 'msg': ""}
    if len(all_products) == 0:
        parm = {'msg': "relevant data not found "}
    return render(request, 'shop/search.html', parm)


def contact(request):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    param = {'form': form,'cart_items':cart_items}
    return render(request, 'shop/contact.html', param)


def base(request):

    products = Product.objects.all()
    Sub_form = SubscriberForm(request.POST or None)
    if Sub_form.is_valid():
        Sub_form.save()
        return redirect('home')
    parm = {"products": products, 'Sub': Sub_form}
    return render(request, 'shop/base.html', parm)

def cart(request):
    customer = Customer.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cart_items = order.get_cart_items
    template = 'shop/cart.html'
    context = {
        'order': order,
        'items': items,
        'cart_items': cart_items,
    }
    return render(request, template, context)

def productview(request, id):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''
    data = Product.objects.get(id=id)
    data_img = data.productimgae_set.all()

    all_products = []
    category_pro = Product.objects.values('category', 'id')
    cats = {i['category'] for i in category_pro}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        all_products.append([prod, range(1, nslides), nslides])

    product = Product.objects.filter(id=id)
    parm = {'product': product[0],
            'all_products': all_products, "img": data_img,'cart_items':cart_items}

    return render(request, 'shop/products.html', parm)



@login_required
def Checkout(request):
    order, created = Order.objects.get_or_create(customer= request.user.customer, complete=False)
    items = order.orderitem_set.all()
    cart_items = order.get_cart_items

    form = CheckoutForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data['email']
        form.save()
        print(email)
        send_mail(
            "Come&buy",
            "An order has been placed using you email",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
        messages.success(request," confirmation email has been send ")
        return redirect('payment')
    context = {
        'order': order,
        'items': items,
        'cart_items': cart_items,
        'form':form
    }
    return render(request, 'shop/Checkout.html', context)

@login_required
def buynow(request):
    order, created = Order.objects.get_or_create(customer= request.user.customer, complete=False)
    items = order.orderitem_set.all()
    cart_items = order.get_cart_items

    form = CheckoutForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data['email']
        form.save()
        print(email)
        send_mail(
            "Come&buy",
            "An order has been placed using you email",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
        messages.success(request," confirmation email has been send ")
        return redirect('payment')
    context = {
        'order': order,
        'items': items,
        'cart_items': cart_items,
        'form':form
    }
    return render(request, 'shop/buynow.html', context)

@login_required
def payment(request):
    order, created = Order.objects.get_or_create(
    customer=request.user.customer, complete=False)
    template = 'shop/payment.html'
    context = {'order': order}

    return render(request, template, context )

def help(request):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''
    form = HelpForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request," your query has been recorded ")
        return redirect('ShopHome')

    param = {'form': form,'cart_items':cart_items}
    return render(request, 'shop/help.html',param)

@login_required()
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(
        order=order, product=product)
    if action == 'add':
        orderitem.quantity = orderitem.quantity + 1
        messages.success(request,product.product_name+' added to cart')
    elif action == 'remove':
        orderitem.quantity = orderitem.quantity - 1
        messages.warning(request,product.product_name+' removed to cart')
    orderitem.save()
    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse('Item added into cart', safe=False)


@login_required()
def processPayment(request):
    messages.success(request, 'your order placed successfully. order will be delivered within 3-5 working days')
    order = Order.objects.get(customer=request.user.customer, complete=False)
    order.complete = True
    order.save()
    # form = PaymentForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    return redirect('ShopHome')
    # param = {'form': form}
    # return render(request, 'shop/payment.html', param)

def home(request):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''
    
    return render(request, 'shop/home.html',{'cart_items':cart_items})


def about(request):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''

    parms = { 'cart_items':cart_items }
    return render(request, 'shop/about.html',parms)


def tracker(request):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''

    parms = { 'cart_items':cart_items }
    return render(request, 'shop/index.html',parms)

def registry(request):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''

    parms = { 'cart_items':cart_items }
    return render(request, 'shop/registry.html',parms)

def sell(request):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''

    parms = { 'cart_items':cart_items }
    return render(request, 'shop/sell.html',parms)


@login_required
def profile(request):
    if request.user.is_authenticated:
    # customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
        customer=request.user.customer, complete=False)
        cart_items = order.get_cart_items
    else:
        cart_items = ''

    parms = { 'cart_items':cart_items }
    # profile = Customer.objects.all()
    # param={'user':profile}
    return render(request, 'shop/profile.html',parms)

# @login_required
def customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form =CustomerForm(request.POST)
        if form.is_valid():
            user = request.user
            customer = form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('account_login')

    param = {'form': form}
    return render(request, 'shop/customer.html', param)

def filter(request):

    # filters =ProductFilter(request.GET, queryset=Product.objects.all())
    # param={'filters':result}
    
    return render(request, 'shop/filter.html')


