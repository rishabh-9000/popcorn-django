# Generated by Django 2.1.7 on 2019-03-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='image',
            field=models.ImageField(default='../static/images/no_image.png', upload_to='static/images/producers'),
        ),
    ]
