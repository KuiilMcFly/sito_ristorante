# Generated by Django 4.2.6 on 2023-10-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=20)),
                ('prezzo', models.FloatField()),
            ],
        ),
    ]
