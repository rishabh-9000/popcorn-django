# Generated by Django 2.1.7 on 2019-04-01 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0003_auto_20190331_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(default='../media/images/no_image.png', upload_to='media/images/actors'),
        ),
    ]
