from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' , views.home_view,name='home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
    # path('profile/',views.product_view,name='profile'),
    # path('product/',views.product_view,name='product'),
    path('search', views.search, name='search'),
    path('all', views.all_view, name='all'),
    path('pharmacy', views.pharmacy_view, name='pharmacy'),
    path('fruits', views.fruits_view, name='fruits'),
    path('beauty', views.beauty_view, name='beauty'),
    path('snacks', views.snacks_view, name='snacks'),
    path('faq',views.faq_view,name='faq'),
    path('cart', views.cart_view, name='cart'),
    path('checkout', views.checkout_view, name='checkout'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
