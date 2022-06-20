from django.shortcuts import render
import json
from shopping.models import CategorySub, Customer, Order, OrderItem, Product, ProductImage, Variation
from django.db.models import Avg, Count, Min, Sum
from datetime import date, timedelta
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay, TruncMonth
# Create your views here.


def dashboard(request):
    today_mony = Product.objects.aggregate(total_price=Sum('price'))
    today_profit = Product.objects.aggregate(total_price=Sum('profit'))
    new_order = Order.objects.filter(
        date_ordered__day=date.today().day).count()
    new_clients = Customer.objects.filter(
        created_at__day=date.today().day).count()
    num_users = Customer.objects.all().count()
    num_partners = Customer.objects.filter(is_receveur=True).count()
    num_orders = Order.objects.all().count()
    num_products = Product.objects.all().count()
    num_promotors = Customer.objects.filter(is_receveur=True)
    # dashboard chart graphic
    chart_data = (
        Order.objects.annotate(date=TruncMonth("date_ordered"))
        .values("date")
        .annotate(y=Count("id"))
        .order_by("-date")
    )
    as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
    context = {
        "chart_data": as_json,
        "today_mony": today_mony,
        "today_profit": today_profit,
        "new_order": new_order,
        "new_clients": new_clients,
        "num_users": num_users,
        "num_partners": num_partners,
        "num_orders": num_orders,
        "num_products": num_products,
        "num_promotors": num_promotors,
        "titel":"Accueil"
    }
    return render(request, 'dashboard/pages/dashboard.html', context)


def tables(request):
    orders = Order.objects.filter(complete=True).order_by("-date_ordered")
    orders_no_complete = Order.objects.filter(complete=False).count()

    context = {"orders": orders, "titel": "orders","orders_no_complete":orders_no_complete}

    return render(request, "dashboard/pages/tables.html", context)


def order_detail(request, pk):
    order_id = Order.objects.get(id=pk)
    order_items = OrderItem.objects.filter(order=order_id)
    context = {"order_items": order_items,
               "order_id": order_id, "titel": "order details"}
    return render(request, 'dashboard/pages/order_detail.html', context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price1 = float(request.POST['price1'])
        price2 = float(request.POST['price2'])
        category = request.POST['category']
        quantity = int(request.POST['quantity'])
        description = request.POST['description']
        images=request.FILES.getlist("images")
        image=request.FILES.get("image")
        
        #size = request.POST.get('size')
        print(images)
        category_id = CategorySub.objects.get(name=category)
        
        try:
            product = Product(   name=name,
                                  category=category_id,
                                  price_achat=price1,
                                  price=price2,
                                  quantity=quantity,
                                  description=description,
                                  image=image)
            product.save()
            print("product_ref",product.id)  
            # using session for adding product variations later
            request.session['product_ref'] = product.id
            for i in images: 
                p = ProductImage(product=product,image=i) 
                p.save()
                print("success")
        except:
            print("error")
    context = {"category": CategorySub.objects.all, "titel": "add product"}
    return render(request, 'dashboard/pages/add_product.html', context)
