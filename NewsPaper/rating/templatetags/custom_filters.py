from django import template
 
register = template.Library()

@register.filter(name='Censor')

def Censor(value):
    s = str(value)
    l = s.split("bad_word")
    s1 = '***'.join(l)
    return s1