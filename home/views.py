from django.shortcuts import render, get_object_or_404, redirect
# from django.template import render_to_response
# from django.template import RequestContext
from django.http import JsonResponse
from .models import *
from django.http import JsonResponse
from . import datamakker
import json


# Create your views here.
# all things are handle by context renaring so gfoh(get the **** out of here )

# {{{


def contactus(request):
    return render(request, 'contectus.html')


def favorite(request):
    return render(request, 'favorite.html')


def complate(request):
    print("paymant has been recesived sucessfully")
    return render(request, 'complate.html')


def payment(request):
    return render(request, 'payment.html')


def home(request): #randaring page
    return render(request, 'home.html')

# https://stackoverflow.com/questions/15998140/how-to-limit-a-view-to-superuser-only


def status(request,orderid):
    order = Order.objects.get(id=orderid)
    date = order.expectedtime
    ctx = {"status":order.status,"id":order.id,"date":date}
    return render(request, 'status.html',ctx)


def about(request):
    return render(request, 'aboutus.html')


def carts(request):
    return render(request, 'cart.html')


def checkout(request):

    return render(request, 'checkout.html')


# }}}


#data getting and priting
def get_data(request):  # {{{
    a = datamakker.UserCount()
    return JsonResponse(a)


def get_cat_data(request):
    b= datamakker.ProfitCount()
    return JsonResponse(b)  # }}}


def profile(request):  #{{{
    if request.method == 'POST':
        if 'update' in request.POST:
            customer = request.user.customer

            fullname = request.POST.get('fullName')
            country = request.POST.get('country')
            address = request.POST.get('address')
            phoneno = request.POST.get('phone')

            customer.name = fullname
            customer.state = country
            customer.address = address
            customer.phoneno = phoneno
            customer.save()

            return redirect('/profile')

    return render(request, 'profile.html')  # }}}




def updateItem(request):  # {{{
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(pid=productId)
    order, created = Order.objects.get_or_create(customer=customer,
                                                 complate=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,
                                                         product=product)

    if action == "add":
        orderItem.quantity += 1
        orderItem.save()
    elif action == "remove":
        orderItem.quantity -= 1
        orderItem.save()
    elif action == "delete":
        orderItem.delete()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("item was added", safe=False)  # }}}


def details(request, product_id):
    product = get_object_or_404(Product, pid=product_id)
    ctx = {"product": product}
    return render(request, 'details.html', ctx)


def updateFav(request):  # {{{
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']


    customer = request.user.customer
    product = Product.objects.get(pid=productId)

    favorite, created = Wishlist.objects.get_or_create(customer=customer)
    favoriteItem, created = WishlistItem.objects.get_or_create(
        product=product, wishlists=favorite)

    if action == "add":
        favoriteItem.save()
    elif action == "delete":
        favoriteItem.delete()

    return JsonResponse("item was added", safe=False)  # }}}


def search(request):
    if request.method == "POST":
        query = request.POST.get("search")
        products = Product.objects.filter(tname__icontains=query)
        if len(products) == 0:
            return redirect("/")
        ctx = {"products": products, "query": query}
        return render(request, 'search.html',ctx)

# def handler404(request,*args,**kwargs):
    # response = render_to_response('404.html',{},context_instance=RequestContext(request))
    # response.code = 404
    # return response
