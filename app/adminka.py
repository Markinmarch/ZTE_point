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


# client_table = admin.add_view(TaskModelViewUsers(User, session, name = 'Клиент'))
# items_table = admin.add_view(TaskModelViewItems(Item, session, name = 'Товары'))

class AdminView(ModelView):
    @expose('/')
    def index(self):
        if User.get_user(current_user.get_id).role =='admin':
            admin.add_view(TaskModelViewUsers(User, session, name = 'Клиент'))
            admin.add_view(TaskModelViewItems(Item, session, name = 'Товары'))
        
        # if User.get_user(current_user.get_id).role == 'user':
        #     return redirect(f'/?user={current_user.get_id}')
        # if User.get_user(current_user.get_id).role =='staff':
        #     items_table
        # if User.get_user(current_user.get_id).role =='admin':
        #     items_table
        #     client_table
        # if current_user.is_anonymous:
        #     return redirect('/hui')
            
# admin.add_view(AdminView(name='My View', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))
