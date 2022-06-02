# Generated by Django 4.0.4 on 2022-05-31 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Multiple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('response', models.CharField(max_length=30)),
                ('option_a', models.CharField(max_length=30)),
                ('option_b', models.CharField(max_length=30)),
                ('option_c', models.CharField(max_length=30)),
                ('option_d', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='True_False',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('response', models.BooleanField()),
            ],
        ),
    ]