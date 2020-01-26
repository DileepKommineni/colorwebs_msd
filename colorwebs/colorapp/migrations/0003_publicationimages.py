# Generated by Django 3.0.2 on 2020-01-26 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colorapp', '0002_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_image', models.ImageField(default='default.jpg', upload_to='publication_images')),
                ('publication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colorapp.Publication')),
            ],
        ),
    ]
