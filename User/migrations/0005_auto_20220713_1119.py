# Generated by Django 4.0.4 on 2022-07-13 11:19

from django.db import migrations
from django.contrib.auth.models import User
def initialize(apps, schema_editor):
    for i in range(1,101):
        t = User.objects.create_user(username="TM202200"+str(i), password="TM202200"+str(i))
        t.save()

class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_order_date'),
    ]

    operations = [
	migrations.RunPython(initialize)
    ]
