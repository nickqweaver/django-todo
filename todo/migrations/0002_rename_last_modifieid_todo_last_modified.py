# Generated by Django 3.2.3 on 2021-06-11 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='last_modifieid',
            new_name='last_modified',
        ),
    ]