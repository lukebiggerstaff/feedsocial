# Generated by Django 2.0.3 on 2018-03-13 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=140)),
                ('comment_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='usercontent',
            name='content',
            field=models.TextField(max_length=140),
        ),
        migrations.AddField(
            model_name='contentcomment',
            name='content_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.UserContent'),
        ),
    ]
