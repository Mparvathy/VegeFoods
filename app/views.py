from django.shortcuts import render,redirect
from app.models import customuser,Product,Veg,Cart,Account,Fruit,Juice,ContactMessage
from django. contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django. contrib.auth  import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Order, OrderItem, Cart,CartItem
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, VegForm,FruitForm,JuiceForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Veg, Wishlist


def is_admin_user(user):
    return user.is_authenticated and user.is_superuser


def adminsignup(request):
    if (request.method=='POST'):
         u=request.POST['u']
         e=request.POST['e']
         p=request.POST['p']
         n=request.POST['n']
         full_name = request.POST['full_name']
         u=customuser.objects.create_user(username=u,email=e,password=p,phone=n)
         u.full_name = full_name
         u.is_admin=True
         u.is_superuser=True
         u.is_staff=True
         u.save()
         return redirect('login')
    return render(request,'adminsignup.html')

def usersignup(request):
    if (request.method=='POST'):
        u=request.POST['u']
        full_name = request.POST['full_name']
        e=request.POST['e']
        p=request.POST['p']
        n=request.POST['n']
        u=customuser.objects.create_user(username=u,email=e,password=p,phone=n)
        u.full_name = full_name
        u.is_user=True
        u.is_staff=True
        u.save()
        return redirect('login')
    return render(request,'usersignup.html')



@user_passes_test(is_admin_user)
def contact_messages(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'contact_messages.html', {'messages': messages})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('u')
        password = request.POST.get('p')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login failed. Invalid credentials. Please try again.')
            return redirect('login')     
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    k = Product.objects.all()
    return render(request, "home.html", {"b": k, 'request': request})


def about(request):
    return  render(request,'about.html')






def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
        return redirect('home')
    return render(request, 'contact.html')


def delete_contact_message(request, id):
    if request.method == 'POST':
        message = get_object_or_404(ContactMessage, id=id)
        message.delete()
    return redirect('contact_messages')

 

def shop(request):
    k = Product.objects.all()
    return render(request, "shop.html", {"b": k, 'request': request})

def vegetable_list(request):
    k=Veg.objects.all()
    return render(request, "vegetables.html", {"b": k, 'request': request})

def fruit_list(request):
    k=Fruit.objects.all()
    return render(request, "fruit.html", {"b": k, 'request': request})


def juice_list(request):
    k=Juice.objects.all()
    return render(request, "juice.html", {"b": k, 'request': request})


def view(request,p):
    k=Product.objects.get(id=p)
    return render(request,'product-single.html',{'b':k,})

def view1(request,p):
    k=Veg.objects.get(id=p)
    return render(request,'view.html',{'b':k})

def view2(request,p):
    k=Fruit.objects.get(id=p)
    return render(request,'view1.html',{'b':k})


def view3(request,p):
    k=Juice.objects.get(id=p)
    return render(request,'view2.html',{'b':k})

def add_product(request):
    if request.method == 'POST':
        if 'product' in request.POST:
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product_form.save()
                return redirect('shop')
        elif 'veg' in request.POST:
            veg_form = VegForm(request.POST, request.FILES)
            if veg_form.is_valid():
                veg_form.save()
                return redirect('vegetable_list')
        elif 'fruit' in request.POST:
            fruit_form = FruitForm(request.POST, request.FILES)
            if fruit_form.is_valid():
                fruit_form.save()
                return redirect('fruit_list')    
        elif 'juice' in request.POST:
            juice_form = JuiceForm(request.POST, request.FILES)
            if juice_form.is_valid():
                juice_form.save()
                return redirect('juice_list')
    else:
        product_form = ProductForm()
        veg_form = VegForm()
        fruit_form = FruitForm()    
        juice_form = JuiceForm()
    return render(request, 'add_product.html', {
        'product_form': product_form,
        'veg_form': veg_form,
        'fruit_form': fruit_form,
        'juice_form': juice_form
    })

@login_required
def update_product(request, p_id):
    product = get_object_or_404(Product, id=p_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop')  # Redirect to the shop page or wherever appropriate
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'update_product.html', {'form': form, 'product': product})

@login_required
def update_veg(request, v_id):
    veg = get_object_or_404(Veg, id=v_id)
    
    if request.method == 'POST':
        form = VegForm(request.POST, request.FILES, instance=veg)
        if form.is_valid():
            form.save()
        
            return redirect('vegetable_list')  # Redirect to the vegetable list page or wherever appropriate
    else:
        form = VegForm(instance=veg)
    
    return render(request, 'update_veg.html', {'form': form, 'veg': veg})

@login_required
def update_fruit(request, f_id):
    fruit = get_object_or_404(Fruit,id=f_id)
    if request.method == 'POST':
        form = VegForm(request.POST, request.FILES, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('fruit_list')  # Redirect to the vegetable list page or wherever appropriate
    else:
        form = FruitForm(instance=fruit) 
    return render(request, 'update_fruit.html', {'form': form, 'fruit':fruit})

@login_required
def update_juice(request, j_id):
    juice = get_object_or_404(Juice,id=j_id)
    if request.method == 'POST':
        form = JuiceForm(request.POST, request.FILES, instance=juice)
        if form.is_valid():
            form.save()
            messages.success(request, "Juice updated successfully.")
            return redirect('juice_list')  # Redirect to the vegetable list page or wherever appropriate
    else:
        form = JuiceForm(instance=juice) 
    return render(request, 'update_juice.html', {'form': form, 'juice':juice})

def delete_product(request, id):
    b= Product.objects.get(id=id)
    b.delete()
    return  shop(request)

def delete_veg(request, id):
    b= Veg.objects.get(id=id)
    b.delete()
    return  vegetable_list(request)

def delete_fruit(request, id):
    b= Fruit.objects.get(id=id)
    b.delete()
    return  fruit_list(request)

def delete_juice(request, id):
    b= Juice.objects.get(id=id)
    b.delete()
    return  juice_list(request)

@login_required
def add_to_cart(request, b, item_type):
    if item_type == 'product':
        try:
            product = Product.objects.get(id=b)
            cart, created = Cart.objects.get_or_create(user=request.user, product=product, veg=None, defaults={'quantity': 1})
            if not created:
                cart.quantity += 1
                cart.save()
        except Product.DoesNotExist:
            messages.error(request, "Product does not exist.")
            return redirect('shop')
    elif item_type == 'veg':
        try:
            veg = Veg.objects.get(id=b)
            cart, created = Cart.objects.get_or_create(user=request.user, product=None, veg=veg, defaults={'quantity': 1})
            if not created:
                cart.quantity += 1
                cart.save()
        except Veg.DoesNotExist:
            messages.error(request, "Vegetable does not exist.")
            return redirect('vegetable_list')
    elif item_type == 'fruit':
        try:
            fruit = Fruit.objects.get(id=b)
            cart, created = Cart.objects.get_or_create(user=request.user, product=None,fruit=fruit, defaults={'quantity': 1})
            if not created:
                cart.quantity += 1
                cart.save()
        except Fruit.DoesNotExist:
            messages.error(request, "Fruit does not exist.")
            return redirect('fruit_list')  
    elif item_type == 'juice':
        try:
            juice = Juice.objects.get(id=b)
            cart, created = Cart.objects.get_or_create(user=request.user, product=None,juice=juice, defaults={'quantity': 1})
            if not created:
                cart.quantity += 1
                cart.save()
        except Juice.DoesNotExist:
            messages.error(request, "Juice does not exist.")
            return redirect('juice_list')        
    else:
        messages.error(request, "Invalid item type.")
        return redirect('shop')
    return redirect('cart')




@login_required
def cartview(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    subtotal = 0

    for item in cart_items:
        subtotal += item.subtotal()

    total = subtotal
    return render(request, 'cart.html', {'cart': cart_items, 'subtotal': subtotal, 'total': total})

@login_required
def cart_delete(request, item_id, item_type):
    if item_type == 'product':
        try:
            cart_item = Cart.objects.get(user=request.user, product_id=item_id, veg=None)
            cart_item.delete()
        except Cart.DoesNotExist:
            messages.error(request, "Item not found in cart.")
    elif item_type == 'veg':
        try:
            cart_item = Cart.objects.get(user=request.user, veg_id=item_id, product=None)
            cart_item.delete()
        except Cart.DoesNotExist:
            messages.error(request, "Item not found in cart.")
    elif item_type == 'fruit':
        try:
            cart_item = Cart.objects.get(user=request.user, fruit_id=item_id, product=None)
            cart_item.delete()
        except Cart.DoesNotExist:
            messages.error(request, "Item not found in cart.")        
    elif item_type == 'juice':
        try:
            cart_item = Cart.objects.get(user=request.user, juice_id=item_id, product=None)
            cart_item.delete()
        except Cart.DoesNotExist:
            messages.error(request, "Item not found in cart.")     
    else:
        messages.error(request, "Invalid item type.")
    
    return redirect('cart')

@login_required
def checkout(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        street_address = request.POST.get('street_address')
        phone = request.POST.get('phone')
        email_address = request.POST.get('email_address')
        terms_accepted = request.POST.get('terms')  # Checkbox field
        account_number = request.POST.get('account_number')  # Account number from form

        # Basic validation
        errors = []
        if not first_name or not last_name or not street_address or not phone or not email_address:
            errors.append("All fields are required.")
        if not terms_accepted:
            errors.append("You must accept the terms and conditions.")
        
        # Validate account number
        try:
            account_number = Account.objects.get(account_number=account_number)
        except Account.DoesNotExist:
            errors.append("Account number does not exist. Please enter a valid account number.")
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('checkout')

        # Get cart items for the logged-in user
        cart = Cart.objects.filter(user=request.user)
        
        # Calculate totals
        subtotal = sum(
            item.quantity * (
                item.product.price if item.product else 
                item.veg.price if item.veg else 
                item.fruit.price if item.fruit else 
                item.juice.price
            ) 
            for item in cart
        )
        total = subtotal
        
        # Create the order
        order = Order.objects.create(
            user=request.user,
            address=street_address,
            phone=phone,
            total=total
        )

        # Create order items
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                veg=item.veg,
                fruit=item.fruit,
                juice=item.juice,
                quantity=item.quantity,
                price=(
                    item.product.price if item.product else 
                    item.veg.price if item.veg else 
                    item.fruit.price if item.fruit else 
                    item.juice.price
                ),
                total=(
            item.quantity * (
                item.product.price if item.product else 
                item.veg.price if item.veg else 
                item.fruit.price if item.fruit else 
                item.juice.price
            )
        )
            )
        
        # Remove items from wishlist if they were in the cart
        for item in cart:
            if item.product:
                Wishlist.objects.filter(user=request.user, product=item.product).delete()
            if item.veg:
                Wishlist.objects.filter(user=request.user, veg=item.veg).delete()
            if item.fruit:
                Wishlist.objects.filter(user=request.user, fruit=item.fruit).delete()
            if item.juice:
                Wishlist.objects.filter(user=request.user, juice=item.juice).delete()

        # Clear the cart after checkout
        cart.delete()
        
        context = {
            'address': street_address,
            'phone': phone,
            'total': total,
            'account_number': account_number,
            'order_id': order.id  # Pass order_id to the final page
        }
        
        return render(request, 'final.html', context)
    
    # For GET requests, calculate the cart totals and display them
    cart = Cart.objects.filter(user=request.user)
    subtotal = sum(
        item.quantity * (
            item.product.price if item.product else 
            item.veg.price if item.veg else 
            item.fruit.price if item.fruit else 
            item.juice.price
        )
        for item in cart
    )
    total = subtotal  # Delivery and discount are considered in POST request
    
    # Fetch the account number for the logged-in user
    account_number = "Not available"
    
    context = {
        'subtotal': subtotal,
        'total': total,
        'account_number': account_number,
    }
    return render(request, 'checkout.html', context)



def final(request):
    return render(request,'final.hmtl')
   
@login_required
def add_to_wishlist(request, item_id, item_type):
    if item_type == 'product':
        item = get_object_or_404(Product, id=item_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=item)
        if not created:
            wishlist.quantity += 1  # Increment quantity if item already exists in wishlist
            wishlist.save()
    elif item_type == 'veg':
        item = get_object_or_404(Veg, id=item_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user, veg=item)
        if not created:
            wishlist.quantity += 1  # Increment quantity if item already exists in wishlist
            wishlist.save()
    elif item_type == 'fruit':
        item = get_object_or_404(Fruit, id=item_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user, fruit=item)
        if not created:
            wishlist.quantity += 1  # Increment quantity if item already exists in wishlist
            wishlist.save()    
            wishlist.save()
    elif item_type == 'juice':
        item = get_object_or_404(Juice, id=item_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user, juice=item)
        if not created:
            wishlist.quantity += 1  # Increment quantity if item already exists in wishlist
            wishlist.save()             
    else:
        messages.error(request, "Invalid item type.")
        return redirect('shop')  # or another appropriate redirect location

    return redirect('wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    products = wishlist_items.filter(product__isnull=False)
    veg_items = wishlist_items.filter(veg__isnull=False)
    fruit_items = wishlist_items.filter(fruit__isnull=False)
    juice_items = wishlist_items.filter(juice__isnull=False)
    return render(request, 'wishlist.html', {
        'products': products,
        'veg_items': veg_items,
        'fruit_items': fruit_items,
        'juice_items': juice_items
    })


@login_required
def remove_from_wishlist(request, item_id, item_type):
    if item_type == 'product':
        item = get_object_or_404(Product, id=item_id)
        try:
            wishlist_item = Wishlist.objects.get(user=request.user, product=item)
            wishlist_item.delete()
          
        except Wishlist.DoesNotExist:
            messages.error(request, "Product not found in your wishlist.")
    elif item_type == 'veg':
        item = get_object_or_404(Veg, id=item_id)
        try:
            wishlist_item = Wishlist.objects.get(user=request.user, veg=item)
            wishlist_item.delete()
         
        except Wishlist.DoesNotExist:
            messages.error(request, "Vegetable not found in your wishlist.")
    elif item_type == 'fruit':
        item = get_object_or_404(Fruit, id=item_id)
        try:
            wishlist_item = Wishlist.objects.get(user=request.user, fruit=item)
            wishlist_item.delete()
            
        except Wishlist.DoesNotExist:
            messages.error(request, "fruit not found in your wishlist.")
    elif item_type == 'juice':
        item = get_object_or_404(Juice, id=item_id)
        try:
            wishlist_item = Wishlist.objects.get(user=request.user, juice=item)
            wishlist_item.delete()
         
        except Wishlist.DoesNotExist:
            messages.error(request, "fruit not found in your wishlist.")        
    else:
        messages.error(request, "Invalid item type.")
    
    return redirect('wishlist')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_history.html', {
        'orders': orders
    })





@login_required
@user_passes_test(is_admin_user)
def user_list(request):
    # Get all users with is_user=True
    users = customuser.objects.filter(is_user=True)
    return render(request, 'user_list.html', {'users': users})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def user_profile_details(request):
    if not request.user.is_user:
        # Optionally handle cases where the user is not an `is_user`
        return redirect('home')  # Redirect or show an error

    user = request.user
    return render(request, 'user_profile_details.html', {'user': user})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserProfileForm

@login_required
def edit_user_profile(request):
    if not request.user.is_user:
        # Optionally handle cases where the user is not an `is_user`
        return redirect('home')  # Redirect or show an error

    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('user_profile_details')  # Redirect to profile details page
    else:
        form = UserProfileForm(instance=user)
    
    return render(request, 'edit_user_profile.html', {'form': form})
# @user_passes_test(is_admin_user)
# def admin_user_orders(request):
#     orders = Order.objects.filter(user__is_user=True).order_by('-created_at')
#     return render(request, 'admin_user_orders.html', {'orders': orders})

@user_passes_test(is_admin_user)
def admin_user_orders(request):
    # Fetch orders grouped by user
    user_orders = Order.objects.filter(user__is_user=True).order_by('user', '-created_at')
    
    # Create a dictionary to group orders by user
    grouped_orders = {}
    for order in user_orders:
        if order.user not in grouped_orders:
            grouped_orders[order.user] = []
        grouped_orders[order.user].append(order)

    return render(request, 'admin_user_orders.html', {'grouped_orders': grouped_orders})


# @user_passes_test(is_admin_user)
# def admin_user_order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     order_items = OrderItem.objects.filter(order=order)
#     return render(request, 'admin_user_order_detail.html', {
#         'order': order,
#         'order_items': order_items
#     }) 

@user_passes_test(is_admin_user)
def admin_user_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'admin_user_order_detail.html', {
        'order': order,
        'order_items': order_items
    })

@user_passes_test(is_admin_user)
def admin_user_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'admin_user_order_detail.html', {
        'order': order,
        'order_items': order_items
    })

# views.py
def user_order_history(request, user_id):
    user =customuser.objects.get(pk=user_id)
    orders = Order.objects.filter(user=user)
    return render(request, 'admin_user_order_history.html', {'user': user, 'orders': orders})
