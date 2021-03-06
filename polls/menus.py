from menu import Menu, MenuItem
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

# Add two items to our main menu
Menu.add_item("main", MenuItem("Tools",
                               reverse("polls.views.menus_polls"),
                               weight=10,
                               icon="tools"))

Menu.add_item("main", MenuItem("Reports",
                               reverse("polls.views.contact"),
                               weight=20,
                               icon="report"))


# Define children for the my account menu
myaccount_children = (
    MenuItem("Edit Profile",
             reverse("polls.views.contact"),
             weight=10,
             icon="user"),
    MenuItem("Admin",
             reverse("admin:index"),
             weight=80,
             separator=True,
             check=lambda request: request.user.is_superuser),
    MenuItem("Logout",
             reverse("accounts.views.logout"),
             weight=90,
             separator=True,
             icon="user"),
)

# Add a My Account item to our user menu
Menu.add_item("user", MenuItem("My Account",
                               reverse("accounts.views.myaccount"),
                               weight=10,
                               children=myaccount_children))