# Generated by Django 3.0.8 on 2020-07-21 12:22

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('blog', '0002_auto_20200721_1218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
