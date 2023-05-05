from django.shortcuts import get_object_or_404, render
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            Email = form.cleaned_data.get('Email')
            Password = form.cleaned_data.get('Password')
            Login = login.objects.create(Email=Email, Password=Password)
            Login.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'reg/registration.html', {'form': form})

def u_login(request):

   
	msg=''
   
	if request.method=='POST':
        
       
		Email=request.POST['Email']
		Password=request.POST['Password']
		user=login.objects.filter(Email=Email,Password=Password).count()
        
		if user > 0:
            
			user=login.objects.filter(Email=Email,Password=Password).first()
			

			return redirect('index')
            

		else:
			msg='Invalid!!'
            
	form=loginform
	return render(request, 'login/login.html',{'forms':form,'msg':msg})



def home_Grocery(request):
      

        if request.method == 'POST':
            form = groceryform(request.POST, request.FILES)
            if form.is_valid():
                obj=form.save(commit=False)
                form=groceryform()
                obj.save()
            details=Grocery.objects.all()
            context = {'form': form, 'st': details}
            return render(request, 'products/products.html',context)
                            
        else:
            form = groceryform()
        details=Grocery.objects.all()
        context = {'form': form, 'st': details}
        return render(request, 'products/products.html', context)   

@csrf_exempt
def delete_data_Grocery(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        s = Grocery.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})  
    
    
def editcourse(request,id):
  
    crs =Grocery.objects.get(id=id)
    form=groceryform(instance=crs)
    if request.method == 'POST':
        form = groceryform(request.POST, request.FILES, instance=crs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('add-Grocery') 
    context = {'forms': form}
    return render(request,'products/editproduct.html',context)

def index(request):
    
    products = Grocery.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)



def product_detail(request, pk):
    product = get_object_or_404(Grocery, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def add_to_cart(request):
  
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Grocery.objects.get(id=product_id)
        
        cart, created = Carts.objects.get_or_create( product=product)
        if not created:
            cart.quantity += 1
            cart.save()
        return redirect('cart')
        
    
def cart(request):
        cart_items = Carts.objects.all()
        total_quantity = sum(item.quantity for item in cart_items)
        total_price = sum(item.product.amount * item.quantity for item in cart_items)
        return render(request, 'cart.html', {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})


def update_cart(request):
    
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        quantity = int(request.POST.get('quantity'))
        cart = Carts.objects.get(pk=cart_id)
        if quantity == 0:
            cart.delete()
        else:
            cart.quantity = quantity
            cart.save()
        return redirect('cart')
    
    
def delete_from_cart(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        cart = Carts.objects.get(pk=cart_id)
        cart.delete()
        return redirect('cart')