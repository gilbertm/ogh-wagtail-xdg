from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    existing_classes = field.field.widget.attrs.get('class', '')
    updated_classes = f"{existing_classes} {css_class}".strip()
    field.field.widget.attrs['class'] = updated_classes
    return field
