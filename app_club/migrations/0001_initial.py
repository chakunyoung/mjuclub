# Generated by Django 3.1.3 on 2021-11-07 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_name', models.CharField(max_length=20)),
                ('club_admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app_user.user')),
                ('club_info', models.CharField(max_length=20)),
                ('club_contents', models.TextField(default='')),
                ('club_loc', models.CharField(max_length=20)),
                ('club_score', models.IntegerField(blank=True, default=0)),
                ('club_images', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='PostScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.TextField(default='')),
                ('post_score', models.IntegerField(blank=True, default=0)),
                ('club_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_club.club')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]