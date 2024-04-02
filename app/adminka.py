from flask import redirect, render_template

from flask_login import current_user

from flask_admin import BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from app.app_settings import admin #, staff
from DB.models import User, Item, session


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


admin.add_view(TaskModelViewUsers(User, session, name = 'Клиент'))
admin.add_view(TaskModelViewItems(Item, session, name = 'Товары'))
