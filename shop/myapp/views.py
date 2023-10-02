from django.shortcuts import render,redirect
from .models import*
from django.conf import settings
from django.core.mail import send_mail
import random
import razorpay

# Create your views here.

def index(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        mid = main_category.objects.all()
        context={
            'uid' : uid,
            'mid' : mid
            }
        return render(request, 'myapp/index.html',context)
    
    else:
        return render(request, 'myapp/login.html')

def shop(request):
    uid = user.objects.get(email=request.session['email'])

    aid = Add_product.objects.all()

    context = {
        'aid' : aid,
        'uid' : uid
    }

    return render(request, 'myapp/shop.html',context)

def add_to_cart(request,id):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        pid = Add_product.objects.get(id=id)
        pcid = Add_to_cart.objects.filter(user_id=uid,product_id=pid).exists()
        if pcid:
            pcid = Add_to_cart.objects.get(product_id=pid)
            pcid.que = pcid.que+1
            pcid.total_price = pcid.que * pcid.price
            pcid.save()

            return redirect("shoppingcart")
        else:
            
            aid = Add_to_cart.objects.create(user_id=uid,
                                            product_id=pid,
                                            name = pid.name,
                                            IMG=pid.IMG,
                                            que=pid.que,
                                            price=pid.price,
                                            total_price=pid.que*pid.price
                                            
                                            
            )
            return redirect("shoppingcart")

def shoppingcart(request):
    uid = user.objects.get(email=request.session['email'])

    pid = Add_to_cart.objects.filter(user_id=uid)
    context ={

        'pid' : pid,
        'uid' : uid
    }
    return render(request, 'myapp/shoppingcart.html',context)

def plus(request,id):
    uid = user.objects.get(email=request.session['email'])

    pid = Add_to_cart.objects.get(id=id)
    if pid:
        pid.que = pid.que + 1
        pid.total_price = pid.que * pid.price
        pid.save()

        return redirect("shoppingcart")

def minus(request,id):
    uid = user.objects.get(email=request.session['email'])
    mid = Add_to_cart.objects.get(id=id)
    
    if mid:
        mid.que = mid.que - 1
        mid.total_price = mid.que * mid.price
        mid.save()
        return redirect("shoppingcart")


def remove(request,id):

    rid = Add_to_cart.objects.get(id=id)

    rid.delete()

    return redirect("shoppingcart")



def checkout(request):
    uid = user.objects.get(email=request.session['email'])

    cid = Add_to_cart.objects.filter(user_id=uid)

    l1 = []

    sub_total = 0

    total = 1

    for x in cid:

        z = x.que * x.price

        l1.append(z)

        sub_total = sum(l1)

        total = sub_total + 50

    amount = total*100
    client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    response = client.order.create({

                                    'amount':amount,
                                   'currency':'INR',
                                   'payment_capture':1

    
    })
    print(response,"****************************************")
   

    context ={
        'cid' : cid,
        'sub_total' : sub_total,
        'total' : total,
        'response' : response,
        'uid' : uid
    }
    return render(request,"myapp/checkout.html",context)






def product(request):
    return render(request, 'myapp/product.html')

def blog(request):
    return render(request, 'myapp/blog.html')

def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        cid = Contact.objects.create(name=name,email=email,message=message)
        context={ 'cid' : cid,
                  'cs_msg' : "Your message has been sent"}
        
        return render(request, 'myapp/contact.html',context)
    
    else:
         return render(request, 'myapp/contact.html')
     
def blogdetails(request,id):

    aid = Add_product.objects.filter(id=id)

    context = {

        'aid' : aid
    }
    return render(request, 'myapp/blogdetails.html',context)

def category(request,id):
    mid = Add_product.objects.filter(main_id=id)

    context = { 'mid':mid}

    return render(request, 'myapp/category.html',context)


def faq(request):
    return render(request, 'myapp/faq.html')

def login(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        
        context={
            'uid' : uid
            }
        return render(request, 'myapp/index.html',context)
    else:
        try:
            if request.POST:
                email = request.POST['email']
                password = request.POST['password']
                
                uid = user.objects.get(email = email)
                
                                    
                if uid.password ==password:
                    request.session['email'] = uid.email
                    context={
                        'uid' : uid
                    }
                    return render(request, 'myapp/index.html',context)
                else:
                    context={
                        'p_msg' : "Invalid password...."
                    }
                    return render(request, 'myapp/login.html',context)
            
            else:
                return render(request, 'myapp/login.html')
    
        except:
            context={
                'e_msg' : "Invalid email....."
            }
            return render(request, 'myapp/login.html',context)
        
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request, 'myapp/login.html')
    
    else:
        return render(request, 'myapp/login.html')
    

def register(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
            
        rid = user.objects.create(email=email,
                                    password=password)
                                   
       
            
        context={
            'rid':rid
        }

        return render(request,'myapp/login.html',context)
    

        
    else:
        return render(request,'myapp/register.html')
    
def forgetpassword(request):
    if request.POST:
        email = request.POST['email']
        otp = random.randint(1111,9999)
    
        uid = user.objects.get(email=email)
        if uid.email == email:
            uid.otp = otp
            uid.save()
            send_mail("forgot password", "your otp is"+str(otp),"gohiljayb10@gmail.com",[email])
            context ={
                'email' : email
            }
                    
            return render(request, 'myapp/newpassword.html', context)
        else:
            context ={
                    'oe_msg' : "Invalid email...."
                }
            return render(request, 'myapp/forgetpassword.html', context)
       
    else:
        return render(request, 'myapp/forgetpassword.html')


def newpassword(request):
    if request.POST:
        otp = request.POST['otp']
        email = request.POST['email']
        Npassword = request.POST['Npassword']
        Cpassword = request.POST['Cpassword']
        
        
        uid = user.objects.get(email=email)
        if str(uid.otp) == otp:
            if Npassword == Cpassword:
                uid.password = Npassword
                uid.save()
                    
                context = {
                    'email' : email
                }
                    
                return render(request, 'myapp/login.html', context)
            else:
                context ={
                        'np_msg' : "Invalid new password...."
                    }
                return render(request, 'myapp/newpassword.html', context)
                
        else:
            context ={
                    'o_msg' : "Invalid otp...."
                }
            return render(request, 'myapp/newpassword.html', context)
       
    else:
           
        return render(request, 'myapp/newpassword.html')
    
            
           
            
            
            
    