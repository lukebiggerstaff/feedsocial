# Generated by Django 2.0.3 on 2018-03-13 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20180313_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercontent',
            options={'ordering': ['last_updated']},
        ),
        migrations.AddField(
            model_name='contentcomment',
            name='creation_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercontent',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercontent',
            name='num_comments',
            field=models.IntegerField(default=0),
        ),
    ]