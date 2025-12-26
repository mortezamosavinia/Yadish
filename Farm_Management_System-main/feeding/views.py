from django.shortcuts import render
from .models import FeedingRule, Pond
from .models import FeedingInput


def calculate_feeding(request):
    result = None

    if request.method == 'POST':
        pond_id = request.POST.get('pond')
        water_temp = float(request.POST.get('water_temp'))
        fish_weight = float(request.POST.get('fish_weight'))
        fish_length = float(request.POST.get('fish_length'))
        fish_count = int(request.POST.get('fish_count'))

        biomass = round((fish_weight * fish_count) / 1000, 2)
        if not pond_id:
            return render(request, 'feeding/calculate.html', {
                'ponds': Pond.objects.all(),
                'result': {
                    'biomass': '—',
                    'feed_size': '—',
                    'feeding_times': '—',
                    'adaptation': 'لطفاً استخر را انتخاب کنید'
                }
            })

        FeedingInput.objects.create(
            pond_id=pond_id,
            water_temp=water_temp,
            fish_length=fish_length,
            fish_weight=fish_weight,
            fish_count=fish_count,
        )

        rule = FeedingRule.objects.filter(
            min_temp__lte=water_temp,
            max_temp__gte=water_temp,
            min_weight__lte=fish_weight,
            max_weight__gte=fish_weight
        ).first()

        if rule:
            result = {
                'biomass': biomass,
                'feed_size': rule.feed_size,
                'feeding_times': rule.feeding_times,
                'adaptation': 'بله' if rule.adaptation else 'خیر'
            }
        else:
            result = {
                'biomass': biomass,
                'feed_size': 'نامشخص',
                'feeding_times': 'نامشخص',
                'adaptation': 'نامشخص'
            }

    ponds = Pond.objects.all()

    return render(request, 'feeding/calculate.html', {
        'ponds': ponds,
        'result': result
    })
