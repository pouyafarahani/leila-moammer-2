from django import template

register = template.Library()


@register.filter
def translate_day(value):
    value = str(value)
    my_dict = {
        'Saturday': 'شنبه',
        'Sunday': 'یکشنبه',
        'Monday': 'دوشنبه',
        'Tuesday': 'سه شنبه',
        'Wednesday': 'چهارشنبه',
        'Thursday': 'چنج شنبه',
        'Friday': 'جمعه',

    }
    english_to_persian_tags = value.translate(my_dict)
    return my_dict[value]

