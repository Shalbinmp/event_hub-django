# Generated by Django 3.2.23 on 2023-12-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(db_column='Booking_id', primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'booking',
                'managed': False,
            },
        ),
    ]
