# Generated by Django 2.1.7 on 2019-03-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0002_actor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(default='../static/images/no_image.png', upload_to='static/images/actors'),
        ),
    ]
