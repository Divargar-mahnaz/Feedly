# Generated by Django 3.2.4 on 2021-06-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Name')),
                ('link', models.URLField(verbose_name='Link')),
                ('image', models.ImageField(blank=True, null=True, upload_to='feed/', verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'db_table': 'feed',
            },
        ),
    ]
