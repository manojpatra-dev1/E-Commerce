from django.db import models
from .category import Category
from django.core.validators import MinValueValidator, MaxValueValidator


# =========================
# CUSTOMER MODEL
# =========================
class Customer(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)

    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


# =========================
# PRODUCT MODEL
# =========================
class Product(models.Model):

    name = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    image = models.ImageField(upload_to='products/')

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    # ✅ FIXED: better decimal precision
    rating = models.DecimalField(
        max_digits=3,  # changed from 2 → 3
        decimal_places=1,
        default=4.0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    # =========================
    # METHODS
    # =========================

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category_id=category_id)
        return Product.get_all_products()

    @property
    def discount_percentage(self):
        if self.old_price > 0:
            discount = (
                (self.old_price - self.price) / self.old_price
            ) * 100
            return round(discount)
        return 0

    @property
    def saving_amount(self):
        return self.old_price - self.price

    def __str__(self):
        return self.name