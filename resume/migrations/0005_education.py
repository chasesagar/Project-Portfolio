# Generated by Django 3.0.3 on 2020-02-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='pictures')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
    ]
