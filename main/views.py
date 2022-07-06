from django.shortcuts import render, redirect
from .forms import *
from .models import Catalog, Anketa
from django.views.generic import DetailView


def index(request):
    playlists = Catalog.objects.all()
    return render(request, 'main/index.html', {'playlists': playlists})


def profile(request):
    tracks = Anketa.objects.filter(user=request.user)
    drumKit = DrumKit.objects.filter(user=request.user)
    return render(request, 'registration/profile.html', {'tracks': tracks, 'drumkit': drumKit})


class PlaylistDetailView(DetailView):
    model = Catalog
    template_name = 'main/playlist_detail.html'
    context_object_name = 'playlists'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'main/index.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def add_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            Anketa = form.save(commit=False)
            Anketa.user = request.user
            form.save()
            return redirect('/profile')
    else:
        form = TrackForm()
    return render(request, 'main/track_edit.html', {'form': form})


def add_drumKit(request):
    if request.method == 'POST':
        kitForm = DrumKitForm(request.POST, request.FILES)
        if kitForm.is_valid():
            new_KitForm = kitForm.save(commit=False)
            new_KitForm.user = request.user
            new_KitForm.save()
            return redirect('/profile')
    else:
        form = DrumKitForm()
    return render(request, 'main/drumKit_edit.html', {'form': form})


def deleteTrack(request, pk):
    track = Anketa.objects.get(id=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('/profile')
    context = {'item': track}
    return render(request, 'main/deleteTrack.html', context)


def tracks(request):
    allTracks = Anketa.objects.all()
    return render(request, 'main/allTrack.html', {'tracks': allTracks})
