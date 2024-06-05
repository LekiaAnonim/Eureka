# Generated by Django 4.2.8 on 2024-06-05 23:36

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('heading_title', models.CharField(blank=True, max_length=500, null=True)),
                ('banner', models.ImageField(blank=True, help_text='upload image banner to display.', null=True, upload_to='')),
                ('intro', wagtail.fields.RichTextField(blank=True, null=True)),
                ('modules', wagtail.fields.StreamField([('introduction', wagtail.blocks.RichTextBlock(required=False)), ('module1', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module2', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module3', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module4', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module5', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module6', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module7', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module8', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module9', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module10', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module11', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module12', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module13', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module14', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module15', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module16', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module17', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module18', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module19', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('module20', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('duration', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False)), ('what_you_will_learn', wagtail.blocks.RichTextBlock(required=False))])), ('more_text', wagtail.blocks.RichTextBlock(required=False))], blank=True, null=True)),
                ('course_tip_1', wagtail.fields.RichTextField(blank=True, null=True)),
                ('course_tip_2', wagtail.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DeliveryMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_mode', models.CharField(help_text='e.g Online, In-person, etc', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Job title e.g. Data Analyst', max_length=500, null=True)),
                ('description', wagtail.fields.RichTextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, help_text='Job location e.g. Remote', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocationSchedule',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('heading_title', models.CharField(blank=True, max_length=500, null=True)),
                ('intro', wagtail.fields.RichTextField(blank=True, help_text='Enter the class schedule content', null=True)),
                ('location', wagtail.fields.StreamField([('intro', wagtail.blocks.RichTextBlock(required=False)), ('location_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('map_url', wagtail.blocks.URLBlock(required=False)), ('more_text', wagtail.blocks.RichTextBlock(required=False))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProgramCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_category', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Program Categories',
            },
        ),
        migrations.CreateModel(
            name='ProgramType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_type', models.CharField(help_text='e.g Full-time, Part-time, etc', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupportTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='e.g. Instructional team, Career services', max_length=500, null=True)),
                ('description', wagtail.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('course_title', models.CharField(blank=True, max_length=500, null=True)),
                ('banner', models.ImageField(blank=True, help_text='upload image banner to display.', null=True, upload_to='')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('introduction', wagtail.fields.RichTextField(blank=True, null=True)),
                ('course_metric', wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('metric', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False))], blank=True, null=True)),
                ('course_metric1', wagtail.fields.RichTextField(blank=True, null=True)),
                ('course_metric2', wagtail.fields.RichTextField(blank=True, null=True)),
                ('course_metric3', wagtail.fields.RichTextField(blank=True, null=True)),
                ('program_benefit', wagtail.fields.RichTextField(blank=True, null=True)),
                ('become_a_professional', wagtail.fields.RichTextField(blank=True, null=True)),
                ('projects', wagtail.fields.RichTextField(blank=True, null=True)),
                ('course_model', wagtail.fields.RichTextField(blank=True, null=True)),
                ('student_support', wagtail.fields.RichTextField(blank=True, null=True)),
                ('jobs', wagtail.fields.StreamField([('introduction', wagtail.blocks.RichTextBlock(required=False)), ('job1', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False))])), ('job2', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False))])), ('job3', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False))])), ('job4', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False))])), ('job5', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False))])), ('more_text', wagtail.blocks.RichTextBlock(required=False))], blank=True, null=True)),
                ('career_services', wagtail.fields.RichTextField(blank=True, null=True)),
                ('testimonials', wagtail.fields.StreamField([('intro', wagtail.blocks.RichTextBlock(required=False)), ('person1', wagtail.blocks.StructBlock([('message', wagtail.blocks.RichTextBlock(required=False)), ('first_name', wagtail.blocks.CharBlock(required=False)), ('last_name', wagtail.blocks.CharBlock(required=False)), ('personal_info', wagtail.blocks.CharBlock(required=False))])), ('person2', wagtail.blocks.StructBlock([('message', wagtail.blocks.RichTextBlock(required=False)), ('first_name', wagtail.blocks.CharBlock(required=False)), ('last_name', wagtail.blocks.CharBlock(required=False)), ('personal_info', wagtail.blocks.CharBlock(required=False))])), ('paragraph', wagtail.blocks.RichTextBlock(required=False))], blank=True, null=True)),
                ('faq', wagtail.fields.StreamField([('faq1', wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=False)), ('answer', wagtail.blocks.RichTextBlock(required=False))])), ('faq2', wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=False)), ('answer', wagtail.blocks.RichTextBlock(required=False))])), ('faq3', wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=False)), ('answer', wagtail.blocks.RichTextBlock(required=False))])), ('faq4', wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=False)), ('answer', wagtail.blocks.RichTextBlock(required=False))])), ('faq5', wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=False)), ('answer', wagtail.blocks.RichTextBlock(required=False))])), ('faq6', wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=False)), ('answer', wagtail.blocks.RichTextBlock(required=False))]))], blank=True, null=True)),
                ('how_to_apply', wagtail.fields.RichTextField(blank=True, null=True)),
                ('course_schedule', wagtail.fields.RichTextField(blank=True, null=True)),
                ('delivery_mode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.deliverymode')),
                ('program_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.programcategory')),
                ('program_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.programtype')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]