# Generated by Django 4.1.5 on 2023-02-15 04:28

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import network.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_pic', models.ImageField(default='static/std.jpg', upload_to='posts/')),
                ('bio', models.TextField(blank=True, max_length=160, null=True)),
                ('cover', models.ImageField(default='card2.webp', upload_to='posts')),
                ('friends', models.ManyToManyField(blank=True, related_name='frnd', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='intrest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrest_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('payment_mode', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out For Shipping', 'Out For Shipping'), ('Completed', 'Completed')], default='Pending', max_length=150)),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, null=True)),
                ('pagename', models.CharField(max_length=255, null=True)),
                ('website', models.CharField(max_length=255, null=True)),
                ('category', models.CharField(max_length=255, null=True)),
                ('emial', models.CharField(max_length=255, null=True)),
                ('cover', models.ImageField(default='card2.webp', upload_to='posts')),
                ('image', models.ImageField(blank=True, upload_to='posts/')),
                ('creater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('content_text', models.TextField(blank=True, max_length=140)),
                ('status', models.CharField(max_length=255, null=True)),
                ('doc', models.FileField(blank=True, default=True, upload_to='posts/')),
                ('vedio', models.FileField(blank=True, default=True, upload_to='posts/', validators=[network.validators.file_size])),
                ('Product_Price', models.IntegerField(blank=True, default=True, null=True)),
                ('content_image', models.FileField(blank=True, default=True, upload_to='posts/', validators=[network.validators.file_size])),
                ('comment_count', models.IntegerField(default=0)),
                ('posts_type', models.CharField(max_length=255, null=True)),
                ('slug', models.CharField(default=True, max_length=130)),
                ('views', models.IntegerField(default=True)),
                ('title', models.CharField(default=True, max_length=255)),
                ('categories', models.CharField(default=True, max_length=255)),
                ('tages_n', models.CharField(default=True, max_length=255)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('likers', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('page_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.page')),
                ('savers', models.ManyToManyField(blank=True, related_name='saved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='postz', to='network.post')),
                ('usr', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='whs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=12)),
                ('House', models.CharField(max_length=255)),
                ('Area', models.CharField(max_length=60)),
                ('Landmark', models.CharField(max_length=60)),
                ('Town', models.CharField(max_length=60)),
                ('State', models.CharField(max_length=60)),
                ('Zip', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='posts/')),
                ('Title', models.CharField(max_length=255, null=True)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('creater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=150)),
                ('Product_Image', models.ImageField(null=True, upload_to='posts')),
                ('Product_Description', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('Product_Price', models.IntegerField()),
                ('creater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='pageposts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('content_text', models.TextField(blank=True, max_length=140)),
                ('content_image', models.ImageField(blank=True, upload_to='posts/')),
                ('comment_count', models.IntegerField(default=0)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pageposts', to=settings.AUTH_USER_MODEL)),
                ('likers', models.ManyToManyField(blank=True, related_name='pagelikes', to=settings.AUTH_USER_MODEL)),
                ('savers', models.ManyToManyField(blank=True, related_name='pagesaved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quanty', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.shipping_address'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='invited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fr_pages', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='pagez', to='network.page')),
                ('fr_user', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='frinvit', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='toinvit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='invite_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.TextField(blank=True, max_length=255)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_inv', to=settings.AUTH_USER_MODEL)),
                ('pages', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pagz', to='network.page')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_inv', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='intrest_followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_user', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='intr', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='top', to='network.intrest')),
            ],
        ),
        migrations.CreateModel(
            name='friend_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.TextField(blank=True, max_length=255)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fr', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='freq', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='toreq', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='commentz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=255)),
                ('fr_user', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='comm', to=settings.AUTH_USER_MODEL)),
                ('user_post', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='pos', to='network.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(max_length=90)),
                ('comment_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenters', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='network.post')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
