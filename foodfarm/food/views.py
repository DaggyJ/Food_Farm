from django.shortcuts import render,redirect
from django.views import View
from . import models
from food.models import Cart, Product
from . import forms
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'food/index.html')

def about(request):
    return render(request, 'food/about.html')

def contact(request):
    return render(request, 'food/contact.html')





def cart(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    else:
        cart_items = Cart.objects.filter(user=request.user)
        total_amount = sum([item.total_price() for item in cart_items])

        return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})



class CategoryView(View):
    def get(self, request, val):
        product = models.Product.objects.filter(category=val)
        title = models.Product.objects.filter(category=val).values('title')
        return render(request, 'food/category.html', locals())
    
class CategoryTitle(View):
    def get(self, request, val):
        product = models.Product.objects.filter(title=val)
        title = models.Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'food/category.html', locals())

class ProductDetailView(View):
    def get(self, request, pk):
        product = models.Product.objects.get(pk=pk)
        return render(request, 'food/productdetail.html',locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = forms.CustomUserCreationForm()
        return render(request, 'food/registration.html', locals())
    
    def post(self, request):
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.warning(request, 'Incorrect input!, Please try again')
            return render(request, 'food/registration.html', locals())
        


class ProfileView(View):
    def get(self, request):
        form = forms.CustomerProfileForm()
        return render(request, 'food/profile.html',locals())
    def post(self, request):
        form = forms.CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            

            reg = models.Customer(name=name,locality=locality,city=city,mobile=mobile)
            #reg.save()
            messages.success(request, 'Congratulations!, your profile is successfully saved')
        else:
            messages.warning(request, 'Incorrect input!, Please try again')
        return render(request, 'food/profile.html',locals())
                  