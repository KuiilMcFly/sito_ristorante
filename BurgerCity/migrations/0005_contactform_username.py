# Generated by Django 4.2.6 on 2023-10-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerCity', '0004_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
