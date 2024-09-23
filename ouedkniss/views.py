from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# CRUD

def createUser(data):
    print('user')
    user = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
    
    return user

def Home(request):
    # R
    
    msg = 'you are not logged in'
    islogged = False
    clients = Client.objects.all()
    print(request.user)
    if request.user.is_authenticated:
        islogged = True
        msg = 'Welcome, ' + request.user.username
    context={
        'clients': clients,
        'msg':msg,
        'islogged':islogged
    }
    return render(request, 'home.html', context)


def createClient(request):
    # C
    print('user')
    
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        data = {'username': name, 'password':password, 'email':email}
        user_id = createUser(data)
        Client.objects.create(user=user_id, phone_number=phone)
        return redirect(Home)

def createSeller(request):
    # C
    print('user')
    
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        address = request.POST['address']
        data = {'username': name, 'password':password, 'email':email}
        user_id = createUser(data)
        Seller.objects.create(user=user_id, phone_number=phone, address=address)
        return redirect(Home)

def ProductView(request):
    seller = Seller.objects.get(user=request.user)
    if request.method == 'GET':
        products = Product.objects.filter(owner=seller)
        context={'products': products}
        return render(request, 'product.html', context)
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        description = request.POST['desc']
        Product.objects.create(
            title=title,
            price=price,
            description=description,
            owner=seller
        )
        return redirect(ProductView)

def cartView(request):
    orders = Order.objects.filter(client=Client.objects.get(user=request.user).id)
    context = {
        'orders': orders
    }
    return render(request, 'cart.html', context)
def catalogView(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog.html', context)

def orderView(request, productid, status):

    client = Client.objects.get(user=request.user)

    product = Product.objects.get(id=productid)
    order = Order.objects.create(client=client, product=product, status=status)
    print(order)
    return redirect(cartView)

def confirmOrder(request, status, orderid):
    order = Order.objects.get(id=orderid)
    order.status = status
    order.save()
    return redirect(cartView)
  
def deleteClient(request, id):
    # D
    Client.objects.get(id=id).delete()
    return redirect(Home)


def updatePage(request, id):
    if request.method == 'GET':
        client = Client.objects.get(id=id)

        context = {
            'client': client,
            
        }
        return render(request, 'update.html', context)
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['number']
        email = request.POST['email']

        client = Client.objects.get(id=id)
        client.email = email
        client.name = name
        client.phone_number = phone
        client.save()
        return redirect(Home)
    

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(Home)
    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect(Home)