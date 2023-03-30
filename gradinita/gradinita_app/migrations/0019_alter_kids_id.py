# Generated by Django 4.1.5 on 2023-03-29 19:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("gradinita_app", "0018_alter_profile_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kids",
            name="id",
            field=models.BigIntegerField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
