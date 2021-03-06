from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

# Create your models here.

class Cart(models.Model):

    owner = models.OneToOneField(User,
                                 related_name="cart",
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    number_of_items = models.PositiveIntegerField(default=0)

    total = models.DecimalField(default=0.00,
                                max_digits=5,
                                decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User: {self.owner}, items in cart {self.number_of_items}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Product,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField()


ORDER_STATUS = (
    ('placed', 'Placed'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered')
)

class Order(models.Model):
    status = models.CharField(max_length=120,
                              choices=ORDER_STATUS,
                              default='created')
                              
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT)

    billing_address = models.CharField(max_length=900)

    shipping_address = models.CharField(max_length=900)

    order_total = models.DecimalField(max_digits=50,
                                      decimal_places=2)

    order_date = models.DateTimeField(auto_now_add=True)
    
    @property
    def is_completed(self):
        return True if self.status == "paid" else False
