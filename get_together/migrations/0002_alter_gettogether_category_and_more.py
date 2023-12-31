# Generated by Django 4.2.7 on 2023-11-24 00:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):
    dependencies = [
        ("get_together", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gettogether",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="get_together.category",
            ),
        ),
        migrations.AlterField(
            model_name="gettogether",
            name="description",
            field=djrichtextfield.models.RichTextField(
                blank=True, max_length=500, null=True
            ),
        ),
        migrations.AlterField(
            model_name="gettogether",
            name="image",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                default=django.utils.timezone.now,
                force_format="WEBP",
                keep_meta=True,
                quality=75,
                scale=None,
                size=[100, 200],
                upload_to="profiles/",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="gettogether",
            name="image_alt",
            field=models.CharField(
                blank=True, default="event_image", max_length=100, null=True
            ),
        ),
    ]
