# Generated by Django 4.0.4 on 2022-04-22 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_state_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='carbodywork',
            options={'verbose_name': 'Кузов', 'verbose_name_plural': 'Кузовы'},
        ),
        migrations.AlterModelOptions(
            name='carbrand',
            options={'verbose_name': 'Марка', 'verbose_name_plural': 'Марки'},
        ),
        migrations.AlterModelOptions(
            name='carcoverage',
            options={'verbose_name': 'Покрытие', 'verbose_name_plural': 'Покрытия'},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AlterModelOptions(
            name='carsalon',
            options={'verbose_name': 'Салон', 'verbose_name_plural': 'Салоны'},
        ),
        migrations.AlterField(
            model_name='car',
            name='state_number',
            field=models.CharField(max_length=20, verbose_name='Госномер'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.carclass'),
            preserve_default=False,
        ),
    ]