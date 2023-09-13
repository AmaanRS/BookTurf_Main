# Generated by Django 4.1.10 on 2023-08-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookTurfMain', '0007_remove_turf_profile_turf_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turf_profile',
            name='turf_category',
        ),
        migrations.AddField(
            model_name='turf_profile',
            name='turf_category_1',
            field=models.ManyToManyField(blank=True, choices=[('option1', 'Football'), ('option2', 'Parking'), ('option3', '12+ players'), ('option3', '8+ players')], to='BookTurfMain.turf_profile'),
        ),
        migrations.AddField(
            model_name='turf_profile',
            name='turf_category_2',
            field=models.ManyToManyField(blank=True, choices=[('option1', 'Football'), ('option2', 'Parking'), ('option3', '12+ players'), ('option3', '8+ players')], to='BookTurfMain.turf_profile'),
        ),
        migrations.AddField(
            model_name='turf_profile',
            name='turf_category_3',
            field=models.ManyToManyField(blank=True, choices=[('option1', 'Football'), ('option2', 'Parking'), ('option3', '12+ players'), ('option3', '8+ players')], to='BookTurfMain.turf_profile'),
        ),
        migrations.AddField(
            model_name='turf_profile',
            name='turf_category_4',
            field=models.ManyToManyField(blank=True, choices=[('option1', 'Football'), ('option2', 'Parking'), ('option3', '12+ players'), ('option3', '8+ players')], to='BookTurfMain.turf_profile'),
        ),
    ]
