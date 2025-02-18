<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recommended Movies</title>
</head>
<body>
    <h1>Recommended Movies for Genre: {{ genre }}</h1>
    <p>You selected: {{ selected_movie }}</p>

    <table border="1">
        <thead>
            <tr>
                <th>Recommended Movies</th>
            </tr>
        </thead>
        <tbody>
            {% for movie in recommended_movies %}
                <tr>
                    <td>{{ movie }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

    <a href="{% url 'newDisplay' %}">Choose another movie</a>
</body>
</html>