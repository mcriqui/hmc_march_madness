from django.db import models
from django import forms


class Ranking(models.Model):

    school_name = models.CharField(max_length=50, null=True, blank=True)
    mascot_name = models.CharField(max_length=25, null=True, blank=True)
    experience_ranking = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    bracket_seed = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    offensive_rebound_ranking = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    steals_ranking = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    away_games_ranking = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.school_name

