from django.urls import path
from shop import views

urlpatterns = [
    path('',views.index, name="ShopHome"),
    path('home/',views.home, name="home"),
    path('profile/',views.profile, name="profile"),
    path('base/',views.base, name="base"),
    path('about/',views.about, name="AboutUs"),
    path('contact/',views.contact, name="ContactUs"),
    path('sell/',views.sell, name="Sell"),
    path('tracker/',views.tracker, name="TrackingStatus"),
    path('',views.search, name="Search"),
    path('productview/<int:id>',views.productview, name="ProdictView"),
    # path('checkout/',views.checkout, name="Checkout"),
    path('checkout_page/',views.Checkout, name="checkout"),
    path('buynow/',views.buynow, name="Buynow"),
    path('cart/',views.cart,name="Cart"),
    path('update/',views.updateItem,name="update"),
    path('payment/',views.payment,name="payment"),
    path('process_payment/', views.processPayment, name='process_payment'),
    # path('checkout/',views.home, name="checkout"),

    path('help',views.help, name="Help"),
    path('registry',views.registry, name="Registry"),
    path('customer',views.customer, name="Customer"),

    # path('accounts/signup/',views.signup,name="account_signup"),

    # path('zoom/',views.zoom, name="zoom"),
# 
    path('filter',views.filter, name="Filter"),
    # path('filters/', views.ProductListView.as_view(), name="Filters"),


]
