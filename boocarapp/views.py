from django.shortcuts import render, redirect
from .forms import GoForItForm
from .models import CarPart

def car_items(request):
    car_data = CarPart.objects.all()
    return render(request, 'boocarapp/vroom.html', {'car_data':car_data})

def go_for_it(request, item):

    print('item: {}'.format(item))

    if request.method == "POST":
        form = GoForItForm(request.POST)
        if form.is_valid():
            car = CarPart.objects.filter(item_name__icontains=item)[0]
            print(car)
            car.name = request.POST.get('your_name', '')
            car.note = 'Someone already snatched this one!'
            car_data = CarPart.objects.all()
            print(car)
            car.save()
            return redirect('/', {'car_data':car_data}) #pk=car_part.pk)
    else:
        form = GoForItForm()

    return render(request, 'boocarapp/go_for_it.html', {'form': form})