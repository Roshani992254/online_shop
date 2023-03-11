from django.shortcuts import render, HttpResponse
from .forms import UserRgisterationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.conf import settings
from .models import Customer, Product, Order, Checkout
from .forms import *
# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRgisterationForm(request.POST)  
		# import pdb
		# pdb.set_trace()
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return HttpResponse("Form is not valid")
	form = UserRgisterationForm()
	return render(request,'register.html',{'form':form })


def home(request):
	products = Product.objects.all()
	return render(request,"home.html",{'products':products})

def login(request):

	form = AuthenticationForm()
	if request.method=="POST":
		form = AuthenticationForm(request.POST)
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=authenticate(request,username=username,password=password)
		if user is not None:
			user_login(request,user)
			return redirect("/")
		else:
			return HttpResponse("Enter valid username and password")
	else:
		form=AuthenticationForm()		
		return render(request,'login.html',{"form":form})

def contact(request):
	return render(request,"contact.html")


def search(request):

	if request.method == "POST":
		search = request.POST['search']
		products = Product.objects.filter(name__contains=search)
		return render(request, "search.html", {'search':search, 'products':products})
	else:
		return render(request, "search.html")


def product(request, myid):
	form=CreateproductForm()
	if request.method=='POST':
		form=Createproductform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request,'product.html',{'form':form})

def order(request):
	# customer= Customer.objects.get(id=i)
	customer = Customer.objects.all()
	# form=CreateorderForm(instance=customer)
	form = CreateorderForm()
	if request.method=='POST':
		# form=CreateorderForm(request.POST,instance=customer)
		form = CreateorderForm(request.POST)
		form.save()
		return redirect('/cart/')
	return render(request,'order.html',{'form':form })
	


def cart(request):
	order = Order.objects.all()
	return render(request,'cart.html',{'order':order})


def checkout(request):
	if request.method == "POST":
		
		form = CheckoutForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Checkout details is saved..!!")
	else:
		form = CheckoutForm()
		return render (request,'checkout.html',{'form':form})

def customer(request):

	if request.method == "POST":
		form = CreatecustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")

	form = CreatecustomerForm()
	return render(request,"customer.html",{'form':form})




