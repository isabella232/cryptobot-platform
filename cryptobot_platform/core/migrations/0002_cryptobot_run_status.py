# Generated by Django 4.1.1 on 2022-09-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cryptobot",
            name="run_status",
            field=models.CharField(default="STOPPED", max_length=50),
            preserve_default=False,
        ),
    ]
