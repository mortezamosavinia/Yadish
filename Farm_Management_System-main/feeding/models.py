from django.db import models


class Pond(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FeedingRule(models.Model):
    min_temp = models.FloatField()
    max_temp = models.FloatField()

    min_weight = models.FloatField()
    max_weight = models.FloatField()

    feed_size = models.FloatField()
    feeding_times = models.IntegerField()
    adaptation = models.BooleanField(default=False)

    def __str__(self):
        return f"T {self.min_temp}-{self.max_temp} | W {self.min_weight}-{self.max_weight}"


from django.db import models

class FeedingInput(models.Model):
    pond = models.ForeignKey('Pond', on_delete=models.CASCADE)
    water_temp = models.FloatField()
    fish_length = models.FloatField()
    fish_weight = models.FloatField()
    fish_count = models.IntegerField()

    # خروجی‌های محاسبه‌شده
    biomass = models.FloatField()
    feed_size = models.CharField(max_length=20)
    feeding_times = models.IntegerField()
    adaptation = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pond} - {self.created_at.date()}"
