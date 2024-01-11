from django.shortcuts import render
from .models import AIModel
from plugins.spotify.plugin import SpotifyPlugin

def index(request):
    ai_model = AIModel.objects.all()
    context = {'ai_model': ai_model}
    return render(request, 'ai_model/index.html', context)

def handle_command(request, command):
    if 'spotify' in command:
        spotify_plugin = SpotifyPlugin()
        if 'login' in command:
            spotify_plugin.login()
        elif 'play my music' in command:
            try:
                spotify_plugin.play_music()
            except Exception as e:
                if 'not logged in' in str(e):
                    spotify_plugin.login()
                    spotify_plugin.play_music()
    return render(request, 'ai_model/index.html')