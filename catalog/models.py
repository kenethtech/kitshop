from django.db import models
from django.urls import reverse


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)


class Category(models.Model):
    objects = models.Manager()
    active = ActiveCategoryManager()


    name =models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text= 'Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta keywords", max_length=255, help_text= 'Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for desription meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('catalog_category', args= [self.slug])


class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(is_active =True)

class FeaturedProductManager(models.Manager):
    def get_query_set(self):
        return super(FeaturedProductManager, self).get_query_set.filter(is_featured=True)


class Product(models.Model):
    objects = models.Manager()
    active = ActiveProductManager()
    featured = FeaturedProductManager()


    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='images/products/main')
    thumbnail = models.ImageField(upload_to='images/products/thumbnails')
    image_caption = models.CharField(max_length=200)





    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', args=[self.slug])



    def sale_price(self):
        if self.old_price >self.price:
            return self.price
        else:
            return None

    #order-based filtering product recommendation
    def cross_sells(self):
        from checkout.models import Order, OrderItem
        orders = Order.objects.filter(orderitem__product=self)
        order_items = OrderItem.objects.filter(order__in=orders).exclude(product=self)
        products = Product.active.filter(orderitem__in=order_items).distinct()
        return products

    #customer-based product recommendation

    def cross_sells_user(self):
        from checkout.models import Order, OrderItem
        from django.contrib.auth.models import User
        users = User.objects.filter(order__orderitem__product=self)
        items = OrderItem.objects.filter(order__user__in=users).exclude(product=self)
        products = Product.active.filter(orderitem__in=items).distinct()
        return products

    #Product recommendation using the same category
    def cross_sells_category(self):
        category = Category.active.filter(product=self)
        products = Product.active.filter(categories__in=category).exclude(name=self).distinct()
        return products

    #combined order and customer based order filtering
    def cross_sells_hybrid(self):
        from checkout.models import Order, OrderItem
        from django.contrib.auth.models import User
        from django.db.models import Q

        orders = Order.objects.filter(orderitem__product=self)
        users = User.objects.filter(order__orderitem__product=self)
        items = OrderItem.objects.filter(Q(order__in=orders)| Q(order__user__in=users)).exclude(product=self)
        products = Product.active.filter(orderitem__in=items).distinct()
        return products


# Create your models here.
