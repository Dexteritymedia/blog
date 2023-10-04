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

from .blocks import (
    HeroBlock,
    AboutBlock,
    ClientBlock,
    EducationBlock,
    ExperienceBlock,
    PortfolioBlock,
    ProfileBlock,
    SkillBlock,
    BodyBlock
)

# Create your models here.

class PortfolioHomePage(Page):
    page_description = "Use this page to create a portfolio website"
    template = "portfolio/home.html"
    subpage_types = [
        'portfolio.PortfolioPage',
        ]

    #page = StreamField(BodyBlock(), blank=True, use_json_field=True)

    body = StreamField(
        [
            ('hero', HeroBlock()),
            ('about', AboutBlock()),
            ('client', ClientBlock()),
            ('education', EducationBlock()),
            ('experience', ExperienceBlock()),
            ('portfolio', PortfolioBlock()),
            ('profile', ProfileBlock()),
            ('skill', SkillBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
        block_counts = {
            'about': {'max_num': 1},
            'education': {'max_num': 1},
        },
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        #FieldPanel("page"),
    ]


    class Meta:
        verbose_name = "Portfolio website"
        verbose_name_plural = "Portfolio websites"


class PortfolioPage(Page):
    template = "portfolio/page.html"
    parent_page_types = [
        'portfolio.PortfolioHomePage'
        #'portfolio.PortfolioPage',
        ]
    #subpage_types = []
    page_description = "Use this page for addings projects completed"
