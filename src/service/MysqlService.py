from repository.MysqlRepository import MysqlRepository as repository

class MysqlService:
    def __init__(self):
        self.repository = repository()

    def update_user_last_prediction_at(self, user_id):
        self.repository.update_user_last_prediction_at(user_id)

    def save_new_user(self, user_id):
        self.repository.save_new_user(user_id)

    def check_user_data(self, user_id):
        result = self.repository.check_user_data(user_id)

        if result is None:
            return 'user_not_found'
        else:
            if result[0] == 0:
                return 'not_allowed_to_predict'
            else:
                return 'allowed_to_predict'