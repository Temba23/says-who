from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import star, quote, question, game

urlpatterns = [
    path('star/', star, name="create-star"),
    path('quote/', quote, name="create-quote"),
    # path('question/', question, name="create-question"),
    path('game/', game, name="game"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)