from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import userinfo, product , abouts

def index(request):
    return render(request,"index.html")

def about(request):
    data = abouts.objects.all()
    return render(request,"about.html",{'data':data})

def contact(request):
    return render(request,"contact.html")

def products(request):
    return render(request,"products.html")

def sproduct(request):
    return render(request,"single-product.html")

def signup(request):
    try:
        if request.method =='POST':
            obj = userinfo()
            obj.username = request.POST.get('username')
            obj.password = request.POST.get('password')
            obj.email = request.POST.get('email')
            obj.phone = request.POST.get('contact')
            obj.utype = request.POST.get('utype')
            obj.save()
            print("Saved Successfully")
            return redirect('login')
    except:
        pass

    return render(request,"signup.html")

def login(request):
    try:
        if request.method =='POST':
            x = request.POST.get('username')
            y = request.POST.get('password')
            print(x,y)
            z=userinfo.objects.get(username=x)
            print(z.password)
            if y==z.password:
                return redirect('about')
            else:
                return HttpResponse("Invalid Password")
    except:
        return HttpResponse("UNAUTHORIZED")
    return render(request,"login.html")        
            
            
            # result = int(x)+int(y)
            # data = {
            #     "Sum":result
            # }
    
def adminproduct(request):
    
        if request.method =='POST':
            obj = product()
            obj.product_id = request.POST.get('productId')
            obj.product_name = request.POST.get('productName')
            obj.category = request.POST.get('productCategory')
            obj.price = request.POST.get('productPrice')
            obj.quantity = request.POST.get('productQuantity')
            obj.image = request.POST.get('productImage')
            obj.warranty = request.POST.get('productWarranty')
            obj.description = request.POST.get('productDescription')
            obj.save()
            print("Saved Successfully")
    

        return render(request,"admin_product.html")


def base(request):
    return render(request,"base.html")

def users(request):
    userlist=userinfo.objects.all()
    return render(request,"users.html",{'userlist':userlist})