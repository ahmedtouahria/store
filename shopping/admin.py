from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'category', 'available', 'avg_rating')
    search_fields = ('category', 'name')
    readonly_fields = ('barcode_num', 'profit','num_views')
    actions = ['set_product_avaiable', ]
    '''  def set_product_avaiable(self,request,queryset):
        queryset.update(available=True)
    def has_delete_permission(self, request, obj=None):
        return False '''


class FavoritectAdmin(admin.ModelAdmin):
    model = Favorite
    list_display = ('customer', 'product', 'create_at',)
    search_fields = ('customer', 'product')


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('product', 'order', 'quantity', 'date_added')
    search_fields = ('category', 'name')


class ShippingAddressAdmin(admin.ModelAdmin):
    model = ShippingAddress
    list_display = ('customer', 'order', 'city', 'state', 'date_added')


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('customer', 'id', 'date_ordered',
                    'complete', 'transaction_id')
    readonly_fields = ('transaction_id', 'customer_number', 'recommended_by')
   #fieldsets = ((None, {'fields': ('customer', 'complete',)}), )


class RatingAdmin(admin.ModelAdmin):
    models = Rating
    list_display = ('user', 'product', 'stars')


class BannerImage(admin.ModelAdmin):
    model = ImageBanner


class Category_sub_admin(admin.ModelAdmin):
    model = CategorySub


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Favorite, FavoritectAdmin)
admin.site.register(ImageBanner, BannerImage)
admin.site.register(Section)

admin.site.register(ToastMessage)
admin.site.register(Affaire)

admin.site.register(ProductImage)
admin.site.register(Conversion)

admin.site.register(CategorySub, Category_sub_admin)
admin.site.register(Rating, RatingAdmin)
