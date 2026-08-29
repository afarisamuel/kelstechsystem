from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='break_amp')
def break_amp(value):
    """
    Breaks a title into two lines at ' & ' or ' &amp; '.
    Example: 'Kels Technologies & Systems' -> 'Kels Technologies<br>&amp; Systems'
    """
    if not value:
        value = 'Kels Technologies & Systems'
    val_str = str(value)
    if ' & ' in val_str:
        parts = val_str.split(' & ', 1)
        return mark_safe(f'{parts[0]}<br>&amp; {parts[1]}')
    elif ' &amp; ' in val_str:
        parts = val_str.split(' &amp; ', 1)
        return mark_safe(f'{parts[0]}<br>&amp; {parts[1]}')
    return val_str
