from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm, MyPaswordResetForm
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    path('category-title/<val>/', views.CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),


    # user authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='registration'),
    path('account/login/', auth_view.LoginView.as_view(template_name='food/login.html', authentication_form= LoginForm ), name='login'),
    path('account/login/', auth_view.LogoutView.as_view(template_name='food/logout.html'), name='logout'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='food/password-reset.html', form_class= MyPaswordResetForm ), name='password-reset'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
