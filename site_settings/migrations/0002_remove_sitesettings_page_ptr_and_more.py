# Generated by Django 4.2.3 on 2023-09-14 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='site_logo',
        ),
        migrations.DeleteModel(
            name='HeaderLinks',
        ),
        migrations.DeleteModel(
            name='SiteSettings',
        ),
    ]