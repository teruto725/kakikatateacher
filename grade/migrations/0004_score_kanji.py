# Generated by Django 3.1.5 on 2021-01-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0003_auto_20210111_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='kanji',
            field=models.CharField(default='d', max_length=1),
            preserve_default=False,
        ),
    ]
