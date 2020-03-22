from django import template

register = template.Library()


@register.filter
def video(value):
    tail = value.split("Seagate Expansion Drive")[-1].split("/")[1:]
    return "/".join(["/video"] + tail)
