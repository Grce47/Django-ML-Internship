# Generated by Django 4.0.4 on 2022-06-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='temp', max_length=150)),
                ('session_key', models.CharField(default='temp', max_length=150)),
                ('first_name', models.CharField(default='temp', max_length=150)),
                ('last_name', models.CharField(default='temp', max_length=150)),
                ('email', models.EmailField(default='temp@temp.com', max_length=150)),
                ('password1', models.CharField(default='temp', max_length=150)),
                ('password2', models.CharField(default='temp', max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
