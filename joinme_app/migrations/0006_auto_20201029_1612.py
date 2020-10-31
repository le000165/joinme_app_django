# Generated by Django 3.1.2 on 2020-10-29 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joinme_app', '0005_auto_20201029_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cmt_user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmt_users', to='joinme_app.user'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='joinme_app.activity'),
        ),
    ]
