# Generated by Django 3.1.5 on 2021-03-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210215_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='developer',
            name='data',
            field=models.JSONField(),
        ),
    ]