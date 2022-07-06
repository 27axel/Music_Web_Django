# Generated by Django 4.0.2 on 2022-04-10 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Название трека')),
                ('bpm', models.IntegerField(verbose_name='Темп')),
                ('image', models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Изображение')),
                ('audio', models.FileField(upload_to='music/%Y/%m/%d/', verbose_name='Аудио')),
            ],
        ),
        migrations.CreateModel(
            name='DrumKit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Название')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Файл')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Название жанра')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Название тарифа')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Tonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=45, verbose_name='Тональность')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCost', models.IntegerField(blank=True, verbose_name='Итоговая цена')),
                ('anketa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.anketa')),
            ],
        ),
        migrations.AddField(
            model_name='anketa',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.genre'),
        ),
        migrations.AddField(
            model_name='anketa',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.price'),
        ),
        migrations.AddField(
            model_name='anketa',
            name='tonal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.tonal'),
        ),
        migrations.AddField(
            model_name='anketa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]