# Generated by Django 3.0.1 on 2020-01-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('article', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
    ]
