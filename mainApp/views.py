from django.shortcuts import render,redirect

def home(Request):
    return render(Request,"index.html")

def about(Request):
    return render(Request,"about.html")

def contact(Request):
    return render(Request,"contact.html")

def product(Request):
    return render(Request,"product.html")

def services(Request):
    return render(Request,"services.html")

def qaac(Request):
    return render(Request,"qaac.html")

def dal(Request):
    return render(Request,"dal.html")

def pmsas(Request):
    return render(Request,"pmsas.html")

# def singleProduct(Request):
#     return render(Request,"single-product.html")