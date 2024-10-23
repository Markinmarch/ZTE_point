import os

from flask import redirect, url_for
from flask_login import current_user

from flask_admin.form import ImageUploadField
from flask_admin import AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import BaseSQLAFilter
from flask_admin.menu import MenuLink

from markupsafe import Markup

from app.app_settings import dp
from DB.models import User, Item, Order, Bascket, session

class MyCustomFilter(BaseSQLAFilter):
    def apply(self, query, value):
        return query.filter(self.column == value)

    def operation(self):
        return 'equals'

file_path = os.path.abspath(os.path.dirname(__name__))

def name_gen_image(model, file_data):
    hash_name = f'{model.name}_{model.index}/{model.name}'
    return hash_name

class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    def inaccessible_callback(self, name, **kwargs):
        return redirect('/')

class TaskModelViewUsers(ModelView):
    column_list = [
        'id',
        'name',
        'email',
        'phone'
    ]
    column_labels = {
        'id': 'ID клиента',
        'name': 'Имя',
        'email': 'Почта',
        'phone': 'Номер телефона'
    }
    can_set_page_size = True
    page_size = 20
    can_create = False
    can_edit = False
    can_delete = False
    
class TaskModelViewItems(ModelView):
    column_list = [
        'id',
        'name',
        'price',
        'unit',
        'index',
        'parametrs',
        'description',
        'image'
    ]
    column_labels = {
        'id': 'ID',
        'name': 'Наименование',
        'price': 'Цена',
        'unit': 'Единица измерения',
        'index': 'Индекс',
        'parametrs': 'Основные параметры',
        'description': 'Краткое описание',
        'image': 'Изображение',
    }
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
            url_relative_path = 'images/item_images/',
            namegen = name_gen_image,
            # Список разрешенных расширений. Если не указано, то будут разрешены форматы gif, jpg, jpeg, png и tiff.
            allowed_extensions=['jpg'],
            max_size = (1200, 780, True),
            thumbnail_size = (200, 200, True)
            )
        }
    
class TaskModelViewBascket(ModelView):
    column_list = [
        'id',
        'date',
        'id_user',
        'id_item',
        'count',
        'paid_status'
    ]
    column_labels = {
        'id': 'ID',
        'date': 'Дата',
        'id_user': 'ID клиента',
        'id_item': 'ID товара',
        'count': 'Количество',
        'paid_status': 'Статус'
    }
    can_set_page_size = True
    page_size = 20
    column_display_all_relations = True
    column_hide_backrefs = False
    column_display_pk = True
    
class TaskModelViewOrders(ModelView):
    column_list = [
        'id',
        'id_user',
        'date',
        'link_to_list_items'
    ]
    column_labels = {
        'id': 'ID',
        'date': 'Дата',
        'id_user': 'ID клиента',
        'link_to_list_items': 'Ссылка на список товаров клиента'
    }
    column_filters = [
        MyCustomFilter(column = Order.id_user, name = 'ID клиента')
    ]
    
    @staticmethod
    def _order_formatters(view, context, model, name):
        return Markup("<a href ='%s'>%s</a>" % (model.link_to_list_items, 'Ссылка'))
    
    column_formatters = {
        'link_to_list_items': _order_formatters
    }
    
    can_set_page_size = True
    page_size = 20
    column_display_all_relations = True
    column_hide_backrefs = False
    column_display_pk = True
    
class MainPageLink(MenuLink):
    def get_url(self):
        return url_for('home')


admin = Admin(dp, name = 'ZTE point', template_mode = 'bootstrap3', index_view = CustomAdminIndexView())
    
admin.add_view(TaskModelViewUsers(User, session, name = 'Клиент'))
admin.add_view(TaskModelViewItems(Item, session, name = 'Товары'))
admin.add_view(TaskModelViewBascket(Bascket, session, name = 'Корзина'))
admin.add_view(TaskModelViewOrders(Order, session, name = 'Заказы'))
admin.add_link(MainPageLink(name = 'На главную'))
########################################################################
