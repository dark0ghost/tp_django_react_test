# Generated by Django 3.2 on 2021-05-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0006_momentmodel_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='momentmodel',
            name='tags',
            field=models.ManyToManyField(default=None, to='tech.TagModel'),
        ),
    ]
