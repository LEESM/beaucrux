from django import template
register = template.Library()

@register.filter(name='times')
def times(count):
    return range(int(count))