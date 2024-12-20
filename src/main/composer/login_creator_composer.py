from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_creator_controller import LoginCreatorController
from src.views.login_creator_view import LoginCreatorView

def login_creator_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = LoginCreatorController(model)
    view = LoginCreatorView(controller)

    return view