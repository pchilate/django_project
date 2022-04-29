from django.urls import path
from app1 import views
from app1.views import UserRegistrationForm
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordResetForm,MysSetPasswordForm


urlpatterns = [
           path('', views.Home, name = 'home'),
           path('products/laptops/<use>', views.laptops, name = 'laptops'),
           path('products/monitors/<use>', views.monitors, name = 'monitors'),
           path('products/printers/<use>', views.printers, name = 'printers'),
           path('products/headphones/<category>', views.headphones, name = 'headphones'),


           path('registration',views.UserRegistrationView.as_view(),name = 'registration'),
           path('accounts/login/', auth_views.LoginView.as_view(template_name = 'login.html',
           authentication_form = LoginForm)  , name='login'),
           path('logout/',auth_views.LogoutView.as_view(next_page = 'login'),name = 'logout'),
           path('profile/', views.ProfileView.as_view(), name='profile'),

           path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'password_reset.html',
            form_class = MyPasswordResetForm), name = 'password_reset'),

           path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html',),
           name = 'password_reset_done'),

           path('password-reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html',
           form_class = MysSetPasswordForm),name = 'password_reset_confirm'),

           path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html',),
           name = 'password_reset_complete'),


             path('address/', views.address, name='address'),
             path('add_to_cart/<id>/<category>', views.add_to_cart, name='add-to-cart'),
             path('cart/', views.Mycart, name='cart'),
             path('remove/<id>/<category>', views.Removeitem, name='remove'),
             path('checkout/', views.checkout, name='checkout'),
             path('paymentdone/', views.payment_done,name= "paymentdone"),
             path('orders/', views.orders, name='orders'),




]
