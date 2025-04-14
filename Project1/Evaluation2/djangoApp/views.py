from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        selected_role=request.POST.get('role')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if(selected_role=='admin' and user.is_superuser) or (selected_role=='user' and not user.is_superuser):
               login(request, user)
               messages.success(request, f"Welcome, {username}!")
               return redirect('dashboard')  
            else:
               messages.error(request,"invalid credentials or passsword")
        # or whatever your post-login page is
        else:
           messages.error(request, "Invalid username or password")

    return render(request, 'login.html')
 

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        print("Password:", password)
        print("Confirm Password:", cpassword)

        if not password or not cpassword:
            messages.error(request, 'Password and Confirm Password are required')
        elif password != cpassword:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
        else:
            try:
                validate_password(password)
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                messages.success(request, 'Registration successful! You can now login.')
                return redirect('login')
            except ValidationError as e:
                for error in e:
                    messages.error(request, error)

    return render(request, 'register.html')



def dashboard_view(request):
    return render(request,'dashboard.html')
@login_required
def profile_view(request):
    return render(request,'profile.html')
@login_required
def product_view(request):
    return render(request,'product.html')
@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import CartItem , cart

# Create your views here.
def home_view(request):
    return render(request , 'home.html')



# def beauty_view(request):
#     return render(request , 'beauty.html')


def beauty_view(request):
    beauty_products = [
    {'name': 'Sol de Janeiro Beija Flor Jet Set', 'price': '$32.00', 'image': 'product1.webp'},
    {'name': 'Charlotte Tilbury Beauty Pillow Talk Mini', 'price': '$25.00', 'image': 'product2.webp'},
    {'name': 'Sol de Janeiro Bom Dia Bright Jet set', 'price': '$33.00', 'image': 'product3.jpg'},
    {'name': 'Glow Recipe Fruit Babies Bestsellers Kit', 'price': '$250.00', 'image': 'product4.jpeg'},
    {'name': 'Fenty Beauty Pro Filtr Foundation', 'price': '$38.00', 'image': 'product5.jpeg'},
    {'name': 'Urban Decay Naked3 Eyeshadow Palette', 'price': '$54.00', 'image': 'product6.jpeg'},
    {'name': 'Anastasia Beverly Hills Brow Wiz', 'price': '$21.00', 'image': 'product7.jpeg'},
    {'name': 'Too Faced Better Than Sex Mascara', 'price': '$25.00', 'image': 'product8.jpeg'},
    {'name': 'MAC Cosmetics Matte Lipstick', 'price': '$19.00', 'image': 'product9.jpeg'},
    {'name': 'Tarte Shape Tape Concealer', 'price': '$27.00', 'image': 'product10.jpeg'},
    {'name': 'Maybelline Fit Me Foundation', 'price': '$10.00', 'image': 'product11.jpeg'},
    {'name': 'Huda Beauty Desert Dusk Palette', 'price': '$65.00', 'image': 'product12.jpeg'},
    {'name': 'NARS Radiant Creamy Concealer', 'price': '$30.00', 'image': 'product13.jpeg'},
    {'name': 'Fenty Beauty Killawatt Highlighter', 'price': '$36.00', 'image': 'product14.jpeg'},
    {'name': 'L`Oréal Lash Paradise Mascara', 'price': '$12.00', 'image': 'product15.jpeg'},
    {'name': 'Benefit Cosmetics Hoola Bronzer', 'price': '$30.00', 'image': 'product16.jpeg'},
    {'name': 'Charlotte Tilbury Airbrush Powder', 'price': '$45.00', 'image': 'product17.jpeg'},
    {'name': 'Becca Shimmering Skin Perfector', 'price': '$38.00', 'image': 'product18.jpeg'},
    {'name': 'IT Cosmetics CC+ Cream', 'price': '$39.00', 'image': 'product19.jpeg'},
    {'name': 'Tatcha The Dewy Skin Cream', 'price': '$68.00', 'image': 'product20.jpeg'}

    ]
    return render(request, 'beauty.html', {'beauty_products': beauty_products})


def all_view(request):
    products = [
    {'name': 'Amul Moti Milk', 'price': '$0.40', 'image': 'milk.png'},
    {'name': 'Whole Wheat Bread', 'price': '$0.72', 'image': 'wheatbread.png'},
    {'name': 'Brown Bread', 'price': '$0.66', 'image': 'brownbread.png'},
    {'name': 'Pav Bread', 'price': '$0.54', 'image': 'pavbread.png'},
    {'name': 'Eggs', 'price': '$0.86', 'image': 'eggs.png'},
    {'name': 'Corn Flakes', 'price': '$1.44', 'image': 'cornflakes.png'},
    {'name': 'Muesli', 'price': '$6.53', 'image': 'muesli.png'},
    {'name': 'Oats', 'price': '$0.82', 'image': 'oats.png'},
    {'name': 'Curd', 'price': '$0.30', 'image': 'curd.png'},
    {'name': 'Salted Butter', 'price': '$0.72', 'image': 'butter.png'},
    {'name': 'Cheese Slices', 'price': '$1.02', 'image': 'cheese.png'},
    {'name': 'Fresh Cream', 'price': '$0.82', 'image': 'cream.png'},
    {'name': 'Condensed Milk', 'price': '$1.68', 'image': 'condensedmilk.png'},
    {'name': 'Peanut Butter', 'price': '$1.75', 'image': 'peanutbutter.png'},
    {'name': 'Honey', 'price': '$1.38', 'image': 'honey.png'},
    {'name': 'Tomato Ketchup', 'price': '$1.20', 'image': 'ketchup.png'},
    {'name': 'Mayonnaise', 'price': '$0.59', 'image': 'mayo.png'},
    {'name': 'Schezwan Chutney', 'price': '$1.01', 'image': 'chutney.png'},
    {'name': 'Chocolate Syrup', 'price': '$1.26', 'image': 'chocolatesyrup.png'},
    {'name': 'Ginger Garlic Paste', 'price': '$0.55', 'image': 'gingergarlic.png'},
    {'name': 'Vinegar', 'price': '$0.80', 'image': 'vinegar.png'},
    {'name': 'Premium Tea', 'price': '$1.68', 'image': 'tea.png'},
    {'name': 'Taj Mahal Tea', 'price': '$0.78', 'image': 'tajtea.png'},
    {'name': 'Instant Coffee', 'price': '$2.76', 'image': 'coffee.png'},
    {'name': 'Whole Wheat Flour', 'price': '$2.86', 'image': 'wheatflour.png'},
    {'name': 'Basmati Rice', 'price': '$4.98', 'image': 'rice.png'},
    {'name': 'Kabuli Chana', 'price': '$1.87', 'image': 'chana.png'},
    {'name': 'Red Rajma', 'price': '$1.44', 'image': 'rajma.png'},
    {'name': 'Toor Dal', 'price': '$2.38', 'image': 'toordal.png'},
    {'name': 'Urad Dal', 'price': '$0.92', 'image': 'uraddal.png'},
    {'name': 'Brown Chana', 'price': '$0.79', 'image': 'brownchana.png'},
    {'name': 'Chewing Gum', 'price': '$0.59', 'image': 'gum.png'},
    {'name': 'Choco Pie', 'price': '$0.96', 'image': 'chocopie.png'}
]    
    return render(request, 'all.html', {'products': products})

# def snacks_view(request):
#     return render(request , 'snacks.html')
def snacks_view(request):
 snacks_products = [
    {'name': 'Maggi Noodles', 'price': '$0.12', 'image': 'maggi.png'},
    {'name': 'Tedhe Medhe', 'price': '$0.12', 'image': 'tedhemedhe.png'},
    {'name': "Lay's Magic Masala", 'price': '$0.12', 'image': 'Bluelays.png'},
    {'name': "Lay's Classic Salted", 'price': '$0.12', 'image': 'Yellowlays.png'},
    {'name': "Lay's Cream & Onion", 'price': '$0.12', 'image': 'GreenLays.png'},
    {'name': "Maggi Cheese Pasta", 'price': '$0.42', 'image': 'cheese.png'},
    {'name': "Maggi Masala Pasta", 'price': '$0.42', 'image': 'masala.png'},
    {'name': "Oreo Cookies", 'price': '$0.12', 'image': 'oreo.png'},
    {'name': "Dark Fantasy", 'price': '$0.36', 'image': 'darkfantasy.png'},
    {'name': "Hide & Seek", 'price': '$0.36', 'image': 'hide.png'},
    {'name': "Jim Jam", 'price': '$0.12', 'image': 'jimjam.png'},
    {'name': "Good Day", 'price': '$0.12', 'image': 'gooday.png'},
    {'name': "Little Hearts", 'price': '$0.12', 'image': 'hearts.png'},
    {'name': "Ferrero Rocher", 'price': '$9.16', 'image': 'ferrero.png'},
    {'name': "Dairy Milk Silk", 'price': '$2.23', 'image': 'fruitNut.png'},
    {'name': "Kit Kat", 'price': '$1.32', 'image': 'kitkat.png'},
    {'name': "Crispello", 'price': '$0.48', 'image': 'crispello.png'},
    {'name': "Munch", 'price': '$0.68', 'image': 'munch.png'},
    {'name': "Thums Up", 'price': '$0.48', 'image': 'thumsup.png'},
    {'name': "Choco Latte", 'price': '$1.44', 'image': 'chocolatte.png'},
    {'name': "Cold Coffee", 'price': '$1.44', 'image': 'coldcoffee.png'},
    {'name': "Diet Coke", 'price': '$0.48', 'image': 'diet.png'},
    {'name': "Fanta", 'price': '$0.48', 'image': 'fanta.png'},
    {'name': "Sprite", 'price': '$0.48', 'image': 'sprite.png'},
    {'name': "Limca", 'price': '$0.48', 'image': 'limca.png'},
    {'name': "Maza", 'price': '$0.48', 'image': 'maza.png'},
    {'name': "Mountain Dew", 'price': '$1.03', 'image': 'dew.png'},
    {'name': "Aloo Bhujia", 'price': '$2.65', 'image': 'bhujia.png'},
    {'name': "Kinder Joy", 'price': '$0.58', 'image': 'joy.png'},
    {'name': "Makhana", 'price': '$1.92', 'image': 'makhana.png'}
]
 return render(request, 'snacks.html', {'snacks_products': snacks_products})
# def pharmacy_view(request):
#     return render(request , 'pharmacy.html')

def pharmacy_view(request):
    # = Product.objects.all()  # Assuming Product is your model
  pharmacy_products =[
    {'name': 'Pain Reliever Tablet', 'price': '$12.99', 'image': 'painrelif.jpg'},
    {'name': 'Cough Syrup', 'price': '$8.50', 'image': 'cough.jpg'},
    {'name': 'Multivitamin Capsules', 'price': '$15.75', 'image': 'multivitamin.jpg'},
    {'name': 'Antibiotic Ointment', 'price': '$5.99', 'image': 'onitment.jpg'},
    {'name': 'Cold Relief Capsules', 'price': '$10.30', 'image': 'cold.jpg'},
    {'name': 'Allergy Relief Tablets', 'price': '$7.99', 'image': 'allergy.jpg'},
    {'name': 'Digestive Aid Tablets', 'price': '$6.50', 'image': 'digestive.jpg'},
    {'name': 'Vitamin D3 Supplement', 'price': '$9.00', 'image': 'vitaminD3.jpg'},
    {'name': 'Antacid Tablets', 'price': '$3.75', 'image': 'amtacid.jpg'},
    {'name': 'Headache Relief Gel', 'price': '$4.99', 'image': 'haedache.jpg'},
    {'name': 'Hair Growth Shampoo', 'price': '$12.00', 'image': 'hair.jpg'},
    {'name': 'Sleep Aid Tablets', 'price': '$8.40', 'image': 'sleep.jpg'},
    {'name': 'Band-Aids', 'price': '$2.99', 'image': 'bandaid.jpg'},
    {'name': 'Eye Drops', 'price': '$5.50', 'image': 'eyedrops.jpg'},
    {'name': 'Muscle Relief Cream', 'price': '$7.25', 'image': 'muscle.jpg'},
    {'name': 'Moisturizing Lotion', 'price': '$6.80', 'image': 'moisturizing.jpg'},
    {'name': 'Thermometer', 'price': '$15.99', 'image': 'thermometer.jpeg'},
    {'name': 'Sunscreen Lotion', 'price': '$12.99', 'image': 'sunscreen.jpg'},
    {'name': 'First Aid Kit', 'price': '$25.00', 'image': 'firstaid.jpg'},
    {'name': 'Cold Compress', 'price': '$8.50', 'image': 'compress.jpg'}
]
  return render(request, 'pharmacy.html', {'pharmacy_products': pharmacy_products})
# def fruits_view(request):
#     return render(request , 'fruits&veg.html')


def fruits_view(request):
    fruits_products = [
    {'name': 'Apple', 'price': '$1.56', 'image': 'apple.png'},
    {'name': 'Banana', 'price': '$0.53', 'image': 'banana.png'},
    {'name': 'Mango', 'price': '$1.20', 'image': 'mango.png'},
    {'name': 'Orange', 'price': '$0.78', 'image': 'orange.png'},
    {'name': 'Litchi', 'price': '$1.20', 'image': 'litchi.png'},
    {'name': 'Kiwi', 'price': '$1.48', 'image': 'kiwi.png'},
    {'name': 'Dragon Fruit', 'price': '$0.76', 'image': 'dragonfruit.png'},
    {'name': 'Pineapple', 'price': '$1.12', 'image': 'pineapple.png'},
    {'name': 'Strawberry', 'price': '$1.15', 'image': 'strawberry.png'},
    {'name': 'Grapes', 'price': '$0.84', 'image': 'grapes.png'},
    {'name': 'Carrot', 'price': '$0.24', 'image': 'carrot.png'},
    {'name': 'Pomegranate', 'price': '$1.38', 'image': 'pomegranet.png'},
    {'name': 'Watermelon', 'price': '$0.42', 'image': 'watermelon.png'},
    {'name': 'Muskmelon', 'price': '$0.80', 'image': 'muskmelon.png'},
    {'name': 'Papaya', 'price': '$1.33', 'image': 'papaya.png'},
    {'name': 'Guava', 'price': '$1.44', 'image': 'guava.png'},
    {'name': 'Potato', 'price': '$0.36', 'image': 'potato.png'},
    {'name': 'Tomato', 'price': '$0.48', 'image': 'tomato.png'},
    {'name': 'Green Chilli', 'price': '$0.17', 'image': 'greenChilli.png'},
    {'name': 'Cauliflower', 'price': '$0.18', 'image': 'cauliflower.png'},
    {'name': 'Ginger', 'price': '$0.28', 'image': 'ginger.png'},
    {'name': 'Capsicum', 'price': '$0.96', 'image': 'capsicum.png'},
    {'name': 'Mushroom', 'price': '$0.60', 'image': 'mushroom.png'},
    {'name': 'Garlic', 'price': '$1.02', 'image': 'garlic.png'},
    {'name': 'Cucumber', 'price': '$0.36', 'image': 'cucumber.png'},
    {'name': 'Beans', 'price': '$0.35', 'image': 'beans.png'},
    {'name': 'Radish', 'price': '$0.36', 'image': 'raddish.png'},
    {'name': 'Lemon', 'price': '$0.36', 'image': 'lemon.png'},
    {'name': 'Broccoli', 'price': '$0.30', 'image': 'broccoli.png'},
    {'name': 'Onion', 'price': '$0.60', 'image': 'onion.png'}

    ]
    return render(request, 'fruits&veg.html', {'fruits_products': fruits_products})
# def add_to_cart(request, product_id):
    # Logic to handle adding the product to a cart
#     return HttpResponse(f"Product {product_id} added to the cart!")
    # Your cart logic here
    # return redirect('pharmacy_products')
# from django.shortcuts import render, get_object_or_404
# from .models import Cart, CartItem
# from django.contrib.auth.decorators import login_required

# def get_or_create_cart(request):
#     """Helper function to get or create cart for both authenticated and anonymous users"""
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user)
#     else:
#         if not request.session.session_key:
#             request.session.create()
#         cart, created = Cart.objects.get_or_create(
#             session_key=request.session.session_key,
#             user=None
#         )
#     return cart

# def cart_detail(request):
#     cart = get_or_create_cart(request)
#     cart_items = cart.items.all()
#     cart_total = sum(item.get_total_price() for item in cart_items)
    
#     return render(request, 'cart.html', {
#         'cart_items': cart_items,
#         'cart_total': cart_total
#     })

# @login_required
# def add_to_cart(request, product_id):
#     # Your existing add to cart logic
#     pass

# @login_required
# def remove_from_cart(request, item_id):
#     # Your existing remove from cart logic
#     pass