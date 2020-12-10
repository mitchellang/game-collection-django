# Generated by Django 3.1.4 on 2020-12-10 00:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game_catalogue', '0003_auto_20201209_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='id',
        ),
        migrations.RemoveField(
            model_name='gamecollection',
            name='id',
        ),
        migrations.AddField(
            model_name='gamecollection',
            name='collection_id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique collection identifier Id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique game identifier Id', primary_key=True, serialize=False),
        ),
    ]
