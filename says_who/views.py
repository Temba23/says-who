from django.shortcuts import render, HttpResponse
from .models import Star, Question, Quote
from .forms import StarForm


def star(request):
    if request.method == "POST":
        form = StarForm(request.POST)
        if form.is_valid():
            star_name = form.cleaned_data['name']
            if Star.objects.filter(name=star_name).exists():
                return HttpResponse("Star Already Exists. Try Another One!")
            else:
                Star.objects.create(name=star_name)
                return HttpResponse("Star Created Successfully.")
        else:
            return HttpResponse("Error!")
    else:
        form = StarForm()
    return render(request, 'star.html', {"form": form})