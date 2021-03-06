# Generated by Django 4.0.2 on 2022-03-10 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0009_remove_complains_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_feedback', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer')),
            ],
        ),
    ]
