# Generated by Django 3.0.2 on 2020-01-17 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodie', '0004_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodie.Hood'),
        ),
    ]
