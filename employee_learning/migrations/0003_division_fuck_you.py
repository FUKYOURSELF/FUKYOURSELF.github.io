# Generated by Django 5.1.2 on 2024-11-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee_learning", "0002_division"),
    ]

    operations = [
        migrations.AddField(
            model_name="division",
            name="fuck_you",
            field=models.BooleanField(
                default=False, help_text="If you want to get fucked,please click this"
            ),
            preserve_default=False,
        ),
    ]
