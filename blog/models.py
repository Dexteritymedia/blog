import datetime

from django.db import models
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.dateformat import DateFormat
from django.utils.formats import date_format
from django.utils.functional import cached_property

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.fields import StreamField, RichTextField

from taggit.models import Tag as TaggitTag
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.tags import ClusterTaggableManager

from home.blocks import BodyBlock

# Create your models here.

class BlogPage(Page):
    template = "blog/home.html"
    subpage_types = [
        'blog.BlogPostPage',
        'blog.BlogTagIndexPage',
        ]

    class Meta:
        verbose_name = "Copywriting Blog"
        verbose_name_plural = "Copywriting Blog"


class BlogPostPage(Page):
    template = "blog/post_page.html"
    parent_page_types = [
        'blog.BlogPage'
        ]
    subpage_types = [
        'blog.BlogPostPage'
        ]
    
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    tags = ClusterTaggableManager(through="blog.PostPageTag", blank=True)

    body = StreamField(BodyBlock(), blank=True, use_json_field=True)

    post_date = models.DateTimeField(
        verbose_name="Post date", default=datetime.datetime.today
    )

    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
        InlinePanel("categories", label="category"),
        FieldPanel("tags"),
        FieldPanel("body"),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel("post_date"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]

    class Meta:
        verbose_name = "Post"


class BlogTagIndexPage(Page):
    template = "blog/tag_page.html"
    max_count = 1
    parent_page_types = [
        'blog.BlogPage'
        ]
    subpage_types = [
        'blog.BlogTagIndexPage'
        ]

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

    class Meta:
        verbose_name = "Tag"


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Copywriting Blog Category"
        verbose_name_plural = "Copywriting Blog Categories"

"""
@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
"""

class PostPageBlogCategory(models.Model):
    page = ParentalKey(
        "blog.BlogPostPage", on_delete=models.CASCADE, related_name="categories"
    )
    blog_category = models.ForeignKey(
        "blog.BlogCategory", on_delete=models.CASCADE, related_name="post_pages"
    )

    panels = [
        FieldPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category")


class PostPageTag(TaggedItemBase):
    content_object = ParentalKey("blog.BlogPostPage", related_name="post_tags")

