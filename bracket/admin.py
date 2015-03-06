from django.contrib import admin
from bracket.models import Ranking


class RankingAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'mascot_name')

admin.site.register(Ranking, RankingAdmin)

