# Generated by Django 4.2.8 on 2024-07-24 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_alter_paymentplan_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentplanwidget',
            name='payment_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_plan_schedule', to='dashboard.paymentplan'),
        ),
    ]