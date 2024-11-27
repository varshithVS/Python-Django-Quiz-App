from django import template

register = template.Library()

@register.filter
def get_option(question, option_number):
    # Retrieve the option dynamically using getattr
    option_field = f"option{option_number}"
    return getattr(question, option_field)
