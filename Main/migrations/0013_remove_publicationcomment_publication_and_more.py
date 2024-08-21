# Generated by Django 5.0.7 on 2024-08-16 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_alter_hashtag_title_alter_publication_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationcomment',
            name='Publication',
        ),
        migrations.AddField(
            model_name='publicationcomment',
            name='Publication_Detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.publication_detail'),
        ),
    ]
