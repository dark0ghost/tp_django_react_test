# Generated by Django 3.2 on 2021-05-07 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0004_alter_tagmodel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='momentmodel',
            name='tags',
        ),
    ]
