# Generated by Django 2.1 on 2020-02-23 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_racks_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racks',
            name='student',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.students'),
        ),
    ]
