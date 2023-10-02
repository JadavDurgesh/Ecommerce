
from re import search
from django.shortcuts import render

from django.shortcuts import render, redirect

from myapp.models import Cart, CustomeraddressModel, Maincategory, Order, Wishlist, contactmodel, productmodel
from .form import ContactForm, CustomeraddressForm, PassChangeForm, SigninForm, UserProfileChangeForm, signupform
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
import razorpay
# Create your views here.


def homeview(request):
    data = Maincategory.objects.all()
    prodctdata = productmodel.objects.all()
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    context = {"data": data, 'prodctdata': prodctdata,'cart_count':cart_count}
    return render(request, "home.html", context)

# User Signup


def signupview(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            usrname = form.cleaned_data['username']
            form.save()
            messages.success(request, f'{usrname} Successfully Registred')
            form = signupform()
        return render(request, 'signup.html', {'form': form})
    else:
        form = signupform()
        context = {'form': form, }
    return render(request, 'signup.html', context)


# User Signin
def SigninView(request):
    form = SigninForm()
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        user = authenticate(username=uname, password=upass)
        if user is None:
            messages.error(request, 'Please Enter Correct Credinatial')
            return redirect('/signin/')
        else:
            login(request, user)
            messages.success(request, 'Login Successful')
        return redirect('/')
        # return render(request,'home.html')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'signin.html', {'form': form})

# user logout


def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'you are successfully logout')
        return redirect('/signin/')
    else:
        messages.info(request, 'please login first')
    return redirect('/signin/')


def ChangePassView(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
        if request.method == 'POST':
            form = PassChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Successfully Changed')
        else:
            form = PassChangeForm(user=request.user)

        context = {'form': form, 'cart_count':cart_count}
        return render(request, 'passchange.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin/')


# profile
def ProfileView(request):
    if request.user.is_authenticated:
        form = UserProfileChangeForm(instance=request.user)
        context = {'form': form}
        if request.method == 'POST':
            form = UserProfileChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                get_user = form.cleaned_data['username']
                messages.info(request, f'{get_user} - successfully updates')
                return redirect('/profile/')
        else:
            form = UserProfileChangeForm(instance=request.user)
        context = {'form': form, }
        return render(request, 'profile.html', context)


def ProductInfoView(request, id):
    get_product = productmodel.objects.get(id=id)
    context = {'get_product': get_product}
    return render(request, 'proinfo.html', context)


def AllproductView(request):
    all_categories = Maincategory.objects.all()
    all_products = productmodel.objects.all()
    #cart_count = cart.objects.filter(user=request.user).count()

    get_cat_id = request.GET.get('catesid')
    if get_cat_id:
        all_products = productmodel.objects.filter(pcate__id=get_cat_id)

    get_product_name = request.GET.get('byname')
    if get_product_name:
        all_products = productmodel.objects.filter(
            name__icontains=get_product_name)

    get_category = request.GET.get('catename')
    get_from_price = request.GET.get('startprice')
    get_to_price = request.GET.get('endprice')

    get_prodname = request.GET.get('byname')
    if get_category and get_from_price == '' and get_to_price == '' and get_prodname == '':
        all_products = productmodel.objects.filter(pcate__name=get_category)
    if get_category and get_from_price and get_to_price == '' and get_prodname == '':
        all_products = productmodel.objects.filter(
            pcate__name=get_category, sell_price__gte=int(get_from_price))
    if get_category and get_from_price and get_to_price and get_prodname == '':
        all_products = productmodel.objects.filter(pcate__name=get_category, sell_price__gte=int(
            get_from_price), sell_price__lte=int(get_to_price))
    if get_category and get_from_price and get_to_price and get_prodname:
        all_products = productmodel.objects.filter(pcate__name__icontains=get_category, sell_price__gte=int(
            get_from_price), sell_price__lte=int(get_to_price), name__icontains=(get_prodname))
    
    context={'all_categories':all_categories,'all_products':all_products}
    return render(request,'allproducts.html',context)


                                                                                            
def CartView(request):
    if request.user.is_authenticated:

        cart_count = Cart.objects.filter(user=request.user).count()
        cart_items = Cart.objects.filter(user=request.user)

        sub_total = 0
        ship_charged = 0
        GST = 0
        grand_total = 0

        user = request.user
        get_address_id = request.GET.get('add')

        for i in cart_items:
            
            sub_total += i.prod_total()
            # ship_charged = sub_total<=100
            total = sub_total + ship_charged
            GST = total*0.12
            grand_total = GST+ total

    else:
        return redirect('login')

    context = {'cart_count': cart_count, 'cart_items': cart_items, 'sub_total': sub_total,
               'ship_charge': ship_charged, 'GST':  GST  ,'grand_total': grand_total}
    return render(request, 'cart.html', context)

def Add_to_cartView(request, id):
    user = request.user
    prod = productmodel.objects.get(id=id)
    item_exist = Cart.objects.filter(user=request.user,product=prod).exists()

    if item_exist:
        get_item = Cart.objects.get(product__id=id)
        get_item.quantity += 1
        get_item.save()
        return redirect('/cart/')
    else:
        product = productmodel.objects.get(id=id)
    Cart(user=user, product=product).save()
    return redirect('/cart/')



def DeleteView(request, id):
    get_item = Cart.objects.get(id=id)
    get_item.delete()
    get_name = get_item.product.name
    messages.error(request, f'{get_name} - Successfully delete')

    return redirect('cart')


def pluse_quantity(request, id):
    get_item = Cart.objects.get(id=id)
    if get_item:
        get_item.quantity += 1
        get_item.save()
        return redirect('/cart/')


def minus_quantity(request, id):
    get_item = Cart.objects.get(id=id)
    if get_item:
        get_item.quantity -= 1
        get_item.save()
        if get_item.quantity == 0:
            get_item.delete()
        return redirect('/cart/')

def clearcart(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_items.delete()
    messages.error(request, 'Cart Successfully Cleared')
    return redirect('/cart/')


def Add_to_wishlistView(request, id):
    user = request.user
    prod = productmodel.objects.get(id=id)
    item_exist = Wishlist.objects.filter(user=request.user,product=prod).exists()

    if item_exist:
        get_item = Wishlist.objects.get(product__id=id)
        get_item.quantity += 1
        get_item.save()
        return redirect('/wishlist/')
    else:
        product = productmodel.objects.get(id=id)
    Wishlist(user=user, product=product).save()
    return redirect('/wishlist/')



def WishListView(request):   
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()

        wishlist_count = Wishlist.objects.filter(user=request.user).count()
        wishlist_items = Wishlist.objects.filter(user=request.user)
    else:
        return redirect('login')

    context = {'wishlist_count': wishlist_count, 'cart_count':cart_count, 
    'wishlist_items': wishlist_items}
    return render(request, 'wishlist.html', context)


def DeletewishlistView(request, id):
    get_item = Wishlist.objects.get(id=id)
    get_item.delete()
    get_name = get_item.product.name

    messages.error(request, f'{get_name} - Successfully delete')
    return redirect('/wishlist/')



def CheckoutView(request):
    if request.user.is_authenticated:

        cart_count = Cart.objects.filter(user=request.user).count()
        cart_items = Cart.objects.filter(user=request.user)
        all_address = CustomeraddressModel.objects.filter(user=request.user)
        # totals count -----
        sub_total = 0
        ship_charge = 0
        GST = 0
        grand_total = 0
        # get data for order
        usr = request.user
        get_address_id = request.GET.get('add')

        for i in cart_items:
            sub_total += i.prod_total()
            total = sub_total + ship_charge
            GST = total* 0.12
            grand_total= GST+ total
        # Payment Start
        amount = (grand_total)*100
        client = razorpay.Client(
        auth=("rzp_test_abD1wLLRfEnWCU", "D6FZtPTRHaIw7IfiF3y99paf"))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        # payment End
        if get_address_id:
            address = CustomeraddressModel.objects.get(id=get_address_id)
            for i in cart_items:
                order_data = Order(
                    user=usr,
                    customer=address,
                    product=i.product,
                    quantity=i.quantity

                )
                order_data.save()
                cart_items.delete()
            return redirect('orders')
    else:
        return redirect('login')

    context = {'cart_count': cart_count, 'cart_items': cart_items, 'sub_total': sub_total,
               'ship_charge': ship_charge,'GST': GST, 'grand_total': grand_total, 'all_address': all_address,
               'payment': payment}
    return render(request, 'checkout.html', context)




def AddressDeleteView(request, id):
    address = CustomeraddressModel.objects.get(id=id)
    address.delete()
    messages.error(request, 'address Successfully delete')
    return redirect('/address/')


def UpdateaddressView(request, id):
    address = CustomeraddressModel.objects.all()  # Show data of Student Table
    set_address = CustomeraddressModel.objects.get(id=id)
    if request.method == 'POST':
        form = CustomeraddressForm(
            request.POST, request.FILES, instance=set_address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Successfully Updated')
            return redirect('/address/')
    else:
        form = CustomeraddressForm(instance=set_address)
    context = {'form': form, 'address': address}
    return render(request, 'address.html', context)


def CustomerAddressView(request):
    all_address = CustomeraddressModel.objects.filter(user=request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomeraddressForm(request.POST)
            if form.is_valid():
                fm = form.save(commit=False)
                fm.user = request.user
                fm.save()

                messages.info(request, 'Address Successfully Added')
                return redirect('/address/')
        else:
            form = CustomeraddressForm()

        context = {'form': form, 'all_address': all_address}
        return render(request, 'address.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
        return redirect('/signin/')


def OrderView(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
        cust_order = Order.objects.filter(user=request.user)
    else:
        return redirect('login')

    context = {'cust_order': cust_order, 'cart_count':cart_count}
    return render(request, 'orders.html', context)



def contactview(request):
    if request.user.is_authenticated:
        contacts=contactmodel.objects.filter(user=request.user)
        cart_count = Cart.objects.filter(user=request.user).count()

        form=ContactForm(instance=request.user)
        context={'form':form}
        if request.POST:
            form=ContactForm(request.POST)
            if form.is_valid():
                fm=form.save(commit=False)
                fm.user=request.user
                fm.save()

                messages.info(request,'your message has been successfully send')
                return redirect('/contact/')

        else:
            form=ContactForm(instance=request.user)
        context={'form':form,'contacts':contacts, 'cart_count':cart_count}
        return render(request,'contact.html',context)
    
    else:
        messages.info(request, '☹ Please Login First')
        return redirect('/signin/')




def AboutView(request):
    cart_count = Cart.objects.filter(user=request.user).count()

    return render(request, "about.html", {'cart_count':cart_count})


def SearchView(request):
    search = request.GET.get("search")
    if search:
        all_products = productmodel.objects.filter(name__contains=search) 
    else:

        all_products =messages.info(request, 'Search any product')

    return render(request,"allproducts.html",{'all_products': all_products})
