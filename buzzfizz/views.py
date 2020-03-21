from django.shortcuts import render

def buzzfizz(request):
    return render(request, 'buzzfizz/buzz_list.html', {})

def add_user(request):
    return render(request, 'buzzfizz/add_user.html', {})

