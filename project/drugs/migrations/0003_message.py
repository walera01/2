# Generated by Django 4.0.3 on 2022-05-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0002_drugs_prise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
