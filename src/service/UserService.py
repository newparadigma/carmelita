from service.DBService import DBService

class UserService:
    def __init__(self):
        self.dbService = DBService()

    def update_user_last_prediction_at(self, user_id):
        self.dbService.update_user_last_prediction_at(user_id)

    def save_new_user(self, user_id):
        self.dbService.save_new_user(user_id)
        
    def check_user_data(self, user_id):
        return self.dbService.check_user_data(user_id)