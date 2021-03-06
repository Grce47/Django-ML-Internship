# Generated by Django 4.0.4 on 2022-06-22 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_orders_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='temp', max_length=150)),
                ('session_key', models.CharField(default='temp', max_length=150)),
                ('first_name', models.CharField(default='temp', max_length=150)),
                ('last_name', models.CharField(default='temp', max_length=150)),
                ('email', models.EmailField(default='temp@temp.com', max_length=150)),
                ('password1', models.CharField(default='temp', max_length=150)),
                ('password2', models.CharField(default='temp', max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_joined', models.CharField(default='temp', max_length=150)),
                ('method', models.CharField(default='temp', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
