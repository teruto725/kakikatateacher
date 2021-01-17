# Generated by Django 3.1.5 on 2021-01-16 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0006_auto_20210116_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='img_exp',
        ),
        migrations.RemoveField(
            model_name='score',
            name='img_sq',
        ),
        migrations.RemoveField(
            model_name='scoredetail',
            name='label',
        ),
        migrations.RemoveField(
            model_name='scoredetail',
            name='scoredetail',
        ),
        migrations.AddField(
            model_name='score',
            name='score_p1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='score_p2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='score_p3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='scoredetail',
            name='phase',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scoredetail',
            name='result',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
