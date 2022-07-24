# Generated by Django 4.0.6 on 2022-07-19 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crawler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_page', models.CharField(blank=True, max_length=1000, null=True)),
                ('url', models.JSONField(blank=True, null=True)),
                ('img', models.JSONField(blank=True, null=True)),
                ('count_url', models.IntegerField(blank=True, null=True)),
                ('count_img', models.IntegerField(blank=True, null=True)),
                ('time_crawl', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('crawler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link.crawler')),
            ],
        ),
    ]