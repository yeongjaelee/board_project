# Generated by Django 4.1.2 on 2022-11-25 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdetail',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='board.post'),
        ),
    ]
