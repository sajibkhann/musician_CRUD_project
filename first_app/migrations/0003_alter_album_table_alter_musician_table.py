# Generated by Django 4.1.2 on 2023-10-17 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_album_num_stars'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='album',
            table='album',
        ),
        migrations.AlterModelTable(
            name='musician',
            table='musician',
        ),
    ]
