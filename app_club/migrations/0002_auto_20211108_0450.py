# Generated by Django 3.1.3 on 2021-11-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postscript',
            name='post_score',
            field=models.FloatField(blank=True, default=0),
        ),
    ]