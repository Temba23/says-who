from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Star, Question, Quote, Life
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
    
def game(request):
    if request.method == 'POST':
        question_id = request.session.get('question_id')
        life_id = request.session.get('life')
        life_count = get_object_or_404(Life, id=life_id)
        question = get_object_or_404(Question, id=question_id)
        correct_answer = question.star

        selected_answer_id = request.POST.get('answer')
        selected_answer = get_object_or_404(Star, id=selected_answer_id)
        if selected_answer == correct_answer:
            messages.success(request, f'{selected_answer} is correct! 🎇')
        else:
            life_count.life += 1
            life_count.save()
            messages.error(request, f'{selected_answer} is incorrect! 👎')
        return redirect('game')

    else:
        question = Question.objects.order_by('?').first()
        request.session['question_id'] = question.id
        correct_answer = question.star

        incorrect_answers = Star.objects.exclude(id=correct_answer.id).order_by('?')[:3]

        answers = list(incorrect_answers) + [correct_answer]
        random.shuffle(answers)

        context = {
            'question': question,
            'answers': answers
        }

    return render(request, 'game.html', context)

def load_question(request):
    """
        First Creating an instance because of ForeignKey, Then filtering the name from db and using dictionary comprehension for next model.
    """
    stars_name = ['Henry Ford', 'Wayne Gretzky', 'Confucius', 'Vincent Van Gogh', 'Thomas Edison', 'Abraham Lincoln', 'Maya Angelou', 'John Wooden',
             'Bob Marley', 'Babe Ruth', 'Aristotle', 'Helen Keller', 'Nelson Mandela', 'Charles Dickens', 'J.Cole', 'K.Dot']
    quotes_text = [
        'Whether you think you can or you think you can’t, you are right.',
        'You miss 100% of the shots you don’t take.',
        'It does not matter how slowly you go as long as you do not stop.',
        'I would rather die of passion than of boredom.',
        'There is no substitute for hard work.',
        "In the end, it's not the years in your life that count. It's the life in your years.",
        "You will face many defeats in life, but never let yourself be defeated.",
        'Do not let making a living prevent you from making a life.',
        'Love the life you live. Live the life you love.',
        'Never let the fear of striking out keep you from playing the game.',
        'Love is composed of a single soul inhabiting two bodies.',
        "Life is either a daring adventure or nothing at all.",
        'The greatest glory in living lies not in never falling, but in rising every time we fall.',
        "Life is made of ever so many partings welded together.",
        "I'd rather be happy being myself than sad trying to please everyone else.",
        "Trynna strike a cord and it's probably a minor."
    ]
    try:
        
        stars = [Star(name=star) for star in stars_name]
        Star.objects.bulk_create(stars)
        
        stars_from_db = Star.objects.filter(name__in=stars_name)
        star_dict = {star.name: star for star in stars_from_db}
        print(star_dict)

        quotes = [Quote(star=star_dict[star], quote=quote) for star, quote in zip(stars_name, quotes_text)]
        Quote.objects.bulk_create(quotes)

        quotes_from_db = Quote.objects.filter(quote__in=quotes_text)
        quote_dict = {quote.quote: quote for quote in quotes_from_db}
        
        questions = [Question(star=star_dict[star], quote=quote_dict[quote]) for star, quote in zip(stars_name, quotes_text)]
        Question.objects.bulk_create(questions)

    except Exception as e:
        messages.error(request, str(e))
        return redirect('create-quote')
    messages.success(request, "Successfully Created Questions.")
    return redirect('create-quote')
