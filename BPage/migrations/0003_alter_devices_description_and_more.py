# Generated by Django 4.1.5 on 2023-02-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPage', '0002_remove_question_content_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Qdescription',
            field=models.TextField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('modelname', 'Question')},
        ),
    ]
