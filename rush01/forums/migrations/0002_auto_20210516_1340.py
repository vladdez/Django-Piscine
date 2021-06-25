# Generated by Django 3.2.2 on 2021-05-16 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.CharField(default='anonymous', max_length=200, null=True),
        ),
    ]
