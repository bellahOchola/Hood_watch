# Generated by Django 3.0.2 on 2020-01-17 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodie', '0005_profile_hood'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hoodie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodie.Hood'),
        ),
    ]
