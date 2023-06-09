# Generated by Django 4.1.5 on 2023-03-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gradinita_app", "0019_alter_kids_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="absente_elev",
            name="id",
            field=models.BigAutoField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="kids",
            name="id",
            field=models.BigAutoField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="motivari_elev",
            name="id",
            field=models.BigAutoField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.BigAutoField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
