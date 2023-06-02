# Generated by Django 4.2 on 2023-06-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Имя пользователя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('phone', models.CharField(max_length=155, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'купить курс',
                'verbose_name_plural': 'купить курсы',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.CharField(max_length=255, verbose_name='Название курса')),
                ('foto_course', models.ImageField(upload_to='product/', verbose_name='Фотография продукта')),
                ('price', models.BigIntegerField(verbose_name='Цена курса')),
                ('desc_course', models.TextField(max_length=255, verbose_name='Описание продукта')),
                ('less', models.BigIntegerField(verbose_name='Количество занятий')),
                ('students', models.BigIntegerField(verbose_name='Количество студентов')),
            ],
            options={
                'verbose_name': 'Наши курсы',
                'verbose_name_plural': 'Наши курсы',
            },
        ),
    ]
