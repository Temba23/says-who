from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import star

urlpatterns = [
    path('star/', star, name="create-star")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)