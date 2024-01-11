from django.shortcuts import render
from .models import SpotifyUser
from .plugin import SpotifyPlugin

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        spotify_user = SpotifyUser.objects.filter(username=username).first()
        if spotify_user:
            spotify_plugin = SpotifyPlugin(spotify_user)
            try:
                spotify_plugin.login(username, password)
                return render(request, 'spotify/success.html')
            except Exception as e:
                return render(request, 'spotify/error.html', {'error': str(e)})
        else:
            return render(request, 'spotify/error.html', {'error': 'User not found'})
    else:
        return render(request, 'spotify/login.html')

def play_music(request):
    spotify_user = SpotifyUser.objects.filter(username=request.user.username).first()
    if spotify_user:
        spotify_plugin = SpotifyPlugin(spotify_user)
        if spotify_plugin.is_logged_in():
            try:
                spotify_plugin.play_music()
                return render(request, 'spotify/success.html')
            except Exception as e:
                return render(request, 'spotify/error.html', {'error': str(e)})
        else:
            try:
                spotify_plugin.login()
                spotify_plugin.play_music()
                return render(request, 'spotify/success.html')
            except Exception as e:
                return render(request, 'spotify/error.html', {'error': str(e)})
    else:
        return render(request, 'spotify/error.html', {'error': 'User not found'})