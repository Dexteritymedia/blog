from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.utils.functional import cached_property

from wagtail.blocks import (
    BooleanBlock,
    CharBlock,
    FieldBlock,
    ListBlock,
    PageChooserBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    StructValue,
    URLBlock,
    IntegerBlock,
    ChoiceBlock,
    EmailBlock,
    DateBlock,
)
from wagtail.blocks.struct_block import StructBlockValidationError
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class HeroBlock(StructBlock):

    image = ImageChooserBlock(required=True)
    text = RichTextBlock()
    button_page = PageChooserBlock(required=False)
    url = URLBlock(required=False)
    button_text = CharBlock(default="Click")


    class Meta:
        template = "portfolio/blocks/hero_block.html"
        icon = "title"
        label = "Hero"
        max_num = 1


class AboutBlock(StructBlock):

    title = CharBlock(required=True, default="ABOUT ME", help_text="Add your title")
    image = ImageChooserBlock(required=True)
    text = RichTextBlock()
    phone_no = CharBlock(required=False)
    email = EmailBlock(required=False)
    website = URLBlock(required=False)

    social_media = ListBlock(
        StructBlock(
            [
                ('name', CharBlock(required=False, help_text='Add name of the social media')),
                ('link', URLBlock(required=False, help_text='If the button page above is selected, that will be used first')),
                ('fontawesome_icon_tag', CharBlock(default="fa fa-facebook", help_text="For example to add facebook logo just add this 'fa fa-facebook' ", required=False)),
            ]
        )
    )
                


    class Meta:
        template = "portfolio/blocks/about_block.html"
        icon = "view"
        label = "About"
        max_num = 1


class EducationBlock(StructBlock):
    title = CharBlock(required=True, default="Education", help_text="Add your title")

    details = ListBlock(
        StructBlock(
            [
                ('year_start', CharBlock(required=False, help_text="Add your title")),
                ('year_end', CharBlock(required=False, help_text="Add your title")),
                ('course', CharBlock(required=False, help_text="Add your title")),
                ('name_of_varsity', CharBlock(required=False, help_text="Add your title")),
                ('varsity_state_and_country', CharBlock(required=False, help_text="Add your title")),
                ('text', RichTextBlock(required=False,)),
            ]
        )
    )

    class Meta:
        template = "portfolio/blocks/education_block.html"
        icon = "edit"
        label = "Education"

class SkillBlock(StructBlock):
    title = CharBlock(required=True, default="Skills", help_text="Add your title")

    details = ListBlock(
        StructBlock(
            [
                ('skill', CharBlock(required=True, help_text="Add your title")),
                ('number', IntegerBlock(required=False, help_text="Add your title")),
            ]
        )
    )

    class Meta:
        template = "portfolio/blocks/skill_block.html"
        icon = "plus"
        label = "Skill"

class ExperienceBlock(StructBlock):
    title = CharBlock(required=True, default="Experience", help_text="Add your title")

    details = ListBlock(
        StructBlock(
            [
                ('select', ChoiceBlock(choices=[
                    ('left', 'Left'),
                    ('right', 'Right'),
                ], blank=True, required=False)
                ),
                ('year_start', DateBlock(required=True, help_text="Add your title")),
                ('year_end', CharBlock(required=True, help_text="Add your title")),
                ('position', CharBlock(required=True, help_text="Add your title")),
                ('name_of_organization', CharBlock(required=True, help_text="Enter the organization or company name you previously worked for")),
                ('location', CharBlock(required=True, help_text="Enter where the organization or company is located")),
                ('text', RichTextBlock()),
            ]
        )
    )

    class Meta:
        template = "portfolio/blocks/experience_block.html"
        icon = "repeat"
        label = "Experience"


class ClientBlock(StructBlock):
    title = CharBlock(required=True, default="Client", help_text="Add your title")
    
    client = ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('name', CharBlock(required=False)),
                ('link', URLBlock(help_text="Enter a valid url to the company website page", required=False)),
            ]
        )
    )

    class Meta:
        template = "portfolio/blocks/client_block.html"
        icon = "group"
        label = "Client"


class PortfolioBlock(StructBlock):
    title = CharBlock(required=True, default="Portfolio", help_text="Add your title")
    
    work = ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('name', CharBlock(required=False)),
                ('link', PageChooserBlock(help_text="Select a page", required=False, target_model=['portfolio.PortfolioPage'])),
                ('secondary_image', ImageChooserBlock(required=False)),
                ('secondary_name', CharBlock(required=False)),
                ('secondary_link', PageChooserBlock(help_text="Select a page", required=False, target_model=['portfolio.PortfolioPage'])),
            ]
        )
    )

    class Meta:
        template = "portfolio/blocks/portfolio_block.html"
        icon = "mail"
        label = "Portfolio"

        
class ProfileBlock(StructBlock):

    title = CharBlock(required=True, default="Profile", help_text="Add your title")

    profile = ListBlock(
        StructBlock(
            [
                ('name', CharBlock(required=False, help_text="Enter the name")),
                ('fontawesome_icon_tag', CharBlock(help_text="Add for example to add behance logo just add this 'flaticon-behance-logo' ", required=False)),
                ('link', URLBlock(help_text="Enter a valid url to your profile page", required=False)),
            ]
        )
    )

    class Meta:
        template = "portfolio/blocks/profile_block.html"
        icon = "user"
        label = "Profile"

class BodyBlock(StreamBlock):
    hero = HeroBlock(
        form_classname="title",
        icon="title",
        template="portfolio/blocks/hero_block.html",
    )
    experience = ExperienceBlock(
        form_classname="title",
        icon="repeat",
        template="portfolio/blocks/hero_block.html",
    )
    skill = SkillBlock(
        form_classname="title",
        icon="plus",
        template="portfolio/blocks/hero_block.html",
    )
    education = EducationBlock(
        form_classname="title",
        icon="edit",
        template="portfolio/blocks/hero_block.html",
    )
    client = ClientBlock(
        form_classname="title",
        icon="group",
        template="portfolio/blocks/hero_block.html",
    )
    profile = ProfileBlock(
        form_classname="title",
        icon="user",
        template="portfolio/blocks/hero_block.html",
    )
    portfolio = PortfolioBlock(
        form_classname="title",
        icon="mail",
        template="portfolio/blocks/hero_block.html",
    )
    about = AboutBlock(
        form_classname="title",
        icon="view",
        template="portfolio/blocks/hero_block.html",
    )
    

    class Meta:
        template = "portfolio/blocks/stream_block.html"
