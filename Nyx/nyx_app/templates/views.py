# mbti_app/views.py

from django.shortcuts import render, redirect
from ..models import UserInput
from ..forms import MBTIForm

def home(request):
    if request.method == 'POST':
        form = MBTIForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']

            predicted_mbti = 'INFJ' 
            UserInput.objects.create(text=text, predicted_mbti=predicted_mbti)
            return redirect('home')
    else:
        form = MBTIForm()

    user_inputs = UserInput.objects.all()
    return render(request, '/workspaces/Nyx/Nyx/nyx_app/templates/home.html', {'form': form, 'user_inputs': user_inputs})

