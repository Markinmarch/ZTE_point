import os

from flask import redirect, url_for
from flask_login import current_user

from flask_admin.form import ImageUploadField
from flask_admin import AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView
# from flask_admin._compat import string_types
# from urllib.parse import urljoin
from markupsafe import Markup
# from flask_admin.helpers import get_url

# from wtforms.widgets import html_params

from app.app_settings import dp
from DB.models import User, Item, Order, session


file_path = os.path.abspath(os.path.dirname(__name__))

def name_gen_image(model, file_data):
    hash_name = f'{model}/{model.name}'
    return hash_name

class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    def inaccessible_callback(self, name, **kwargs):
        return redirect('/')

class TaskModelViewUsers(ModelView):
    column_labels = {
        'name': 'Имя',
        'email': 'Почта',
        'phone': 'Номер телефона'
    }
    can_set_page_size = True
    page_size = 20
    column_list = ['name', 'email', 'phone']
    can_create = False
    can_edit = False
    can_delete = False
    
class TaskModelViewItems(ModelView):
    column_labels = {
        'id': 'ID',
        'name': 'Наименование',
        'price': 'Цена',
        'index': 'Индекс',
        'image': 'Изображение'
    }
    column_list = ['id', 'name', 'price', 'index', 'image']
    can_set_page_size = True
    page_size = 20
    column_display_all_relations = True
    column_display_all_relations = True
    column_hide_backrefs = False
    column_display_pk = True

    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''
        url = url_for('static', filename=os.path.join('images/item_images/', model.image))
        if model.image.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup(f'<img src={url} width="100">')
        
    column_formatters = {'image': _list_thumbnail}
    
    form_extra_fields = {
        # ImageUploadField Выполняет проверку изображений, создание эскизов, обновление и удаление изображений.
        "image": ImageUploadField(
            '',
            # Абсолютный путь к каталогу, в котором будут храниться файлы
            base_path = os.path.join(file_path, 'static/images/item_images/'),
            # Относительный путь из каталога. Будет добавляться к имени загружаемого файла.
            url_relative_path='images/item_images/',
            namegen=name_gen_image,
            # Список разрешенных расширений. Если не указано, то будут разрешены форматы gif, jpg, jpeg, png и tiff.
            allowed_extensions=['jpg'],
            max_size=(1200, 780, True),
            thumbnail_size=(100, 100, True)
            )
        }
    
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
########################################################################
# import os

# from flask import url_for, Markup
# from flask_admin import form
# from flask_admin.contrib.sqla import ModelView
# from wtforms import validators

# 'C:\\Users\\mike\\pythonProject\\NAME_PROJECT'

# file_path = os.path.abspath(os.path.dirname(__name__))


# # Функция, которая будет генерировать имя файла из модели и загруженного файлового объекта.
# def name_gen_image(model, file_data):
#     hash_name = f'{model}/{model.username}'
#     return hash_name


# class UserView(ModelView):
#     column_display_pk = True
#     column_labels = {
#         'id': 'ID',
#         'username': 'Имя пользователя',
#         'last_seen': 'Последний вход',
#         'image_user': 'Аватар',
#         'posts': 'Посты',
#         'email': 'Емайл',
#         'password': 'Пароль',
#         'role': 'Роль',
#         'file': 'Выберите изображение'
#     }

#     # Список отображаемых колонок
#     column_list = ['id', 'role', 'username', 'email', 'password', 'last_seen', 'image_user']

#     column_default_sort = ('username', True)
#     column_sortable_list = ('id', 'role', 'username', 'email')

#     can_create = True
#     can_edit = True
#     can_delete = True
#     can_export = True
#     export_max_rows = 500
#     export_types = ['csv']

#     form_args = {
#         'username': dict(label='ЮЗЕР', validators=[validators.DataRequired()]),
#         'email': dict(label='МЫЛО', validators=[validators.Email()]),
#         'password': dict(label='ПАРОЛЬ', validators=[validators.DataRequired()]),
#     }

#     AVAILABLE_USER_TYPES = [
#         (u'Админ', u'Админ'),
#         (u'Автор', u'Автор'),
#         (u'Редактор', u'Редактор'),
#         (u'Пользователь', u'Пользователь'),
#     ]

#     form_choices = {
#         'role': AVAILABLE_USER_TYPES,
#     }

#     # Словарь, где ключ — это имя столбца, а значение — описание столбца представления списка или поля формы добавления/редактирования.
#     column_descriptions = dict(
#         username='First and Last name'
#     )

#     # исключенные колонки
#     column_exclude_list = ['password']

#     column_searchable_list = ['email', 'username']
#     column_filters = ['email', 'username']
#     column_editable_list = ['role', 'username', 'email']

#     create_modal = True
#     edit_modal = True

#     # Исключить колонку из создания, редактирования
#     form_excluded_columns = ['id']

#     def _list_thumbnail(view, context, model, name):
#         if not model.image_user:
#             return ''

#         url = url_for('static', filename=os.path.join('storage/user_img/', model.image_user))
#         if model.image_user.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
#             return Markup(f'<img src={url} width="100">')

#     # передаю функцию _list_thumbnail в поле image_user
#     column_formatters = {
#         'image_user': _list_thumbnail
#     }

#     form_extra_fields = {
#         # ImageUploadField Выполняет проверку изображений, создание эскизов, обновление и удаление изображений.
#         "image_user": form.ImageUploadField('',
#                                             # Абсолютный путь к каталогу, в котором будут храниться файлы
#                                             base_path=
#                                             os.path.join(file_path, 'blog/static/storage/user_img/'),
#                                             # Относительный путь из каталога. Будет добавляться к имени загружаемого файла.
#                                             url_relative_path='storage/user_img/',
#                                             namegen=name_gen_image,
#                                             # Список разрешенных расширений. Если не указано, то будут разрешены форматы gif, jpg, jpeg, png и tiff.
#                                             allowed_extensions=['jpg'],
#                                             max_size=(1200, 780, True),
#                                             thumbnail_size=(100, 100, True),

#                                             )}

#     def create_form(self, obj=None):
#         return super(UserView, self).create_form(obj)

#     def edit_form(self, obj=None):
#         return super(UserView, self).edit_form(obj)
