from django.urls import path, include
from .views import home, register, login, contact,  product, search , cart, checkout, order, customer
urlpatterns = [
   
    path("",home),
    path("register/",register),
    path("login/",login),
    path("contact/",contact),
	path("cart/", cart, name="cart"),
    path("product/<int:myid>/", product, name="product"),
    path("search/", search, name="search"),
    path("customer/", customer),
    path("checkout/",checkout),
    path('order/', order), 

]
   

