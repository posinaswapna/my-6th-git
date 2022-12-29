from django.shortcuts import render

# Create your views here.

def swapna(request):
    d={'name':'swapna','city':'nellore'}
    return render(request,'jp1.html',context=d)
def swapna1(request):
        d={'code':'74de5','sub':'django'}
        return render(request,'jp02.html',context=d)