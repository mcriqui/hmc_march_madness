from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from bracket.models import Ranking

# Create your views here.

class SelectTeamForm(forms.Form):
    first_team = forms.ModelChoiceField(queryset=Ranking.objects.all(), empty_label=None)
    second_team = forms.ModelChoiceField(queryset=Ranking.objects.all(), empty_label=None)


def get_template(request):
    form = SelectTeamForm(request.GET)
    pick = None
    if form.is_valid():
        team1 = form.cleaned_data['first_team']
        team2 = form.cleaned_data['second_team']
        if team1.bracket_seed < team2.bracket_seed:
            team1_score = 1
            team2_score = 0
        elif team2.bracket_seed < team1.bracket_seed:
            team2_score = 1
            team1_score = 0
        else:
            team1_score = 0
            team2_score = 0
        if team1.experience_ranking > team2.experience_ranking:
            team1_score = team1_score + 1
        elif team2.experience_ranking > team1.experience_ranking:
            team2_score = team1_score + 1
        if team1_score > team2_score:
            pick = team1
        elif team2_score > team1_score:
            pick = team2
        else:
            pick = "It's a tie!"
    context = {'form': form, 'pick':pick}
    return render(request, 'home.html', context)
