from django import forms

# Sample movie list
MOVIE_CHOICES = [
    ("inception", "Inception"),
    ("the shawshank redemption", "The Shawshank Redemption"),
    ("the exorcist", "The Exorcist"),
    ("superbad", "Superbad"),
    ("mad max: fury road", "Mad Max: Fury Road"),
    ("the avengers", "The Avengers"),
]

class NewForm(forms.Form):
    movie = forms.ChoiceField(choices=MOVIE_CHOICES, label='Choose a movie')