# Generated by Django 5.1.3 on 2024-12-01 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryroom',
            name='img5',
            field=models.ImageField(default='info2_ThWrinm.jpeg', upload_to='', verbose_name='Изображение 5'),
            preserve_default=False,
        ),
    ]
