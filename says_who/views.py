from django.shortcuts import render, HttpResponse
from .models import Star, Question, Quote
from .forms import StarForm, QuoteForm


def star(request):
    if request.method == "POST":
        form = StarForm(request.POST)
        if form.is_valid():
            star_name = form.cleaned_data['name']
            if Star.objects.filter(name=star_name).exists():
                form.add_error('name', 'Star Already Exists. Try Another One!')
                return render(request, 'star.html', {"form": form})
            else:
                Star.objects.create(name=star_name)
                return HttpResponse("Star Created Successfully.")
        else:
            return render(request, 'star.html', {"form": form})
    else:
        form = StarForm()
    return render(request, 'star.html', {"form": form})

def quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.cleaned_data['quote']
            star = form.cleaned_data['star']
            print(star, quote)
            form.save()
            return HttpResponse("Quote Added to the Star Successfully.")
        
        else:
            form.add_error(request, "Error submitting the form. Please correct the data.")
    
    else:
        form = QuoteForm()
        return render(request, 'quote.html', {'form':form})