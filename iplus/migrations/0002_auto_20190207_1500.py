# Generated by Django 2.1.5 on 2019-02-07 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iplus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='bank',
        ),
        migrations.AddField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='iplus.Bank'),
            preserve_default=False,
        ),
    ]
