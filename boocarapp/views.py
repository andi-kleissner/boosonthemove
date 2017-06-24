from django.shortcuts import render

# Create your views here.
def car_items(request):
    return render(request, 'boocarapp/vroom.html', {})