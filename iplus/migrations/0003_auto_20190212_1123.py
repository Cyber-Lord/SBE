# Generated by Django 2.1.5 on 2019-02-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplus', '0002_auto_20190207_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post', models.TextField()),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Others',
            },
        ),
        migrations.AlterModelOptions(
            name='loancritereia',
            options={'verbose_name_plural': 'criterias'},
        ),
    ]