# Generated by Django 4.1 on 2022-09-12 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0003_cours_coef_alter_cours_doc_alter_cours_matiere_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='doc',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
    ]
