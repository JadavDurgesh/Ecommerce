from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .form import *
import razorpay
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    cart_count = Cart.objects.filter(user=request.user.id).count()
    return render(request, 'index.html',{'cart_count':cart_count})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.info(request, f'{username} is successfully register')
            return redirect('signup')
            form = SignupForm()
        return render(request, 'signup.html',{'form':form})            
    else:
        form=SignupForm()
    return render(request, 'signup.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request,'Invalid credentional')
            return redirect('signin')
        else:
            login(request, user)
            messages.info(request, 'successfully login')            
            return redirect('index')
        
    return render(request,'signin.html')

def passwordchange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PassChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, "Password change successfully ")    
                return redirect('login')
        else:
            form = PassChangeForm(user=request.user)
        con={'form':form}
        return render(request, "Password_Change.html", con)
    else:
        messages.info(request, "Please login first")
    return redirect('signin')

def logout_user(request):
    logout(request)
    return redirect('index')

def profile(request):
    cart_count = Cart.objects.filter(user=request.user).count()

    if request.user.is_authenticated:
        form = UserProfileChangeForm(instance=request.user)
        if request.method =='POST':
            form = UserProfileChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                get_user = form.cleaned_data['username']
                messages.info(request, f'{get_user}is successfully updated')
                return redirect('profile')
        else:
            form = UserProfileChangeForm(instance=request.user)
        context = {'form':form,'cart_count':cart_count}
        return render(request, 'profile.html',context)

def address(request):
    cart_count = Cart.objects.filter(user=request.user).count()
    
    all_address = CustomeraddressModel.objects.filter(user=request.user)
    if request.user.is_authenticated:
        form = CustomeraddressForm(instance=request.user)
        if request.method == 'POST':
            form = CustomeraddressForm(request.POST)
            if form.is_valid():
                fm = form.save(commit=False)
                fm.user = request.user
                fm.save()
                messages.info(request,'Address successfully added')
                return redirect('address')
        else:
            form = CustomeraddressForm(instance=request.user)
        context = {'form':form,'all_address':all_address, 'cart_count':cart_count}
    return render(request, 'address.html',context)

def addressupdate(request,id):
    cart_count = Cart.objects.filter(user=request.user).count()

    # address = CustomeraddressModel.objects.all()
    set_address = CustomeraddressModel.objects.get(id=id)
    if request.method == 'POST':
        form = CustomeraddressForm(request.POST, request.FILES, instance=set_address)
        if form.is_valid():
            form.save()
            messages.info(request, 'Address successfully updated')
            return redirect('address')
    else:
        form = CustomeraddressForm(instance=set_address)
    context = {'form':form, 'cart_count':cart_count}
    return render(request, 'address.html', context)

def addressdelete(request,id):
    get_add = CustomeraddressModel.objects.get(id=id) 
    get_add.delete()
    messages.info(request, 'Address deleted')
    return redirect('address')

def singleblog(request):
    return render(request, 'singleblog.html')

def cart(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
        cart_item = Cart.objects.all()

        sub_total = 0
        for i in cart_item:
            sub_total += i.product_total()
    else:
        return redirect('signin')
    context={'cart_count':cart_count,'cart_item':cart_item, 'sub_total':sub_total}
    return render(request, 'cart.html',context) 

def category(request):
    cart_count = Cart.objects.filter(user=request.user.id).count()
    all_category = Categories.objects.all()

    get_cat_id = request.GET.get('catesid')

    if get_cat_id:
        product_by_id = Product.objects.filter(category_id = get_cat_id)
    else:
        product_by_id = Product.objects.all()

    context = {'all_category':all_category, 'cart_count':cart_count, 'product_by_id':product_by_id}
    return render(request, 'category.html',context)

def checkout(request):
    cart_count = Cart.objects.filter(user=request.user).count()
    cart_item = Cart.objects.filter(user=request.user)
    all_address = CustomeraddressModel.objects.filter(user=request.user)

    sub_total = 0
    shipping = 100
    grand_total = 1
    
    get_address_id = request.GET.get('add1')
    print(get_address_id,"4444400000000000000000000000000000000000")
    
    for i in cart_item:
        sub_total += i.product_total()
        grand_total = shipping + sub_total

    amount = grand_total*100
    client = razorpay.Client(auth=("rzp_test_Kp7BqY55rTwOR5", "FwhlkMYgi07NXMfBO0STTiGm"))
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})

    if get_address_id:
        address = CustomeraddressModel.objects.get(id=get_address_id)
        
        for i in cart_item:
            order_data = Order(user=request.user,customer=address,product=i.product,quantity=i.quantity)
            order_data.save()
            cart_item.delete()
            
        return redirect('order')
    
    context = {
    'cart_item':cart_item, 
    'cart_count':cart_count, 
    'sub_total':sub_total, 
    'shipping':shipping, 
    'grand_total':grand_total,
    'all_address':all_address,
    'payment':payment
    }

    return render(request,'checkout.html',context)

def singleproduct(request,id):
    cart_count = Cart.objects.filter(user=request.user.id).count()

    product_detail = Product.objects.get(id=id)
    context={'product_detail':product_detail,'cart_count':cart_count}

    return render(request,'singleproduct.html',context)

def addtocart(request,id):  
    user = request.user
    prod = Product.objects.get(id=id)
    item_exist = Cart.objects.filter(product=prod).exists()
    
    if item_exist:
        get_item = Cart.objects.get(product__id=id)
        get_item.quantity +=1
        get_item.save()
        return redirect('cart') 

    else:
        product = Product.objects.get(id=id)
        Cart(user=user, product=product).save()
    return redirect('cart') 

def plusquantity(request,id):
    get_item = Cart.objects.get(id=id)
    if get_item:
        get_item.quantity += 1
        get_item.save()
        return redirect('cart')

def minusquantity(request,id):
    get_item = Cart.objects.get(id=id)
    if get_item:
        get_item.quantity -= 1
        get_item.save()
        if get_item.quantity == 0:
            get_item.delete()
        return redirect('cart')

def deleteitem(request, id):
    get_item = Cart.objects.get(id=id)
    get_item.delete()
    get_name = get_item.product.name
    print(get_name)        
    messages.info(request, f'{get_name}is deleted successfully')
    return redirect('cart')

def contact(request):
    return render(request,"contact.html")

def order(request):
    cart_count = Cart.objects.filter(user=request.user).count()

    cust_order = Order.objects.filter(user= request.user)
    con={'cust_order':cust_order, 'cart_count':cart_count}
    return render(request, 'order.html', con)

def trac(request):
    return render(request,'tracking.html')
