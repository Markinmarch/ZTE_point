from flask import redirect
from flask_login import current_user

from flask_admin import AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView

from app.app_settings import dp
from DB.models import User, Item, Order, session


class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    def inaccessible_callback(self, name, **kwargs):
        return redirect('/')

class TaskModelViewUsers(ModelView):
    can_set_page_size = True
    page_size = 20
    column_list = ['name', 'email', 'phone']
    can_create = False
    can_edit = False
    can_delete = False
    
class TaskModelViewItems(ModelView):
    column_list = ['id', 'name', 'price', 'index', 'image']
    can_set_page_size = True
    page_size = 20
    column_display_all_relations = True
    column_display_all_relations = True
    column_hide_backrefs = False
    column_display_pk = True
    
class TaskModelViewOrders(ModelView):
    column_list = ['id', 'user', 'item']
    can_set_page_size = True
    page_size = 20
    column_display_all_relations = True
    column_hide_backrefs = False
    column_display_pk = True
    
admin = Admin(dp, name = 'ZTE point', template_mode = 'bootstrap3', index_view = CustomAdminIndexView())
    
admin.add_view(TaskModelViewUsers(User, session, name = 'Клиент'))
admin.add_view(TaskModelViewItems(Item, session, name = 'Товары'))
admin.add_view(TaskModelViewOrders(Order, session, name = 'Заказы'))