# Generated by Django 3.1.5 on 2021-01-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210130_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='first_head',
            field=models.CharField(blank=True, default='Заголовок 1', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='first_text_1',
            field=models.CharField(blank=True, default='Текст первого заголовка', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='first_text_2',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='first_text_3',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(blank=True, default='Название продукта', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='second_head',
            field=models.CharField(blank=True, default='Заголовок 2', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='second_text_1',
            field=models.CharField(blank=True, default='Текст второго заголовка', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='second_text_2',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='second_text_3',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='third_head',
            field=models.CharField(blank=True, default='Заголовок 3', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='third_text_1',
            field=models.CharField(blank=True, default='Текст третьего заголовка', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='third_text_2',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='third_text_3',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
