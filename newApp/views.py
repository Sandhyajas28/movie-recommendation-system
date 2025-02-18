from django.shortcuts import render, redirect
from .forms import NewForm

# Example movie recommendations by genre
GENRE_RECOMMENDATIONS = {
    'Action': ['Mad Max: Fury Road', 'John Wick', 'Die Hard', 'The Matrix', 'Gladiator'],
    'Horror': ['The Exorcist', 'Get Out', 'A Quiet Place', 'Hereditary', 'It'],
    'Superhero': ['The Avengers', 'Black Panther', 'Wonder Woman', 'Spider-Man: Far From Home', 'Thor: Ragnarok'],
    'Comedy': ['Superbad', 'The Hangover', 'Step Brothers', 'Anchorman', 'Bridesmaids'],
    'Drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather', 'Fight Club', 'Pulp Fiction'],
    'Sci-Fi': ['Inception', 'Blade Runner 2049', 'Interstellar', 'Dune', 'Ex Machina'],
}

# Movies with genres
MOVIE_GENRES = {
    'inception': 'Sci-Fi',
    'the shawshank redemption': 'Drama',
    'the exorcist': 'Horror',
    'superbad': 'Comedy',
    'mad max: fury road': 'Action',
    'the avengers': 'Superhero',
}

def newDisplay(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            selected_movie = form.cleaned_data['movie'].lower()

            # Determine the genre of the selected movie
            genre = MOVIE_GENRES.get(selected_movie, '')
            if genre:
                # Get recommendations based on the genre
                recommended_movies = GENRE_RECOMMENDATIONS.get(genre, [])
                # Pass the recommendations to a new page
                return render(request, 'recommendations.html', {
                    'selected_movie': selected_movie,
                    'recommended_movies': recommended_movies,
                    'genre': genre,
                })
            else:
                return render(request, 'index.html', {
                    'form': form,
                    'error_message': "No genre information available for the selected movie."
                })
    else:
        form = NewForm()

    return render(request, 'index.html', {"form": form})