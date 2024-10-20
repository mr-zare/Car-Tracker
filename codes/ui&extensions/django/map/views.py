from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect

def convert(request):
    if request.method == 'POST' and 'location' in request.POST:
        location = request.POST['location']
        data = location.split(",")
        lat = convert_coordinate(data[3])
        lon = convert_coordinate(data[5])
        addr = f"https://www.google.com/maps/@{lat},{lon},1x`8z"

        with open("loc.txt", "w") as file:
            file.write(addr)

        return HttpResponse('ok', status=200)
    else:
        with open("loc.txt", 'r') as file:
            tx = file.read()
            return redirect(tx)  # Redirect to some URL if 'location' is not in POST data

def convert_coordinate(coordinate):
    string = str(int(coordinate) / 100).split(".")
    degree = int(string[0]) * 60
    string[1] = int(string[1]) * (10 ** (6 - len(str(int(string[1])))))
    minutes = (int(string[1]) / 10000)
    minutes += degree
    return minutes / 60
