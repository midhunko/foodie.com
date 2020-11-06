from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile, Pasta, Cart, Review
from django.contrib.auth import authenticate, login, logout
from .forms import ReviewForm


def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(request, username=email, password=password)

        if user:
            print(user)
            login(request, user)
            return HttpResponseRedirect(reverse(index))
        else:
            error = 'Sorry, Please log in with correct credentials'
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))


def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        emailcheck = UserProfile.objects.filter(email=email).exists()

        if not emailcheck:
            user1 = User.objects.create_user(
                username=name,
                password=password
            )
            user = UserProfile.objects.create(
                user=user1,
                name=name,
                email=emailcheck,
                password=password
            )
            return render(request, 'login.html')
        else:
            error = " Email or Phone-Number already exists "
            return render(request, 'signup.html', {'error': error})
    else:
        return render(request, 'signup.html')


def index(request):
    product = Pasta.objects.all()
    return render(request, 'index.html', {'product': product})


def pasta(request):
    pasta = Pasta.objects.all()
    return render(request, 'pasta.html', {'pasta': pasta})


def showcart(request):
    pasta = Cart.objects.filter(user=request.user)
    print(pasta)
    return render(request, 'showcart.html', {'pasta': pasta})


def delete_item(request, item):
    pasta = Cart.objects.get(id=item)
    #pasta = p.pasta
    return render(request, 'delete.html', {'pasta': pasta})


def delete_confirm(request, item):
    #p = Pasta.objects.filter(id=item).first()
    Cart.objects.get(id=item).delete()

    return redirect('showcart')


def checkout_view(request):
    return render(request, 'checkout.html')


def cart_check(request):
    return redirect('showcart')


def review(request):
    review = Review.objects.all()
    return render(request, 'review.html', {'review': review})


def add_review(request):
    form = ReviewForm(initial={'user': request.user})
    #form = JournalForm(initial={'tank': 123})
    #pasta = Pasta.objects.get(id=item)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            #user_name = request.user
            pastas = form.cleaned_data['pasta']
            reviews = form.cleaned_data['review']
            reviewform = Review()
            #reviewform.user = user_name
            reviewform.pasta = pastas
            reviewform.review = reviews
            form.save()
            return redirect('review')
    return render(request, 'add_review.html', {'form': form}) #'pasta': pasta})



def addtocart(request, pro):
    pasta = Pasta.objects.get(id=pro)
    #print(pasta)
    s = request.user
    #print(s)
    cart = Cart.objects.create(
                user=request.user,
                pasta=pasta)
    cart.save()
    print('hi')
    return render(request, 'detail.html', {'pasta': pasta})


def order_placed(request):
    Cart.objects.all().delete()
    return render(request, 'order_placed.html')