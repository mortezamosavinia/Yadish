from django.contrib import admin
from .models import Pond, FeedingRule, FeedingInput


@admin.register(Pond)
class PondAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FeedingRule)
class FeedingRuleAdmin(admin.ModelAdmin):
    list_display = (
        'min_temp',
        'max_temp',
        'min_weight',
        'max_weight',
        'feed_size',
        'feeding_times',
        'adaptation',
    )
    list_filter = ('adaptation',)
    search_fields = ('feed_size',)


@admin.register(FeedingInput)
class FeedingInputAdmin(admin.ModelAdmin):
    list_display = (
        'pond',
        'water_temp',
        'fish_weight',
        'fish_count',
        'created_at',
    )
    list_filter = ('pond', 'created_at')
