# Generated by Django 5.0.2 on 2024-03-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreport',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='commentreport',
            name='reason',
            field=models.CharField(choices=[('Inappropriate', 'Inappropriate Content'), ('Spam', 'Spam or Advertising'), ('Abusive', 'Abusive or Offensive'), ('Other', 'Other')], max_length=20),
        ),
    ]