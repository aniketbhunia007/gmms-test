# Generated by Django 2.0.3 on 2018-03-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                ("member_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("mobile_number", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=300)),
                ("registration_date", models.DateField()),
                ("start_date", models.DateField()),
                ("registration_upto", models.DateField()),
                (
                    "subscription_type",
                    models.CharField(
                        choices=[
                            ("gym", "Gym"),
                            ("cross_fit", "Cross Fit"),
                            ("gym_and_cross_fit", "Gym + Cross Fit"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "subscription_period",
                    models.CharField(
                        choices=[
                            ("1", "1 Month"),
                            ("3", "3 Months"),
                            ("6", "6 Months"),
                            ("12", "12 Months"),
                        ],
                        max_length=30,
                    ),
                ),
                ("amount", models.IntegerField()),
            ],
        ),
    ]
