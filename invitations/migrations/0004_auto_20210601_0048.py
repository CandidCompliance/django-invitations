class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0004_invitation_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='role',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
