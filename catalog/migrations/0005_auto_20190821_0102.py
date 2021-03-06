# Generated by Django 2.2.3 on 2019-08-21 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190819_0719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_add_authors', 'Can add authors'),)},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_add_books', 'Can add books'),)},
        ),
    ]
