# Generated by Django 4.0.2 on 2022-02-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0004_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='un-categorized', max_length=255),
        ),
    ]
