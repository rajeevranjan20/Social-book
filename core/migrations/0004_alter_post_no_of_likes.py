# Generated by Django 5.0.4 on 2024-06-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_likepost_alter_profile_id_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
