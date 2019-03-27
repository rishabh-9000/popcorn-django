# Generated by Django 2.1.7 on 2019-03-27 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('yearOfRelease', models.CharField(max_length=4)),
                ('plot', models.TextField()),
                ('poster', models.ImageField(upload_to='')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producer.Producer')),
            ],
        ),
    ]