# Generated by Django 4.0.4 on 2022-04-22 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carclass_alter_car_options_alter_carbodywork_options_and_more'),
        ('carwash', '0005_order_created_at_order_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carclass')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carwash.service')),
            ],
        ),
    ]
