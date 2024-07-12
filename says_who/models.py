from django.db import models

# Create your models here.
class Star(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Quote(models.Model):
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    quote = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.quote
    
class Question(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='quote_question')
    star = models.ForeignKey(Star, related_name='star_question', on_delete=models.CASCADE)

    def __str__(self):
        return f'Who said "{self.quote}"?'

class Life(models.Model):
    life = models.IntegerField(max_length=2, default=3)
    points = models.IntegerField(max_length=3, default=0)