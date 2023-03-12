from django import template
from django.template.loader import get_template

register = template.Library()

temp = get_template('tags/form_table_row.html')

@register.inclusion_tag(temp)
def form_table_row(form_field):
    return {'form_field': form_field }