# Generated by Django 3.2.4 on 2021-07-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20210702_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
