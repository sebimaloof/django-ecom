from django.shortcuts import render ,redirect
from django.db.models import Q
from.models import *

# Create your views here.

def index(request):
    
    all={
        'week':AllProducts.objects.filter(weekly_product=True),
        'new':AllProducts.objects.filter(new_arrivals=True),
        
    }
    
    return render(request,'index.html',all)
    
    


def about(request):
    
    return render(request,'about.html')






def category(request,code=None):
    
    all_codes = ProductCode.objects.all()
    search = request.GET.get("q", "").strip()

    if code:
        product_code = ProductCode.objects.get(code=code)
        products = AllProducts.objects.filter(product_code=product_code)
    else:
        products = AllProducts.objects.all()
        
    if search:
        products = products.filter(
            Q(product_name__icontains=search) |
            Q(pro_discr1__icontains=search) |
            Q(pro_discr2__icontains=search) |
            Q(pro_discr3__icontains=search)
        )

    products = products[0:25]

   

    procode = {
        'products': products,
        'filter_code':code,
        'all_codes': all_codes,
    }

    return render(request, 'category.html', procode)


# single_product

def single_product(request, single_id):
    product = AllProducts.objects.get(id=single_id)
    return render(request, 'single_product.html',{'product': product})
    
    
# cart 

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def add_cart(request, product_id):
    
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    
    product = AllProducts.objects.filter(id=product_id).first()
    
   
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.quantity * int(product.current_price.replace(',', ''))
        cart_item.save()
    
    
    
    return redirect('cart')



def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    items = CartItem.objects.filter(user=user)
    
    
    cart_items = []
    total = 0
    for item in items:
        subtotal = item.quantity * int(item.product.current_price.replace(',', ''))
        total += subtotal
        cart_items.append({
            'id': item.product.id,
            'product_name': item.product.product_name,
            'quantity': item.quantity,
            'price': int(item.product.current_price.replace(',', '')),
            'subtotal': subtotal,
            'image': item.product.product_image.url  
        })
    
    count=len(cart_items)
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total,'count':count})


def decrease_quantity(request, product_id):
    
    user=request.user
    decrease = AllProducts.objects.filter(id=product_id)[:1]
    
    cart_item,create=CartItem.objects.get_or_create(user=user , product=decrease)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        
    return redirect('cart')


def remove_cart(request, remove_id):
    
    user=request.user
    product = AllProducts.objects.filter(id=remove_id)[:1]
    cart_item = CartItem.objects.filter(user=user, product=product).first()
    if cart_item:
        cart_item.delete()
    
    return redirect('cart')



    

# page2
def category_page2(request):
    all_codes = ProductCode.objects.all()

    products = AllProducts.objects.all()[26:50]


   

    procode = {
        'products': products,
        'all_codes': all_codes,
    }
    return render(request,'category_page2.html',procode)
   
# page3
def category_page3(request):
    all_codes = ProductCode.objects.all()

    products = AllProducts.objects.all()[51:75]


   

    procode = {
        'products': products,
        'all_codes': all_codes,
    }
    return render(request,'category_page3.html',procode)
   
# page4
def category_page4(request):
    all_codes = ProductCode.objects.all()

    products = AllProducts.objects.all()[76:100]


   

    procode = {
        'products': products,
        'all_codes': all_codes,
    }
    return render(request,'category_page4.html',procode)
   
# page5
def category_page5(request):
    all_codes = ProductCode.objects.all()

    products = AllProducts.objects.all()[101:125]

    procode = {
        'products': products,
        'all_codes': all_codes,
    }
    return render(request,'category_page5.html',procode)
   
# signup and login 

from .forms import Signup_Form
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm   

# username : sebimaloof
# email : sebimaloof@gmail.com
# password : puthanpeedikakkal

def signup(request):
    if request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')  
    else:
        form = Signup_Form()
    return render(request, 'signup.html', {'form': form})




def loginpage(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')
    else:
        form=AuthenticationForm()
    
    return render(request,'login.html',{'form':form})



from django.contrib.auth import logout


def logout_view(request):
    
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')



def profile_form(request):

    obj, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        obj.adress = request.POST.get('adress', '')
        obj.location = request.POST.get('location', '')
        obj.mobile_number = request.POST.get('mobile_number', '')
        obj.birth_date = request.POST.get('date', '')
        obj.save()
        return redirect('profile')
   

    return render(request, 'user_profile.html', {'profile': obj})


def userprofile(request):
    
    if request.user.is_authenticated:
        profile,created  = Profile.objects.get_or_create(user=request.user)
        return render(request, 'profile.html', {'profile': profile})
    else:
        return redirect('login')
    

def buy(request):
    profile=Profile.objects.get(user=request.user)
    items=CartItem.objects.filter(user=request.user)
    
    obj, created = Profile.objects.get_or_create(user=request.user)
    
    cart_items=[]
    total = 0
    for item in items:
        subtotal = item.quantity * int(item.product.current_price.replace(',', ''))
        total += subtotal
        
        cart_items.append({
        'item': item,
        'subtotal': subtotal,
    })

       

    if request.method == 'POST':
        obj.adress = request.POST.get('adress', '')
        obj.location = request.POST.get('location', '')
        obj.mobile_number = request.POST.get('mobile_number', '')
        obj.birth_date = request.POST.get('date', '')
        obj.save()
        return redirect('buy')
         
    pro={
           'pro':profile,
           'item':items,
           'cart_items':cart_items,
           'profilee': obj , 
           'total_price':total
           
       }  
    
    return render(request,'buy.html',pro)


