from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Star, Question, Quote
from .forms import StarForm, QuoteForm
from django.contrib import messages
import random

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
                messages.success(request, f"{star_name} created successfully. Create a Quote for {star_name}.")
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
                messages.error(request, f"Quote already exists for {star}")
                return redirect('create-quote')
            print(star, quote)
            quote_instance = form.save()
            print(quote_instance)
            Question.objects.create(star=star, quote=quote_instance)
            messages.success(request, f'Quote created successfully for {star}.')
            return redirect('create-quote')
        
        else:
            form.add_error(request, "Error submitting the form. Please correct the data.")
    
    else:
        form = QuoteForm()
        return render(request, 'quote.html', {'form':form})
    
# def question(request):
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             quote = form.cleaned_data['quote']
#             star = form.cleaned_data['star']
#             if Question.objects.filter(star=star).exists():
#                 messages.error(request, f"Question already exists for {star}")   
#             else:
#                 s_instance = Star.objects.create(name=star)
#                 Quote.objects.create(star=s_instance, quote=quote)
#                 messages.success(request, f'{Question} created successfully.') 
#             return redirect('create-question')

#     else:
#         form = QuestionForm()
#         return render(request, 'question.html', {'form':form})
    
def game(request):  
    question = Question.objects.order_by('?').first()
    correct_answer = question.star

    incorrect_answers = Star.objects.exclude(id=correct_answer.id).order_by('?')[:3]

    answers = list(incorrect_answers) + [correct_answer]
    random.shuffle(answers)

    if request.method == 'POST':
        selected_answer_id = request.POST.get('answer')
        selected_answer = get_object_or_404(Star, id=selected_answer_id)
        if selected_answer == correct_answer:
            result = "Correct!"
        else:
            result = "Incorrect. The correct answer was " + correct_answer.name + "."

        context = {
            'question': question,
            'answers': answers,
            'result': result
        }
    else:
        context = {
            'question': question,
            'answers': answers
        }
    
    return render(request, 'game.html', context)