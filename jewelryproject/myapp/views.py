from django.shortcuts import render,redirect
from .models import (ProductModel,CustomerModel,Cart,Order,m_cate,s_cate,p_brand,p_mate,)
from .form import (UserCreateForm, SigninForm, UserProfileChangeForm,PassChangeForm,UserProfileChangeForm,
CustomerForm,)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator 
import razorpay

# Filter Only Men Category for sidebar filter
def men_cate(pro_type):
    m_list = ['Ring','Chain','Belt buckle'] 
    if (pro_type in m_list):
        return True
    else:
        return False

# Shop
def index(request):
    if request.user.is_authenticated:
        # for men categogy
        mdata = list(dict(s_cate).keys())
        men_categories = list(filter(men_cate,mdata)) 
        # print(men_categories)
        # for women category
        women_categories = list(dict(s_cate).keys())
        # for kids category
        kids_categories = list(dict(s_cate).keys())

        

        # Display Sidebar (Main Category, Sub Category, Brand & Material)
        Main_Category = dict(m_cate).values()
        Sub_Category = dict(s_cate).values()
        Product_Brand = dict(p_brand).values()
        Product_Material = dict(p_mate).values()
        
        # Cart count
        proamount = 0
        cart_count = 0
        shipping_amt = 70
        final_amt = 0
        cart_data = Cart.objects.filter(user=request.user)
        for i in cart_data:
            prod_amt = ((i.product.sell_price)*(i.quantity))
            cart_count += i.quantity
            proamount += prod_amt
            final_amt = proamount+shipping_amt
        
        all_products = ProductModel.objects.all()
        context = {'all_products':all_products,'cart_data':cart_data,
        'men_categories':men_categories,'women_categories':women_categories,'kids_categories':kids_categories,
        'cart_count':cart_count,'proamount':proamount,'final_amt':final_amt}
        return render(request,'shop.html',context)
    else:
            # for men categogy
        mdata = list(dict(s_cate).keys())
        men_categories = list(filter(men_cate,mdata)) 
        # print(men_categories)
        # for women category
        women_categories = list(dict(s_cate).keys())
        # for kids category
        kids_categories = list(dict(s_cate).keys())

        

        # Display Sidebar (Main Category, Sub Category, Brand & Material)
        Main_Category = dict(m_cate).values()
        Sub_Category = dict(s_cate).values()
        Product_Brand = dict(p_brand).values()
        Product_Material = dict(p_mate).values()
        all_products = ProductModel.objects.all()
        
        context = {'all_products':all_products,
        'men_categories':men_categories,'women_categories':women_categories,'kids_categories':kids_categories}
        

        return render(request,"shop.html",context)

#diamond


def Diamond(request):
    all_products_count = ProductModel.objects.all().count()
    all_products_count_all = ProductModel.objects.all().count()
   
    # Display Sidebar (Main Category, Sub Category, Brand & Material)
    Main_Category = dict(m_cate).values()
    Sub_Category = dict(s_cate).values()
    Product_Brand = dict(p_brand).values()
    Product_Material = dict(p_mate).values()

    # Items Count by Main Category
    men_item = ProductModel.objects.filter(main_cate='Men').count()
    women_item = ProductModel.objects.filter(main_cate='Women').count()
    kids_item = ProductModel.objects.filter(main_cate='Kids').count()

    all_products = ProductModel.objects.filter(p_material='Diamond')
    all_products_count = ProductModel.objects.filter(sub_cate='Earrings').count()
    context = {'all_products':all_products,'Main_Category':Main_Category,
        'Sub_Category':Sub_Category,'Product_Brand':Product_Brand,'Product_Material':Product_Material,
        'all_products_count':all_products_count,'all_products_count_all':all_products_count_all,'men_item':men_item,
        'women_item':women_item,'kids_item':kids_item}
    return render(request,'allproducts.html',context)






#necklace
def Necklace(request):
    all_products_count = ProductModel.objects.all().count()
    all_products_count_all = ProductModel.objects.all().count()
   
    # Display Sidebar (Main Category, Sub Category, Brand & Material)
    Main_Category = dict(m_cate).values()
    Sub_Category = dict(s_cate).values()
    Product_Brand = dict(p_brand).values()
    Product_Material = dict(p_mate).values()

    # Items Count by Main Category
    men_item = ProductModel.objects.filter(main_cate='Men').count()
    women_item = ProductModel.objects.filter(main_cate='Women').count()
    kids_item = ProductModel.objects.filter(main_cate='Kids').count()

    
    all_products = ProductModel.objects.filter(p_material='Pearl' , sub_cate='Necklace')

    all_products_count = ProductModel.objects.filter(sub_cate='Necklace').count()
    context = {'all_products':all_products,'Main_Category':Main_Category,
        'Sub_Category':Sub_Category,'Product_Brand':Product_Brand,'Product_Material':Product_Material,
        'all_products_count':all_products_count,'all_products_count_all':all_products_count_all,'men_item':men_item,
        'women_item':women_item,'kids_item':kids_item}
    return render(request,'allproducts.html',context)






#ear ring

def Earrings(request):
    all_products_count = ProductModel.objects.all().count()
    all_products_count_all = ProductModel.objects.all().count()
   
    # Display Sidebar (Main Category, Sub Category, Brand & Material)
    Main_Category = dict(m_cate).values()
    Sub_Category = dict(s_cate).values()
    Product_Brand = dict(p_brand).values()
    Product_Material = dict(p_mate).values()

    # Items Count by Main Category
    men_item = ProductModel.objects.filter(main_cate='Men').count()
    women_item = ProductModel.objects.filter(main_cate='Women').count()
    kids_item = ProductModel.objects.filter(main_cate='Kids').count()

    all_products = ProductModel.objects.filter(sub_cate='Earrings')
    all_products_count = ProductModel.objects.filter(sub_cate='Earrings').count()
    context = {'all_products':all_products,'Main_Category':Main_Category,
        'Sub_Category':Sub_Category,'Product_Brand':Product_Brand,'Product_Material':Product_Material,
        'all_products_count':all_products_count,'all_products_count_all':all_products_count_all,'men_item':men_item,
        'women_item':women_item,'kids_item':kids_item}
    return render(request,'allproducts.html',context)










# Banner Wedding Bangels Filter
def Banglesbanner(request):
    all_products_count = ProductModel.objects.all().count()
    all_products_count_all = ProductModel.objects.all().count()
   
    # Display Sidebar (Main Category, Sub Category, Brand & Material)
    Main_Category = dict(m_cate).values()
    Sub_Category = dict(s_cate).values()
    Product_Brand = dict(p_brand).values()
    Product_Material = dict(p_mate).values()

    # Items Count by Main Category
    men_item = ProductModel.objects.filter(main_cate='Men').count()
    women_item = ProductModel.objects.filter(main_cate='Women').count()
    kids_item = ProductModel.objects.filter(main_cate='Kids').count()

    all_products = ProductModel.objects.filter(sub_cate='Bangles')
    all_products_count = ProductModel.objects.filter(sub_cate='Bangles').count()
    context = {'all_products':all_products,'Main_Category':Main_Category,
        'Sub_Category':Sub_Category,'Product_Brand':Product_Brand,'Product_Material':Product_Material,
        'all_products_count':all_products_count,'all_products_count_all':all_products_count_all,'men_item':men_item,
        'women_item':women_item,'kids_item':kids_item}
    return render(request,'allproducts.html',context)



#wedding ring
def wedding(request):
    all_products_count = ProductModel.objects.all().count()
    all_products_count_all = ProductModel.objects.all().count()
   
    # Display Sidebar (Main Category, Sub Category, Brand & Material)
    Main_Category = dict(m_cate).values()
    Sub_Category = dict(s_cate).values()
    Product_Brand = dict(p_brand).values()
    Product_Material = dict(p_mate).values()

    # Items Count by Main Category
    men_item = ProductModel.objects.filter(main_cate='Men').count()
    women_item = ProductModel.objects.filter(main_cate='Women').count()
    kids_item = ProductModel.objects.filter(main_cate='Kids').count()

    all_products = ProductModel.objects.filter(p_material='Rose Gold')
    all_products_count = ProductModel.objects.filter(p_material='Rose Gold').count()
    context = {'all_products':all_products,'Main_Category':Main_Category,
        'Sub_Category':Sub_Category,'Product_Brand':Product_Brand,'Product_Material':Product_Material,
        'all_products_count':all_products_count,'all_products_count_all':all_products_count_all,'men_item':men_item,
        'women_item':women_item,'kids_item':kids_item}
    return render(request,'allproducts.html',context)












# Filter by Main Category sidebar
def MaincateFilter(request,mcate):
    # Filter Sidebar
    Main_Category = dict(m_cate).values()
    Sub_Category = dict(s_cate).values()
    Product_Brand = dict(p_brand).values()
    Product_Material = dict(p_mate).values()
    all_products_count = ProductModel.objects.all().count()
    all_products_count_all = ProductModel.objects.all().count()
    # Items Count by Main Category
    men_item = ProductModel.objects.filter(main_cate='Men').count()
    women_item = ProductModel.objects.filter(main_cate='Women').count()
    kids_item = ProductModel.objects.filter(main_cate='Kids').count()
    # Product filter
    all_products = ProductModel.objects.filter(main_cate=mcate)
    all_products_count = ProductModel.objects.filter(main_cate=mcate).count()
    context = {'all_products':all_products,'Main_Category':Main_Category,
        'Sub_Category':Sub_Category,'Product_Brand':Product_Brand,
        'Product_Material':Product_Material,'all_products_count':all_products_count,
        'all_products_count_all':all_products_count_all,'men_item':men_item,'women_item':women_item,
        'kids_item':kids_item}
    return render(request,'allproducts.html',context)

# Filter by Sub Category sidebar
def SubcateFilter(request,scate):
    # Filter Sidebar
    Main_Category = dict(m_cate).values()
    Sub_Category = dict(s_cate).values()
    Product_Brand = dict(p_brand).values()
    Product_Material = dict(p_mate).values()
    all_products_count = ProductModel.objects.all().count()
    all_products_count_all = ProductModel.objects.all().count()
    # Product filter
    all_products = ProductModel.objects.filter(sub_cate=scate)
    all_products_count = ProductModel.objects.filter(sub_cate=scate).count()
    context = {'all_products':all_products,'Main_Category':Main_Category,
        'Sub_Category':Sub_Category,'Product_Brand':Product_Brand,
        'Product_Material':Product_Material,'all_products_count':all_products_count,
        'all_products_count_all':all_products_count_all}
    return render(request,'allproducts.html',context)

# All Products
def AllProductsView(request):
    if request.user.is_authenticated:


         # for men categogy
        mdata = list(dict(s_cate).keys())
        men_categories = list(filter(men_cate,mdata)) 
        # print(men_categories)
        # for women category
        women_categories = list(dict(s_cate).keys())
        # for kids category
        kids_categories = list(dict(s_cate).keys())

       
        all_products = ProductModel.objects.all()
        all_products_count = ProductModel.objects.all().count()
        all_products_count_all = ProductModel.objects.all().count()
        # Items Count by Main Category
        men_item = ProductModel.objects.filter(main_cate='Men').count()
        women_item = ProductModel.objects.filter(main_cate='Women').count()
        kids_item = ProductModel.objects.filter(main_cate='Kids').count()
        
        # Display Sidebar (Main Category, Sub Category, Brand & Material)
        Main_Category = dict(m_cate).values()
        Sub_Category = dict(s_cate).values()
        Product_Brand = dict(p_brand).values()
        Product_Material = dict(p_mate).values()

        # Sidebar filter
        main_c= request.GET.get('mcategory')
        sub_c= request.GET.get('scategory')
        p_matr= request.GET.get('pmaterial')
        f_price = request.GET.get('fprice')
        # t_price = request.GET.get('tprice')
        by_name = request.GET.get('byname')
        
        if main_c and sub_c and p_matr and f_price:
            all_products = ProductModel.objects.filter(main_cate=main_c,
            sub_cate=sub_c,p_material=p_matr,og_price=f_price)
        elif main_c and sub_c and p_matr:
            all_products = ProductModel.objects.filter(main_cate=main_c,
            sub_cate=sub_c,p_material=p_matr)
        elif by_name:
            all_products = ProductModel.objects.filter(name__icontains = by_name)
            all_products_count = ProductModel.objects.filter(name__icontains = by_name).count()
       




        # for cart count
        proamount = 0
        cart_count = 0
        shipping_amt = 70
        final_amt = 0
        cart_data = Cart.objects.filter(user=request.user)
        for i in cart_data:
            prod_amt = ((i.product.sell_price)*(i.quantity))
            cart_count += i.quantity
            proamount += prod_amt
            final_amt = proamount+shipping_amt
        
        
        # Pagination 
        paginator = Paginator(all_products, 9, orphans=1)
        page_number = request.GET.get('page')
        all_products = paginator.get_page(page_number)




        context = {'all_products':all_products,'cart_data':cart_data,'Main_Category':Main_Category,
        'Sub_Category':Sub_Category,'Product_Brand':Product_Brand,'Product_Material':Product_Material,
        'cart_count':cart_count,'proamount':proamount,'final_amt':final_amt,'page_number':page_number,
        'all_products_count_all':all_products_count_all,'all_products_count':all_products_count,'men_item':men_item,
        'women_item':women_item,'kids_item':kids_item,"men_categories":men_categories,"women_categories":women_categories,"kids_categories":kids_categories}
        return render(request,'allproducts.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Product Details
def ProductDetailsView(request,id):

    by_name = request.GET.get('byname')
    if by_name:
        all_prod = ProductModel.objects.filter(name__icontains = by_name)
        all_products_count = ProductModel.objects.filter(name__icontains = by_name).count()
       
    if request.user.is_authenticated:
        # for men categogy
        mdata = list(dict(s_cate).keys())
        men_categories = list(filter(men_cate,mdata)) 
        # print(men_categories)
        # for women category
        women_categories = list(dict(s_cate).keys())
        # for kids category
        kids_categories = list(dict(s_cate).keys())
        # all_products = ProductModel.objects.all()


        one_product = ProductModel.objects.get(id=id)
        rendom = ProductModel.objects.order_by('?')[:6]
        # for cart count
        proamount = 0
        cart_count = 0
        shipping_amt = 70
        final_amt = 0
        cart_data = Cart.objects.filter(user=request.user)
        for i in cart_data:
            prod_amt = ((i.product.sell_price)*(i.quantity))
            cart_count += i.quantity
            proamount += prod_amt
            final_amt = proamount+shipping_amt


        context = {'one_product':one_product,'kids_categories':kids_categories,
        'women_categories':women_categories, 'men_categories':men_categories,
        'cart_data':cart_data,'cart_count':cart_count,'proamount':proamount,'final_amt':final_amt,'rendom':rendom}
        return render(request,'productdetails.html',context)
    else:
        one_product = ProductModel.objects.get(id=id)
        rendom = ProductModel.objects.order_by('?')[:6]
        context = {'one_product':one_product,'rendom':rendom}
        return render(request,'productdetails.html',context)
        
      
# Add $ Show Address
def AddressView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            address = CustomerModel.objects.filter(user=request.user)
            
            # for cart count
            proamount = 0
            cart_count = 0
            shipping_amt = 70
            final_amt = 0
            cart_data = Cart.objects.filter(user=request.user)
            for i in cart_data:
                prod_amt = ((i.product.sell_price)*(i.quantity))
                cart_count += i.quantity
                proamount += prod_amt
                final_amt = proamount+shipping_amt

            if form.is_valid():
                usr = request.user
                name = form.cleaned_data['name']
                mobile = form.cleaned_data['mobile']
                email = form.cleaned_data['email']
                locality = form.cleaned_data['locality']
                city = form.cleaned_data['city']
                zipcode = form.cleaned_data['zipcode']
                state = form.cleaned_data['state']
                data = CustomerModel(
                    user=usr,
                    name=name,
                    mobile=mobile,
                    email=email,
                    locality=locality,
                    city=city,
                    zipcode=zipcode,
                    state=state,
                )
                data.save()
                messages.info(request, 'Address Successfully Added...!')
                form = CustomerForm()
            context = {'form': form,'address':address,'cart_count':cart_count,'proamount':proamount,'final_amt':final_amt}
            return render(request, 'address.html', context)
        else:
            form = CustomerForm()
            address = CustomerModel.objects.filter(user=request.user)
            # for cart count
            proamount = 0
            cart_count = 0
            shipping_amt = 70
            final_amt = 0
            cart_data = Cart.objects.filter(user=request.user)
            for i in cart_data:
                prod_amt = ((i.product.sell_price)*(i.quantity))
                cart_count += i.quantity
                proamount += prod_amt
                final_amt = proamount+shipping_amt
                
        context = {'form': form,'address':address,'cart_count':cart_count,'proamount':proamount,'final_amt':final_amt}
        return render(request, 'address.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Update Address
def EditAddress(request,id):
    if request.method == 'POST':
        data = CustomerModel.objects.get(id=id)
        form = CustomerForm(request.POST,instance=data)
        address = CustomerModel.objects.filter(user=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Address Successfully Updated...!')
            return redirect('/addview/')
    else:
        data = CustomerModel.objects.get(id=id)
        form = CustomerForm(instance=data)
        address = CustomerModel.objects.filter(user=request.user)
    context = {'form': form,'address':address}
    return render(request,'address.html',context)

# Delete Address
def DeleteAddress(request,id):
    data = CustomerModel.objects.get(id=id)
    data.delete()
    messages.info(request,'Address Successfully Deleted')
    return redirect('/addview/')

# Add To Cart
def add_to_cart(request,id):
    if request.user.is_authenticated:
        
        if request.user.is_authenticated:
            if request.method == 'POST':
                product_data = ProductModel.objects.get(id=id)
                p_size = request.POST.get('psize')
                if product_data:
                    data = Cart(user = request.user,product= product_data,size=p_size)
                   
                    data1=Cart.objects.filter(user=request.user,product_id=id).exists()
                    if data1:
                        messages.info(request, 'Item already added ')
                        return redirect('shop')
                        # if data:
                        #     data1=Cart.objects.filter(user=request.user,product_id=id)
                        #     for x in data1:
                        #         x.quantity +=1
                        #         x.save()
                    else :           
                         
                        data.save()
                    # messages.info(request, 'Added')
                return redirect('/showcart/')   
            else:
                cart_data = Cart.objects.filter(user=request.user)
            context = {'cart_data':cart_data}
            return render(request,'cart.html',context)
            
        else:
            messages.info(request, '☹︎ Please Login First')
        return redirect('/signin')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Plus Product Quantity By 1
def plusscart(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cart_data = Cart.objects.filter(user=request.user)
            cart_item = Cart.objects.get(id=id)

            # for cart count
            proamount = 0
            cart_count = 0
            shipping_amt = 70
            final_amt = 0
            cart_data = Cart.objects.filter(user=request.user)
            for i in cart_data:
                prod_amt = ((i.product.sell_price)*(i.quantity))
                cart_count += i.quantity
                proamount += prod_amt
                final_amt = proamount+shipping_amt
            
            if cart_item:
                cart_item.quantity+=1
            cart_item.save()
            return redirect('/showcart/')
        else:
            # for cart count
            proamount = 0
            cart_count = 0
            shipping_amt = 70
            final_amt = 0
            cart_data = Cart.objects.filter(user=request.user)
            for i in cart_data:
                prod_amt = ((i.product.sell_price)*(i.quantity))
                cart_count += i.quantity
                proamount += prod_amt
                final_amt = proamount+shipping_amt
            context = {'cart_data':cart_data,'proamount':proamount,'final_amt':final_amt,'proamount':proamount,'final_amt':final_amt}
            return render(request,'cart.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Minuse Product Quantity By 1
def minuscart(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cart_data = Cart.objects.filter(user=request.user)
            cart_item = Cart.objects.get(id=id)

            
            # for cart count
            proamount = 0
            cart_count = 0
            shipping_amt = 70
            final_amt = 0
            cart_data = Cart.objects.filter(user=request.user)
            for i in cart_data:
                prod_amt = ((i.product.sell_price)*(i.quantity))
                cart_count += i.quantity
                proamount += prod_amt
                final_amt = proamount+shipping_amt

            if cart_item:
                cart_item.quantity-=1
                if cart_item.quantity == 0:
                    cart_item.delete()
                else:
                    cart_item.save()
            return redirect('/showcart/')
        else:
            data = Cart.objects.filter(user=request.user)
        context = {'cart_data':cart_data}
        return render(request,'cart.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Remove Item From Cart
def RemoveItem(request,id):
    if request.user.is_authenticated:
        cart_item = Cart.objects.get(id=id)
        cart_item.delete()
        cart_data = Cart.objects.filter(user=request.user)
        
        context = {'cart_data':cart_data}
        return redirect('/showcart/')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Clear Cart
def ClearCart(request):
    cart_data = Cart.objects.filter(user=request.user)
    cart_data.delete()
    return redirect('/showcart/')

# Show Cart
def ShowCartView(request):
    if request.user.is_authenticated:
        # for men categogy
        mdata = list(dict(s_cate).keys())
        men_categories = list(filter(men_cate,mdata)) 
        # print(men_categories)
        # for women category
        women_categories = list(dict(s_cate).keys())
        # for kids category
        kids_categories = list(dict(s_cate).keys())
        all_products = ProductModel.objects.all()

        cart_data = Cart.objects.filter(user=request.user)
        # checkout details
        proamount = 0
        cart_count = 0
        shipping_amt = 70
        final_amt = 0
        data = Cart.objects.filter(user=request.user)
        for i in data:
            prod_amt = ((i.product.sell_price)*(i.quantity))
            proamount += prod_amt
            cart_count += i.quantity
            final_amt = proamount+shipping_amt
        
        context = {'cart_data':cart_data,'all_products':all_products ,
        'kids_categories':kids_categories ,'women_categories':women_categories,
        'men_categories':men_categories,'proamount':proamount,'final_amt':final_amt,'cart_count':cart_count}
        return render(request,'cart.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Checkout
def CheckoutView(request):
    if request.user.is_authenticated:
        cart_data = Cart.objects.filter(user=request.user)
        customer_data = CustomerModel.objects.filter(user=request.user)
        # checkout details
        proamount = 0
        cart_count = 0
        shipping_amt = 70
        final_amt = 0
        data = Cart.objects.filter(user=request.user)
        for i in data:
            prod_amt = ((i.product.sell_price)*(i.quantity))
            cart_count += i.quantity 
            proamount += prod_amt
            
            final_amt = proamount+shipping_amt
        # # Payment Start
        ok = (final_amt)*100
        client = razorpay.Client(auth=("rzp_test_ipzrIdLiSar1fv", "pjxtqHmkQbw3M1QXzArVFQoE"))
        payment = client.order.create({'amount': ok, 'currency': 'INR','payment_capture': '1'})
        # Payment End  
        context = {'cart_data':cart_data,'customer_data':customer_data,
        'proamount':proamount,'prod_amt':prod_amt,'final_amt':final_amt,
        'cart_count':cart_count,'payment':payment,}
        if not context['customer_data'].values():
            context["no_address"] = True
        return render(request,'checkout.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Place Order
def PlaceorderView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # paymode = request.POST.get('paymentmethod')
            # if paymode == 'cash':
            #     cart_data = Cart.objects.filter(user=request.user)
            #     add_id = request.POST.get('address_id')
            #     customer_add = CustomerModel.objects.get(id=add_id)
            #     customer_data = CustomerModel.objects.filter(user=request.user)
            #     # checkout details
            #     proamount = 0
            #     cart_count = 0
            #     shipping_amt = 70
            #     final_amt = 0
            #     data = Cart.objects.filter(user=request.user)
            #     for i in data:
            #         prod_amt = ((i.product.sell_price)*(i.quantity))
            #         cart_count += i.quantity
            #         proamount += prod_amt 
            #         final_amt = proamount+shipping_amt
            #         order_data = Order(
            #             user=request.user,
            #             customer=customer_add,
            #             product=i.product,
            #             quantity=i.quantity,
            #             psize=i.size,
            #         )
            #         order_data.save()
            #         messages.success(request,'Your Order Successfully Placed Thank you shoping With us')
            #     cart_data.delete()
            #     return redirect('/orders/')
            # elif paymode == 'bank':
            cart_data = Cart.objects.filter(user=request.user)
            add_id = request.POST.get('address_id')
            customer_add = CustomerModel.objects.get(id=add_id)
            customer_data = CustomerModel.objects.filter(user=request.user)
            
            # checkout details
            proamount = 0
            cart_count = 0
            shipping_amt = 70
            final_amt = 0
            data = Cart.objects.filter(user=request.user)
            for i in data:
                prod_amt = ((i.product.sell_price)*(i.quantity))
                cart_count += i.quantity
                proamount += prod_amt
                final_amt = proamount+shipping_amt
                order_data = Order(
                    user=request.user,
                    customer=customer_add,
                    product=i.product,
                    quantity=i.quantity,
                    psize=i.size,
                )
                order_data.save()
                messages.success(request,'Your Order Successfully Placed Thank you shoping With us')
            cart_data.delete()
            # Pament Start
            ok = (final_amt)*100
            client = razorpay.Client(auth=("rzp_test_ipzrIdLiSar1fv", "pjxtqHmkQbw3M1QXzArVFQoE"))
            payment = client.order.create({'amount': ok, 'currency': 'INR','payment_capture': '1'})
            # Pament End 
            return redirect('/orders/')

        else:
            cart_data = Cart.objects.filter(user=request.user)
            add_id = request.POST.get('address_id')
            customer_data = CustomerModel.objects.filter(user=request.user)
            # checkout details
            proamount = 0
            cart_count = 0
            shipping_amt = 70
            final_amt = 0
            data = Cart.objects.filter(user=request.user)
            for i in data:
                prod_amt = ((i.product.sell_price)*(i.quantity))
                cart_count += i.quantity
                proamount += prod_amt
                final_amt = proamount+shipping_amt
            # # Pament Start
            ok = (final_amt)*100
            client = razorpay.Client(auth=("rzp_test_ipzrIdLiSar1fv", "pjxtqHmkQbw3M1QXzArVFQoE"))
            payment = client.order.create({'amount': ok, 'currency': 'INR','payment_capture': '1'})
            # Pament End             
            context = {'cart_data':cart_data,'customer_data':customer_data,
            'proamount':proamount,'prod_amt':prod_amt,'final_amt':final_amt,'cart_count':cart_count,
            'proamount':proamount,'final_amt':final_amt,'payment':payment,}
        return render(request,'checkout.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# Show Orders List
def OrdersView(request):
    if request.user.is_authenticated:
        order_data = Order.objects.filter(user=request.user)[::-1]

        # Pagination 
        paginator = Paginator(order_data, 5, orphans=0)
        page_number = request.GET.get('page')
        order_data = paginator.get_page(page_number)

        # For Cart count
        proamount = 0
        cart_count = 0
        shipping_amt = 70
        final_amt = 0
        data = Cart.objects.filter(user=request.user)
        for i in data:
            prod_amt = ((i.product.sell_price)*(i.quantity))
            cart_count += i.quantity
            proamount += prod_amt
            
            final_amt = proamount+shipping_amt
        context = {'order_data':order_data,'cart_count':cart_count,'page_number':page_number,
        'proamount':proamount,'final_amt':final_amt}
        return render(request,'order.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')




def orderdetails(request,id):
    if request.user.is_authenticated:
        one_product = Order.objects.get(id=id)
        rendom = Order.objects.order_by('?')[:6]
        customer_data = CustomerModel.objects.filter(user=request.user)
        
        order_data = Order.objects.filter(user=request.user)[::-1]
        # for cart count
        proamount = 0
        cart_count = 0
        shipping_amt = 70
        final_amt = 0
        for i in order_data:
            prod_amt = ((i.product.sell_price)*(i.quantity))
            cart_count += i.quantity
            proamount += prod_amt
            final_amt = proamount+shipping_amt


        context = {"order_data":order_data,'one_product':one_product,'cart_count':cart_count,'proamount':proamount,'final_amt':final_amt,'rendom':rendom,'customer_data':customer_data}
        return render(request,'orderdetails.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

# -------------------------------------------------------------------------------
#                              Auth Section
# -------------------------------------------------------------------------------

# User Login
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
            # messages.info(request, 'Login Successful')
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'signin.html', {'form': form})

# Logout
def Userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, '🙋‍ You are Successfully Logged Out !')
    return redirect('/signin/')

# User Register
# def UserRegisterView(request):
#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             uname = form.cleaned_data['username']
#             form.save()
#             messages.success(request, f'{uname} - User Successfully Registred')
#             form = UserCreateForm()
#             context = {'form': form}
#             return render(request, 'signup.html', context)
#     else:
#         form = UserCreateForm()
#     context = {'form': form}
#     return render(request, 'signup.html', context)

# User Register
def UserRegisterView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already found')
            return redirect('signup')
            
        if User.objects.filter(email=email).exists():
            messages.info(request, 'EmailId already found')
            return redirect('signup')
        if password1 == password2:
            usr = User(username=username, email=email)
            usr.set_password(password1)
            usr.save()

        messages.info(request, 'Successfully register' )



        return redirect('signup')

      
    return render(request, 'signup.html')



# User Password Change
def ChangePassView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # For cart count
            cart_count = 0
            data = Cart.objects.filter(user=request.user)
            for i in data:
                cart_count += i.quantity
            form = PassChangeForm(user = request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Password Successfully Changed')
        else:
            form = PassChangeForm(user =request.user)
            # For cart count
            cart_count = 0
            data = Cart.objects.filter(user=request.user)
            for i in data:
                cart_count += i.quantity
        context= {'form':form,'cart_count':cart_count}
        return render(request,'changepass.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin/')

# Profile 
def ProfileChange(request):
        if request.user.is_authenticated:

                if request.method == 'POST':
                    form = UserProfileChangeForm(request.POST, instance=request.user)
                    # For cart count
                    cart_count = 0
                    data = Cart.objects.filter(user=request.user)
                    for i in data:
                        cart_count += i.quantity
                    context = {'form': form,'cart_count':cart_count}
                    if form.is_valid():
                        form.save()
                        messages.success(
                            request, f'{request.user} - Your Profile Successfully Updated...!')
                        return render(request, 'profile.html', context)
                else:
                    form = UserProfileChangeForm(instance=request.user)
                    # For cart count
                    cart_count = 0
                    data = Cart.objects.filter(user=request.user)
                    for i in data:
                        cart_count += i.quantity
                    context = {'form': form,'cart_count':cart_count}
                    return render(request,'profile.html',context)
        else:
            messages.info(request, '☹︎ Please Login First')
        return redirect('/signin/')
