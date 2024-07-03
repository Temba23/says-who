from django.shortcuts import render, HttpResponse, redirect
from .models import Star, Question, Quote
from .forms import StarForm, QuoteForm, QuestionForm
from django.contrib import messages


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
                messages.success(request, f"{star_name} created successfully.")
                return redirect("create-quote")
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
            if Quote.objects.filter(star=star).exists():
                return HttpResponse(f"Quote for {star} already exists.")
            print(star, quote)
            form.save()
            return HttpResponse("Quote Added to the Star Successfully.")
        
        else:
            form.add_error(request, "Error submitting the form. Please correct the data.")
    
    else:
        form = QuoteForm()
        return render(request, 'quote.html', {'form':form})
    
def question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success.")

    else:
        form = QuestionForm()
        return render(request, 'question.html', {'form':form})