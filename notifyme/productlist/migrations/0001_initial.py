# Generated by Django 2.2.7 on 2019-11-19 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('userid', models.IntegerField()),
                ('url', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
