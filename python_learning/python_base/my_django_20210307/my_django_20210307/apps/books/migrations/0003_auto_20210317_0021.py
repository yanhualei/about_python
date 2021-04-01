# Generated by Django 2.1.7 on 2021-03-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210316_1211'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bookinfo',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='b_id',
            field=models.IntegerField(default=1615911663, primary_key=True, serialize=False, verbose_name='图书编号'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='b_name',
            field=models.CharField(default='book_1615911663', max_length=30, unique=True, verbose_name='图书名'),
        ),
    ]