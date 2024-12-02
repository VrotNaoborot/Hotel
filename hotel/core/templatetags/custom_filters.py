from django import template

register = template.Library()
print("Custom filters loaded")


@register.filter
def thousand_separator(value):
    try:
        return f"{int(value):,}".replace(",", " ")
    except (ValueError, TypeError):
        return value
