# Generated by Django 3.2 on 2021-05-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('edf', models.FileField(upload_to='edfs/')),
            ],
        ),
    ]
