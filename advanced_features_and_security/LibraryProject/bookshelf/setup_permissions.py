from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Article
# Get content type
article_ct = ContentType.objects.get_for_model(Article)

# Define permissions
permissions = {
    "can_view": Permission.objects.get(codename="can_view", content_type=article_ct),
    "can_create": Permission.objects.get(codename="can_create", content_type=article_ct),
    "can_edit": Permission.objects.get(codename="can_edit", content_type=article_ct),
    "can_delete": Permission.objects.get(codename="can_delete", content_type=article_ct),
}

# Create and assign permissions to groups
groups = {
    "Viewers": ["can_view"],
    "Editors": ["can_view", "can_create", "can_edit"],
    "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
}

for group_name, perms in groups.items():
    group, _ = Group.objects.get_or_create(name=group_name)
    group.permissions.set([permissions[perm] for perm in perms])
    group.save()