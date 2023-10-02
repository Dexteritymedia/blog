from django import template

from ..models import BlogListingPage, BlogDetailPage

register = template.Library()

@register.inclusion_tag("sportsblog/include/categories.html", takes_context=True)
def get_all_categories(context):
    categories = BlogListingPage.objects.live().public().all()
    context['categories'] = categories
    return context

@register.inclusion_tag("sportsblog/include/blogs.html", takes_context=True)
def get_top_five_blogs(context):
    blogs = BlogDetailPage.objects.live().public().order_by('-first_published_at')[:5]
    context['blogs'] = blogs
    return context
