# Generated by Django 4.2.8 on 2024-06-28 08:31

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
        ('home', '0006_sitesocial_sitelogo_sitecontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantExtraContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sidebar_about', wagtail.fields.RichTextField(blank=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
