from django.shortcuts import render,redirect
from django.views import View
from .forms import RegistrationForm, LoginForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import UsereUpdateForm
from .models import Product_Buddha,ProductCategory,Order
from django.shortcuts import render, get_object_or_404
from .models import Product_Buddha ,CartItem
from .forms import Buddha_Form,Tara_Form,Ganesh_Form,CategoryForm,Product_Tara,Product_Ganesh,Product_Sarsoti_Laxmi,Utencils,laxmi_Sarsoti_Form,Utensils_Form,ProfileEditForm
from django.contrib.auth.decorators import login_required



def Register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
        form = RegistrationForm() 

    return render(request,'registration.html',{'form':form})

def LandingPage(request):
    Buddha_products = Product_Buddha.objects.all()
    tara_products = Product_Tara .objects.all()
    ganesh_products = Product_Ganesh.objects.all()
    laxmi_sar_products = Product_Sarsoti_Laxmi.objects.all()
    utensils_products = Utencils.objects.all()

    productcategory = ProductCategory.objects.all()
    
    return render(request, 'LandingPage.html', {'Buddha_products': Buddha_products,'tara_products':tara_products,'ganesh_products':ganesh_products,'laxmi_sar_products':laxmi_sar_products,'utensils_products':utensils_products,'productcategory': productcategory})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password) #user lai authenticate garako 
            if user is not None:  # checks whether a user has been successfully authenticated.
                login(request, user)
                # Check if the user is a superuser

                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                if user.is_superuser:
                    return redirect('admindashboard')
                return redirect('HomeDashboard')
            
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def root_view(request):
    return render(request, 'LandingPage.html', {'user': request.user})

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_user')
    else:
        form = UserCreationForm()
    return render(request,'User/create_user.html',{'form':form})

def user_list(request):
    users = User.objects.all()
    return render(request,'User/user_list.html',{'users':users})

def update_user(request, user_id):
    user = User.objects.get(pk=user_id) # retrieves the user object from the database based on the primary key (pk), which is the user_id.
    if request.method == 'POST':
        form = UsereUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('user_list')
    else:
        form = UsereUpdateForm()
    return render(request,'User/update_user.html',{'form':form})

def user_delete(request,user_id):
    user = User.objects.get(pk=user_id)
    if request.method =='POST':
        user.delete()
        return redirect('user_list')
    return render(request,'User/user_delete.html')

# Buddha=================================
def Buddha_list(request):
    products = Product_Buddha.objects.all()
    return render(request,'Buddha_Products/Buddha_product_list.html', {'products': products})

def addProduct_Buddha(request):
    if request.method == 'POST':
        form = Buddha_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Buddha_product_list')
    else:
        form = Buddha_Form()
    return render(request,'Buddha_Products/add_Buddha_Product.html',{'form':form})

def Buddha_update_product(request, pk):
    product = Product_Buddha.objects.get(pk=pk)
    if request.method == 'POST':
        form = Buddha_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Buddha_product_list')
    else:
        form = Buddha_Form(instance=product)
    return render(request,'Buddha_Products/Buddha_updateProduct.html',{'form':form})

def Buddha_deleteProduct(request, pk):
    Buddha_product = Product_Buddha.objects.get(pk=pk)
    if request.method == 'POST':
        Buddha_product.delete()
        return redirect('Buddha_product_list')
    return render(request, 'Buddha_Products/Buddha_delete_product.html',{'Buddha_product': Buddha_product})

# Tara=============================================================

def Tara_list(request):
    Tara_products = Product_Tara.objects.all()
    return render(request,'Tara_Products/Tara_product_list.html', {'Tara_products': Tara_products})

def addProduct_Tara(request):
    if request.method == 'POST':
        form = Tara_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Tara_product_list')
    else:
        form = Tara_Form()
    return render(request,'Tara_Products/add_Tara_Product.html',{'form':form})

def Tara_update_product(request, pk):
    product = Product_Tara.objects.get(pk=pk)
    if request.method == 'POST':
        form = Tara_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Tara_product_list')
    else:
        form = Tara_Form(instance=product)
    return render(request,'Tara_Products/Tara_updateProduct.html',{'form':form})

def Tara_deleteProduct(request, pk):
    Tara_product = Product_Tara.objects.get(pk=pk)
    if request.method == 'POST':
        Tara_product.delete()
        return redirect('Tara_product_list')
    return render(request, 'Tara_Products/Tara_delete_product.html',{'Tara_product': Tara_product})
#ganesh ============================================================================

def Ganesh_list(request):
    Ganesh_products = Product_Ganesh.objects.all()
    return render(request,'Ganesh_Products/Ganesh_product_list.html', {'Ganesh_products': Ganesh_products})

def addProduct_Ganesh(request):
    if request.method == 'POST':
        form = Ganesh_Form(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('Ganesh_product_list')
    else:
        form = Ganesh_Form()
    return render(request,'Ganesh_Products/add_Ganesh.html',{'form':form})

def Ganesh_update_product(request, pk):
    product = Product_Ganesh.objects.get(pk=pk)
    if request.method == 'POST':
        form = Ganesh_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Ganesh_list')
    else:
        form = Ganesh_Form(instance=product)
    return render(request,'Ganesh_Products/Ganesh_updateProduct.html',{'form':form})

def Ganesh_deleteProduct(request, pk):
    Ganesh_product = Product_Ganesh.objects.get(pk=pk)
    if request.method == 'POST':
        Ganesh_product.delete()
        return redirect('Ganesh_product_list')
    return render(request, 'Ganesh_Products/Ganesh_delete_product.html',{'Ganesh_product': Ganesh_product})

#laxmi sar ==========================================

def Sarsoti_Laxmi_list(request):
    Sarsoti_Laxmi_products =Product_Sarsoti_Laxmi.objects.all()
    return render(request,'Sarsoti_Laxmi_Products/Sarsoti_Laxmi_product_list.html', {'Sarsoti_Laxmi_products': Sarsoti_Laxmi_products})

def addProduct_Sarsoti_Laxmi(request):
    if request.method == 'POST':
        form = laxmi_Sarsoti_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Sarsoti_Laxmi_list')
    else:
        form = Tara_Form()
    return render(request,'Sarsoti_Laxmi_Products/add_Sarsoti_Laxmi.html',{'form':form})

def Sarsoti_Laxmi_update_product(request, pk):
    product = Product_Sarsoti_Laxmi.objects.get(pk=pk)
    if request.method == 'POST':
        form = laxmi_Sarsoti_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Sarsoti_Laxmi_list')
    else:
        form = laxmi_Sarsoti_Form(instance=product)
    return render(request,'Sarsoti_Laxmi_Products/Sarsoti_Laxmi_updateProduct.html',{'form':form})

def Sarsoti_Laxmi_deleteProduct(request, pk):
    Sarsoti_Laxmi_product = Product_Sarsoti_Laxmi.objects.get(pk=pk)
    if request.method == 'POST':
        Sarsoti_Laxmi_product.delete()
        return redirect('Sarsoti_Laxmi_product_list')
    return render(request, 'Sarsoti_Laxmi_Products/Sarsoti_Laxmi_delete_product.html',{'Sarsoti_Laxmi_product': Sarsoti_Laxmi_product})

# ==================================================================================

def Utencils_list(request):
    Utencils_products = Utencils.objects.all()
    return render(request,'Utencils_Products/Utencils_product_list.html', {'Utencils_products': Utencils_products})

def addProduct_Utencils(request):
    if request.method == 'POST':
        form = Utensils_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Utencils_product_list')
    else:
        form = Utensils_Form()
    return render(request,'Utencils_Products/add_Utencils.html',{'form':form})

def Utencils_update_product(request, pk):
    product = Utencils.objects.get(pk=pk)
    if request.method == 'POST':
        form = Utensils_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Utencils_list')
    else:
        form = Utensils_Form(instance=product)
    return render(request,'Utencils_Products/Utencils_updateProduct.html',{'form':form})

def Utencils_deleteProduct(request, pk):
    Utencils_product = Utencils.objects.get(pk=pk)
    if request.method == 'POST':
        Utencils.delete()
        return redirect('Utencils_product_list')
    return render(request, 'Utencils_Products/Utencils_delete_product.html',{'Utencils_product': Utencils_product})
# ==============================================================
def dashboard(request):
    Buddha_products = Product_Buddha.objects.all()
    tara_products = Product_Tara .objects.all()
    ganesh_products = Product_Ganesh.objects.all()
    laxmi_sar_products = Product_Sarsoti_Laxmi.objects.all()
    utensils_products = Utencils.objects.all()
    productcategory = ProductCategory.objects.all()


    return render(request, 'LandingPage.html', {'Buddha_products': Buddha_products,'tara_products':tara_products,'ganesh_products':ganesh_products,'laxmi_sar_products':laxmi_sar_products,'utensils_products':utensils_products,'productcategory': productcategory})


# ========================================================

def HomeDashboard(request):
    Buddha_products = Product_Buddha.objects.all()
    tara_products = Product_Tara .objects.all()
    ganesh_products = Product_Ganesh.objects.all()
    laxmi_sar_products = Product_Sarsoti_Laxmi.objects.all()
    utensils_products = Utencils.objects.all()
    productcategory = ProductCategory.objects.all()

    return render (request,'dashboard.html', {'Buddha_products': Buddha_products,'tara_products':tara_products,'ganesh_products':ganesh_products,'laxmi_sar_products':laxmi_sar_products,'utensils_products':utensils_products,'productcategory': productcategory})


def ProductsCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('CategoryList')
            
    else:
        form = CategoryForm()
    return render(request,'ProductCategory/ProductCategory.html',{'form':form})


def CategoryList(request):
    Clist = ProductCategory.objects.all()
    return render(request, 'ProductCategory/CategoryList.html',{"Clist":Clist})

def UpdateProductCategory(request,pk):
    productcategory = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES,instance=productcategory)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CategoryForm(instance=productcategory)#instance=product, you’re telling Django to pre-fill the form with the current details of the specific product.
        return render(request,'ProductCategory/UpdateProduct.html',{"form":form})
    
def CategoryDelete(request, pk):
    categoryDel = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        categoryDel.delete()
        return redirect('CategoryList')
    else:
        return render(request,'ProductCategory/deleteCategoryProduct.html',{"CategoryList":CategoryList})
    

def Buddha_product_details(request,pk):
    Bproduct = get_object_or_404(Product_Buddha, id=pk)
    return render(request, 'Product_Details/BuddhaOne.html', {'Bproduct': Bproduct})

def Tara_product_details(request,pk):
    Tproduct = get_object_or_404(Product_Tara, id=pk)
    return render(request, 'Product_Details/TaraOne.html', {'Tproduct': Tproduct})

def Ganesh_product_details(request,pk):
    Gproduct = get_object_or_404(Product_Ganesh, id=pk)
    return render(request, 'Product_Details/GaneshOne.html', {'Gproduct': Gproduct})

def product_details(request, pk):
    buddha_product = get_object_or_404(Product_Buddha, id=pk)
    tara_product = get_object_or_404(Product_Tara, id=pk)
    ganesh_product = get_object_or_404(Product_Ganesh, id=pk)
    
    context = {
        'buddha_product': buddha_product,
        'tara_product': tara_product,
        'ganesh_product': ganesh_product,
    }
    return render(request, 'Product_Details/BuddhaOne.html', context)    

@login_required
def Buys_now(request,pk):
    return render(request,'buy_detail/Buy_detail.html',{'pk':pk})

def edit_profile(request, pk):
    user = get_object_or_404(User, pk=pk)  # Fetch the user
    profile = user.profile  # Get the user's profile
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)  # Bind form to the user's profile
        if form.is_valid():
            form.save()  # Save the updated profile
            return redirect('profile_view', pk=user.pk)  # Redirect to profile view (define this view)
    else:
        form = ProfileEditForm(instance=profile)  # Display the form with the current profile data
    return render(request, 'Profile/edit_profile.html', {'form': form})


@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'Profile/profile.html', {'user': user})


def godinfo(request,pk):
    product = get_object_or_404(  ProductCategory, id=pk)
    return render(request,'God Information/Information.html',{'product':product})


model_mapping = {
    'buddha': Product_Buddha,
    'tara': Product_Tara,
    'ganesh': Product_Ganesh,
    'sarsoti_laxmi': Product_Sarsoti_Laxmi,
    'utencils': Utencils
}

@login_required
def add_to_cart(request, product_id, product_type):
    # Get the correct model based on the product type
    product_model = model_mapping.get(product_type)

    if not product_model:
        # If the product type is invalid, redirect to an error page or show a message
        return redirect('error_page')

    # Retrieve the product using the appropriate model
    product = product_model.objects.get(id=product_id)
    user = request.user

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(
        user=user,
        product_name=product.name,
        product_price=product.price,
        product_image=product.image,
    )

    if not created:
        # If the item exists, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    # Redirect to the cart view (or any other page you want)
    return redirect('cart_view')



@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        item.total_price = item.product_price * item.quantity

    total_price = sum(item.total_price for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)

    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))
        cart_item.quantity = new_quantity
        cart_item.save()

    return redirect('cart_view') 
from django.shortcuts import get_object_or_404, redirect
from .models import CartItem

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete() 
    return redirect('cart_view') 



def backfunction(request):
    if request.user.is_authenticated:
        return redirect('HomeDashboard')  # This should redirect to the 'dashboard' view
    else:
        return redirect('LandingPage')  # This should redirect to the 'LandingPage' view


model_mapping = {
    'buddha': Product_Buddha,
    'tara': Product_Tara,
    'ganesh': Product_Ganesh,
    'sarsoti_laxmi': Product_Sarsoti_Laxmi,
    'utencils': Utencils,
}

def buy_now(request, product_id, category):
    model = model_mapping.get(category)
    if not model:
        return render(request, 'error.html', {'message': 'Invalid product category'})

    product = get_object_or_404(model, id=product_id)

    # Create the order
    order = Order.objects.create(
        user=request.user,
        product_name=product.name,
        product_price=product.price,
        quantity=1,
        total_price=product.price,
    )
    return redirect('checkout', order_id=order.id) #order id pass garako hai url mah to the checkout page okk



def checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        # Simulate payment processing (e.g., integrate a payment gateway here)
        order.save()

        return render(request, 'payment_success.html', {'order': order})

    return render(request, 'checkout.html', {'order': order})


def process_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Simulate payment processing
    if request.method == "POST":
        # Update order status
        order.save()

        return render(request, 'payment_success.html', {'order': order})

    return redirect('checkout', order_id=order.id)




def registration(request):
    return render(request,'registration.html')

def admindashboard(request):
    return render(request,'admindashboard.html')

def logout_view(request):
    logout(request)
    return redirect('LandingPage')

    

