# Generated by Django 2.0.2 on 2018-02-27 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bTitle', models.CharField(max_length=20)),
                ('bPubDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hName', models.CharField(max_length=20)),
                ('hGender', models.BooleanField()),
                ('hContent', models.CharField(max_length=50)),
                ('bBook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookApp.BookInfo')),
            ],
        ),
    ]