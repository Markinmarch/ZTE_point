from flask_admin.contrib.sqla import ModelView

from app.app_settings import admin
from DB.models import User, Item, session


admin.add_view(ModelView(User, session))
admin.add_view(ModelView(Item, session))