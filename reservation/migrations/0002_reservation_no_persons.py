# Generated by Django 4.2.5 on 2023-09-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="no_persons",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
