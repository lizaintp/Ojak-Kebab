from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog.html', locals())

def blog_detail(request):
    return render(request, 'blog_detail.html', locals())

def cart(request):
    return render(request, 'cart.html', locals())

def gallery(request):
    return render(request, 'gallery.html', locals())

def menu(request):
    return render(request, 'menu.html', locals())

def product(request):
    return render(request, 'product.html', locals())

def reservation(request):
    return render(request, 'reservation.html', locals())

def shop(request):
    return render(request, 'shop.html', locals())