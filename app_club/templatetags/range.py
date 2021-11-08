from django import template

register = template.Library()


# html 템플릿 태그 for문에서 range 사용을 위해 만들어 놓음
@register.filter(name='range')
def _range(start, end):
    end = round(end)
    return range(start, end)