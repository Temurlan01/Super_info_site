# Generated by Django 5.0.7 on 2024-08-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_alter_categorys_title_alter_hashtag_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='Название'),
        ),
    ]
