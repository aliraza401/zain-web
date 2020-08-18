from django.contrib import admin
from shop.models import Product,Contact,Subscribers,ProductImgae, Customer, Order, OrderItem,Checkout,Payment,Help

# class all(admin.TabularInline):
#     model=ProductImgae
#     extra=5

# class images(admin.ModelAdmin):
#     inline=[all]

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Contact)
admin.site.register(Subscribers)
admin.site.register(ProductImgae)
admin.site.register(Checkout)
admin.site.register(Payment)
admin.site.register(Help)




