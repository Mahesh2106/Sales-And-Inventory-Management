from accounts.models import Vendor
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.models import Profile
from store.models import Item,Delivery,Category
from transactions.models import Sale
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django_tables2 import SingleTableView
import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport

from . import models
from .tables import ItemTable, DeliveryTable
from django.db.models import Sum, Avg
from .forms import ProductForm
from functools import reduce
from django.db.models import Q
import operator
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta


from django.views.generic import View
from django.http import JsonResponse, HttpResponse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import ProductFilter

@login_required
def dashboard(request):
    profiles = Profile.objects.all()
    categories = Category.objects.annotate(nitem=Count('item'))
    cat=Category.objects.all()
    items = Item.objects.all()
    total_items = Item.objects.all().aggregate(Sum('quantity')).get('quantity__sum', 0.00)
    items_count = items.count()
    profiles_count = profiles.count()



    #profile pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(profiles, 3)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)

    #items pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 4)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    category_totals = Sale.objects.values('item__category__name').annotate(total_sold=Sum('quantity'))

    overall_total_sold = Sale.objects.aggregate(Sum('quantity'))['quantity__sum']

    category_percentages = []
    for category_total in category_totals:
        category_name = category_total['item__category__name']
        total_sold = category_total['total_sold']

        if overall_total_sold > 0:
            percentage_sold = round((total_sold / overall_total_sold) * 100,2)
        else:
            percentage_sold = 0

        category_percentages.append({'category_name': category_name, 'percentage_sold': percentage_sold})

    context = {
        'items': items,
        'profiles': profiles,
        'profiles_count': profiles_count,
        'items_count': total_items,
        'total_items': total_items,
        'vendors': Vendor.objects.all(),
        'delivery': Delivery.objects.all(),
        'sales': Sale.objects.all(),
        'cat':cat,
        'category_percentages':category_percentages

    }
    return render(request, 'store/dashboard.html', context)



class ProductListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = Item
    table_class = ItemTable
    template_name = 'store/productslist.html'
    context_object_name = 'items'
    paginate_by = 10
    SingleTableView.table_pagination = False



from django.utils import timezone
from datetime import timedelta
from .models import Item

from django.utils import timezone
from datetime import timedelta
from .models import Item, Notification


def notify_close_to_expiry(request):
    # Threshold for items close to expiry
    threshold = timezone.now() + timedelta(days=7)

    # Fetch items close to expiry within the threshold
    items_close_to_expiry = Item.objects.filter(expiring_date__lte=threshold)

    for item in items_close_to_expiry:
        item.selling_price = item.selling_price - float(item.selling_price * 0.4)
        item.save()

    expired_items = items_close_to_expiry.filter(expiring_date__lte=timezone.now())
    expired_items.delete()

    # Notification closing section
    unread_notifications = Notification.objects.filter(read=False)

    for notification in unread_notifications:
        notification.read = True
        notification.save()

    num = items_close_to_expiry.count()

    return render(request, "store/notification.html", {'items_close_to_expiry': items_close_to_expiry, 'num': num})


class ItemSearchListView(ProductListView):
    paginate_by = 10

    def get_queryset(self):
        result = super(ItemSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list))
            )
        return result

class ProductDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Item
    template_name = 'store/productdetail.html'

    def get_success_url(self):
        return reverse('product-detail', kwargs={'slug': self.object.slug})

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'store/productcreate.html'
    form_class = ProductForm
    success_url = '/products'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self,request):
        #item = Item.objects.get(id=pk)
        if request.POST.get("quantity") < 1:
            return False
        else:
            return True

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    template_name = 'store/productupdate.html'
    fields = ['name','category','quantity','selling_price', 'expiring_date', 'vendor']
    success_url = '/products'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'store/productdelete.html'
    success_url = '/products'


    def test_func(self):
        item = self.get_object()
        if self.request.user.is_superuser:
            return True
        else:
            return False

# Delivery
class DeliveryListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = Delivery
    pagination = 10
    template_name = 'store/deliveries.html'
    context_object_name = 'deliveries'

class DeliverySearchListView(DeliveryListView):
    paginate_by = 10

    def get_queryset(self):
        result = super(DeliverySearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(customer_name__icontains=q) for q in query_list))
            )
        return result

class DeliveryDetailView(LoginRequiredMixin, DetailView):
    model = Delivery
    template_name = 'store/deliverydetail.html'
class DeliveryCreateView(LoginRequiredMixin, CreateView):
    model = Delivery
    fields = ['item', 'customer_name', 'phone_number', 'location', 'date','is_delivered']
    template_name = 'store/deliveriescreate.html'
    success_url = '/deliveries'

    def form_valid(self, form):
        return super().form_valid(form)

class DeliveryUpdateView(LoginRequiredMixin, UpdateView):
    model = Delivery
    fields = ['item', 'customer_name', 'phone_number', 'location', 'date','is_delivered']
    template_name = 'store/deliveryupdate.html'
    success_url = '/deliveries'

    def form_valid(self, form):
        return super().form_valid(form)


class DeliveryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Delivery
    template_name = 'store/productdelete.html'
    success_url = '/deliveries'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False

import qrcode

def generate_qr_code(request, item_id):
    item = Item.objects.get(id=item_id)  # Replace YourModel with your actual model
    data = f'Item ID: {item.id}, Name: {item.name},category:{item.category},selling_price:{item.selling_price},expiring_date:{item.expiring_date},vendor:{item.vendor}'  # Customize this based on your model structure

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Serve the image
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response


from django.shortcuts import render
