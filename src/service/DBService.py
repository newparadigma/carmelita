
class service.DBService:
  def __init__(self):
    self.dbService = repository.mysql()

    def update_user_last_prediction_at(self, user_id):
        self.dbService.update_user_last_prediction_at(user_id)

    def save_new_user(self, user_id):
        self.dbService.save_new_user(user_id)
