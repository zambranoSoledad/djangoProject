""" In order to run this script you have to write the comand :
    python manage.py shell, then in the prompt write:
    import ecomerce.groups
    press enter, an this script will create two new groups and test them
"""

from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from comerce.models import Productos, Ventas

costumer_group, created = Group.objects.get_or_create(name="Costumer")
admin_group, created = Group.objects.get_or_create(name="Admin")

content_type = ContentType.objects.get_for_model(Productos)
product_permission = Permission.objects.filter(content_type=content_type)
print([perm.codename for perm in product_permission])
# ['add_productos', 'change_productos', 'delete_productos', 'view_productos']

content2_type = ContentType.objects.get_for_model(Ventas)
sell_permission = Permission.objects.filter(content_type=content2_type)
print([perm.codename for perm in sell_permission])
# ['add_ventas', 'change_ventas', 'delete_ventas', 'view_ventas']

for perm in product_permission:
    if perm.codename in ["change_productos", "view_productos"]:
        costumer_group.permissions.add(perm)
    admin_group.permissions.add(perm)
for perm in sell_permission:
    if perm.codename in ["change_ventas", "add_ventas", "view_ventas"]:
        costumer_group.permissions.add(perm)
    admin_group.permissions.add(perm)

user = User.objects.get(username="sole")
user.groups.add(costumer_group)  # Add the user to the costumer group
print(user.get_group_permissions())

user = get_object_or_404(User, pk=user.id)

print(user.has_perm("comerce.delete_productos"))
print(user.has_perm("comerce.view_productos"))
print(user.has_perm("comerce.change_productos"))
print(user.has_perm("comerce.add_productos"))
