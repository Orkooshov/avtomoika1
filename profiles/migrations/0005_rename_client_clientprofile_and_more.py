# Generated by Django 4.0.4 on 2022-04-26 16:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carclass_alter_car_options_alter_carbodywork_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_alter_staff_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='ClientProfile',
        ),
        migrations.AlterModelOptions(
            name='clientprofile',
            options={'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
    ]