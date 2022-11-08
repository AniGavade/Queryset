from django.shortcuts import render

# Create your views here.
def decore(add):
    def inner():
        a=add()
        z=a+25
        return z
    return inner

def add():
    return 25
add()