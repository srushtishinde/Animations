# Generated by Django 4.0.3 on 2022-10-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animations', '0003_alter_animation_file01'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animation',
            name='file01',
            field=models.CharField(max_length=256),
        ),
    ]
