# Generated by Django 2.1.7 on 2019-04-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0004_auto_20190402_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='image',
            field=models.ImageField(default='images/no_image.png', upload_to='images/producers/'),
        ),
    ]
