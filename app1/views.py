from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import Laptops, Monitors, Printers, Headphones,Customer,Cart,OrderPlaced
from .forms import UserRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def  Home(request):
    return render(request,'Home.html')

def laptops(request, use):
    if use == 'all':
        data = Laptops.objects.all()
    elif use == 'home':
        data = Laptops.objects.filter(Uses = 'Home')
    elif use == 'business':
        data = Laptops.objects.filter(Uses = 'Business')
    elif use == 'gaming':
        data = Laptops.objects.filter(Uses = 'Gaming')
    elif use == 'student':
        data = Laptops.objects.filter(Uses = 'Student')
    elif use == 'premium':
        data = Laptops.objects.filter(Uses = 'Premium')
    return render(request,'products_laptops.html', {"data":data})


def monitors(request, use):
    if use == 'all':
        data = Monitors.objects.all()
    elif use == 'home':
        data = Monitors.objects.filter(Uses = 'Home')
    elif use == 'business':
        data = Monitors.objects.filter(Uses = 'Business')
    elif use == 'gaming':
        data = Monitors.objects.filter(Uses = 'Gaming')

    return render(request,'products_monitors.html', {"data":data})


def printers(request, use):
    if use == 'all':
        data = Printers.objects.all()
    elif use == 'home':
        data = Printers.objects.filter(Uses = 'Home/office')
    elif use == 'A3 printers':
        data = Printers.objects.filter(Uses = 'A3 printers')
    elif use == 'laser':
        data = Printers.objects.filter(Uses = 'Laser printers')

    return render(request,'products_printers.html', {"data":data})


def headphones(request, category):
    if category == 'all':
        data = Headphones.objects.all()
    elif category == 'wired':
        data = Headphones.objects.filter(Category = 'Wired')
    elif category == 'wireless':
        data = Headphones.objects.filter(Category = 'Wireless')
    elif category == 'earbuds':
        data = Headphones.objects.filter(Category = 'Earbuds')

    return render(request,'products_headphones.html', {"data":data})


class UserRegistrationView(View):
    def get(self,request):
        form = UserRegistrationForm()
        return render(request,'register.html',{'form':form})

    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! Account Created successfully ')
            form.save()
        return redirect('login')


@method_decorator(login_required,name = 'dispatch')
class ProfileView(View):
    def get(self,request):
        form  = CustomerProfileForm()
        return render(request,'profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            Contact_No = form.cleaned_data['Contact_No']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            dump = Customer(user = usr,first_name=first_name,last_name = last_name,Contact_No= Contact_No,
                            locality = locality, city = city , state = state , zipcode = zipcode)

            dump.save()
            messages.success(request,'Profile Updated successfully')
        return render(request,'profile.html',{'form':form,'active': 'btn-primary'})

@login_required
def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'address.html',{'add':add,'active':'btn-primary'})


@login_required
def add_to_cart(request, id , category):
    user = request.user
    product_id = id
    category = category
    Cart(user = user,product_id = product_id,category=category).save()
    return redirect('/cart')

@login_required
def Mycart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = Cart.objects.filter(user = user)
        if carts:
            amount = 0.0
            Shipping_charges = 70.0
            total_amount = 0.0
            context = {}
            for cart in carts:
                if cart.category == 'laptop':
                    l = Laptops.objects.get(LID = cart.product_id)
                    amount = amount + (cart.quantity * float(l.Price))
                    if 'laptop' in context:
                        context['laptop'].append(l)
                    else:
                        context['laptop'] = [l]
                elif cart.category == 'monitor':
                    m = Monitors.objects.get( MID = cart.product_id)
                    amount = amount + (cart.quantity * float(m.Price))
                    if 'monitor' in context:
                        context['monitor'].append(m)
                    else:
                        context['monitor'] = [m]
                elif cart.category == 'printer':
                    pr = Printers.objects.get(PID = cart.product_id)
                    amount = amount + (cart.quantity * float(pr.Price))
                    if 'printer' in context:
                        context['printer'].append(pr)
                    else:
                        context['printer'] = [pr]
                elif cart.category == 'headphone':
                    h = Headphones.objects.get(HID = cart.product_id)
                    amount = amount + (cart.quantity * float(h.Price))
                    if 'headphone' in context:
                        context['headphone'].append(h)
                    else:
                        context['headphone'] = [h]
            total_amount = Shipping_charges + amount
            context.update({'amount':amount,'total_amount':total_amount,})
            return render(request, 'addtocart.html',context)
        else:
            return render(request, 'emptycart.html')



def Removeitem(request,id,category):
    print(id)
    print(category)
    if request.user.is_authenticated:
        user  = request.user
        carts = Cart.objects.filter(user = user)
        print(carts)
        for cart in carts:
            cart_id = cart.id
            if category == cart.category:
                a = Cart.objects.filter(id = cart_id,product_id = id)
                a.delete()
                return redirect('cart')



def checkout(request):
    user  = request.user
    add = Customer.objects.filter(user = user)
    carts = Cart.objects.filter(user = user)
    if carts:
        amount = 0.0
        Shipping_charges = 70.0
        total_amount = 0.0
        context = {}
        for cart in carts:
            if cart.category == 'laptop':
                l = Laptops.objects.get(LID = cart.product_id)
                amount = amount + (cart.quantity * float(l.Price))
                if 'laptop' in context:
                    context['laptop'].append(l)
                else:
                    context['laptop'] = [l]
            elif cart.category == 'monitor':
                m = Monitors.objects.get( MID = cart.product_id)
                amount = amount + (cart.quantity * float(m.Price))
                if 'monitor' in context:
                    context['monitor'].append(m)
                else:
                    context['monitor'] = [m]
            elif cart.category == 'printer':
                pr = Printers.objects.get(PID = cart.product_id)
                amount = amount + (cart.quantity * float(pr.Price))
                if 'printer' in context:
                    context['printer'].append(pr)
                else:
                    context['printer'] = [pr]
            elif cart.category == 'headphone':
                h = Headphones.objects.get(HID = cart.product_id)
                amount = amount + (cart.quantity * float(h.Price))
                if 'headphone' in context:
                    context['headphone'].append(h)
                else:
                    context['headphone'] = [h]
        total_amount = Shipping_charges + amount
        context.update({'amount':amount,'total_amount':total_amount,'add':add})
        return render(request, 'checkout.html', context)

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id = custid)
    carts = Cart.objects.filter(user = user)
    for cart in carts:
        OrderPlaced(user = user, customer = customer, product_id = cart.product_id, category = cart.category).save()
        cart.delete()
    return redirect('orders')

@login_required
def orders(request):
    OP = OrderPlaced.objects.filter(user = request.user)
    if OP:
        amount = 0.0
        Shipping_charges = 70.0
        total_amount = 0.0
        context = {}
        for i in OP:
            if i.category == 'laptop':
                l = Laptops.objects.get(LID = i.product_id)
                amount = amount + (i.quantity * float(l.Price))
                if 'laptop' in context:
                    context['laptop'].append(l)
                else:
                    context['laptop'] = [l]
            elif i.category == 'monitor':
                m = Monitors.objects.get( MID = i.product_id)
                amount = amount + (i.quantity * float(m.Price))
                if 'monitor' in context:
                    context['monitor'].append(m)
                else:
                    context['monitor'] = [m]
            elif i.category == 'printer':
                pr = Printers.objects.get(PID = i.product_id)
                amount = amount + (i.quantity * float(pr.Price))
                if 'printer' in context:
                    context['printer'].append(pr)
                else:
                    context['printer'] = [pr]
            elif i.category == 'headphone':
                h = Headphones.objects.get(HID = i.product_id)
                amount = amount + (i.quantity * float(h.Price))
                if 'headphone' in context:
                    context['headphone'].append(h)
                else:
                    context['headphone'] = [h]
        total_amount = Shipping_charges + amount
        context.update({'amount':amount,'total_amount':total_amount,'op':OP})
        return render(request, 'orders.html',context)





