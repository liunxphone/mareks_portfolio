# Generated by Django 3.1.4 on 2021-04-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_finances', '0002_auto_20210411_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='date',
        ),
        migrations.AddField(
            model_name='balance',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='date',
            field=models.DateField(),
        ),
    ]
