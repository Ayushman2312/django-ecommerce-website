from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




class Category(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="media")
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    warranty = models.CharField(max_length=1000, null=True, blank=True)
    return_policy = models.CharField(max_length=1000, null=True, blank=True)
    view_count = models.PositiveIntegerField()


    def __str__(self):
        return self.title

    @staticmethod
    def get_image(image):
        return Product.objects.get(image=image)



class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Cart" + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Cart: " + str(self.cart.id) + "Cart Product" + str(self.id)


ORDER_STATUS = (
    ("ORDER RECIVED", "ORDER RECIEVED"), 
    ("ORDER PROCESSING", "ORDER PROCESSING"), 
    ("ORDER ON THE WAY", "ORDER ON THE WAY"), 
    ("ORDER COMPLETED", "ORDER COMPLETED"),
    ("ORDER CANCELLED", "ORDER CANCELLED"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=1000)
    shipping_address = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=200)
    email = models.EmailField()
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=100, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order" + str(self.id)
