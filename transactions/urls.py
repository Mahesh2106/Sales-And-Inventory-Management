from django.urls import path
from transactions import views
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    PurchaseListView,
    PurchaseDetailView,
    PurchaseCreateView,
    PurchaseUpdateView,
    PurchaseDeleteView,
    SaleListView,
    SaleDetailView,
    SaleUpdateView,
    SaleDeleteView,

)

app_name='transactions'

urlpatterns = [
    path('purchases/', PurchaseListView.as_view(), name="purchaseslist"),
    path('purchase/<slug:slug>/',PurchaseDetailView.as_view(), name='purchase-detail'),
    path('new-purchase/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('purchase/<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase-update'),
    path('purchase/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase-delete'),
    path('sales/',SaleListView.as_view(), name="saleslist"),
    path('sale/<int:pk>/', SaleDetailView.as_view(), name='sale-detail'),
    path('sale/<slug:slug>/update/', SaleUpdateView.as_view(), name='sale-update'),
    path('sale/<slug:slug>/delete/', SaleDeleteView.as_view(), name='sale-delete'),
    path('delete_bill/',views.delete_bill,name='delete_bill'),
    path('add_item/<slug:slug>/',views.add_item,name='add_item'),
    path('billing_details/',views.billing_details,name='billing_details'),
    path('delete_bill_single/<str:product_name_to_delete>',views.delete_bill_single,name='delete_bill_single'),
    path('generate_bill/',views.generate_bill,name='generate_bill'),
    path('sale-delete/<int:pk>/',views.sale_delete,name='sale-delete'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)