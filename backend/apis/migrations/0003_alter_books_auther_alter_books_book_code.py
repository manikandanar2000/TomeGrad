# Generated by Django 4.0.5 on 2023-04-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_courses_course_offer_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='auther',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_code',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
