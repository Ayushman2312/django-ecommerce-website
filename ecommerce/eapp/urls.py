from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about', AboutView.as_view(), name="about"),
    path('service', ServiceView.as_view(), name='service'), 
    path('contact', ContactView.as_view(), name="contact"),
    path('allproducts', AllProducts.as_view(), name="allproducts"),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name="productdetail"),
    path('add-to-cart-<int:pro_id>/', AddToCart.as_view(), name="addtocart"),
    path('my-cart/', MyCart.as_view(), name="mycart"),
    path('manage-my-cart<int:cp_id>', ManageCartView.as_view(), name="manage-my-cart"),
    path('empty-cart/', EmptyCartView.as_view(), name="emptycart"),
    path("checkout", CheckoutView.as_view(), name="checkout"),
    path('register/', CustomerRegisterationView.as_view(), name="register"),
    path('logout', CustomerLogout.as_view(), name="logout"),
    path('login', CustomerLogin.as_view(), name="login"),
    # path('apiview', ProductAPIView.as_view(), name="apiview"),
]
