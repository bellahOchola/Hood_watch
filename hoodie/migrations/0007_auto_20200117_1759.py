# Generated by Django 3.0.2 on 2020-01-17 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodie', '0006_post_hoodie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='hoodie',
            new_name='hoody',
        ),
    ]
