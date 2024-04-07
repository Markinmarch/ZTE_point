from flask import redirect, render_template, g, url_for, request

from flask_login import current_user

from flask_admin import AdminIndexView, Admin, expose
from flask_admin.contrib.sqla import ModelView

from app.app_settings import dp
from DB.models import User, Item, session


class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    
#     # def inaccessible_callback(self, name, **kwargs):
#     #     return redirect(url_for('login', next=request.url))

class TaskModelViewUsers(ModelView):
    can_set_page_size = True
    page_size = 20
    column_list = ['name', 'email', 'phone']
    create_modal = False
    edit_modal = False
    
class TaskModelViewItems(ModelView):
    can_set_page_size = True
    page_size = 20
    column_display_all_relations = True
    
admin = Admin(dp, name = 'ZTE point', template_mode = 'bootstrap3', index_view = CustomAdminIndexView())
    
admin.add_view(TaskModelViewUsers(User, session, name = 'Клиент'))
admin.add_view(TaskModelViewItems(Item, session, name = 'Товары'))