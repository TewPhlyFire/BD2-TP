from django import template

register = template.Library()

@register.filter
def dict_has_key(dictionary, key):
    return key in dictionary

@register.filter
def dict_get(dictionary, key):
    return dictionary.get(key, "")
