# Generated by Django 4.2.7 on 2023-12-12 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitterclone', '0002_profile_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='meeps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
