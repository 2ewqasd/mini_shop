# Generated by Django 3.1.5 on 2021-01-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210130_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterField(
            model_name='extra_text',
            name='text',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
