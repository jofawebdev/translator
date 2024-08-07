from django.shortcuts import render, redirect
from googletrans import Translator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Translation

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
    


def logout_view(request):
    logout(request)
    return redirect('login') # Redirect to the login page after logging out 