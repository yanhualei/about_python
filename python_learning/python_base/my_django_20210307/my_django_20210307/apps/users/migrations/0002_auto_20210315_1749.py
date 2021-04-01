# Generated by Django 2.1.7 on 2021-03-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (0, 'famale')], default=1, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=50, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
