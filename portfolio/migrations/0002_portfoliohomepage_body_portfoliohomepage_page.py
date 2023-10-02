# Generated by Django 4.2.3 on 2023-09-26 21:47

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliohomepage',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('header', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('subtitle', wagtail.blocks.CharBlock(max_length=40, required=False)), ('main_text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link'], required=True)), ('page_button_text', wagtail.blocks.CharBlock(help_text='Enter a hexdecimal color for the background e.g #000000', max_length=40, required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first', required=False))])))], form_classname='title', icon='title', template='portfolio/blocks/hero_block.html'))], blank=True, use_json_field=True),
        ),
        migrations.AddField(
            model_name='portfoliohomepage',
            name='page',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('header', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('subtitle', wagtail.blocks.CharBlock(max_length=40, required=False)), ('main_text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link'], required=True)), ('page_button_text', wagtail.blocks.CharBlock(help_text='Enter a hexdecimal color for the background e.g #000000', max_length=40, required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first', required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]