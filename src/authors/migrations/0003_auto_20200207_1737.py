# Generated by Django 3.0 on 2020-02-07 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20200207_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name': 'author', 'verbose_name_plural': 'authors'},
        ),
    ]
