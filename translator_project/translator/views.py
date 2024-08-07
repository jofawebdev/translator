from django.shortcuts import render, redirect
from googletrans import Translator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Translation
from .forms import CustomUserCreationForm

# Create your views here.
@login_required
def translate_text(request):
    if request.method == 'POST':
        source_text = request.POST.get('source_text')
        source_language = request.POST.get('source_language', 'auto')
        target_language = request.POST.get('target_language', 'en')

        translator = Translator()
        translated_text = translator.translate(source_text, src=source_language, dest=target_language).text


        # Save translation to the database
        Translation.objects.create(
            user=request.user,
            source_text=source_text,
            translated_text=translated_text,
            source_language=source_language,
            target_language=target_language,
        )

        context = {
            'source_text': source_text,
            'translated_text': translated_text,
            'source_language': source_language,
            'target_language': target_language,
        }


        return render(request, 'translator/index.html', context)
    else:
        return render(request, 'translator/index.html')
    


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('translate_text') # redirect to the translation page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('translate_text')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})
    


def logout_view(request):
    logout(request)
    return redirect('login') # Redirect to the login page after logging out 