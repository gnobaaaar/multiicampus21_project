# Generated by Django 3.0 on 2022-02-03 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0003_remove_memo_articleid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='memoContent',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='memo',
            name='memoTitle',
            field=models.CharField(default='', max_length=250, null=True),
        ),
    ]
