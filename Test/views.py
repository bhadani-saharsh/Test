from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    print("here")
    if request.method == "POST":
        print("post")
        print("a: ",request.GET.get('a'))
        print("b: ",request.GET.get('b'))
        print("c: ",request.GET.get("c"))
        print("d: ",request.GET.get("d"))
    return render(request, "Test/index.html")

