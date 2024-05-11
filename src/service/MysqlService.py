import repository.MysqlRepository as repository

class service.MysqlService:
  def __init__(self):
    self.repository = repository.mysql()

    def update_user_last_prediction_at(self, user_id):
        self.repository.update_user_last_prediction_at(user_id)

    def save_new_user(self, user_id):
        self.repository.save_new_user(user_id)

    # отдает ответ на вопрос "прошло ли 24 часа с момента последнего предсказания для пользователя если он был"
    # def get_diff(self, user_id):
    #     # cursor = db.cursor()
    #     # query = "SELECT ((UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(users.last_prediction_at)) > 60 * 60 *24) as diff FROM users WHERE telegram_id = %s"
    #     # cursor.execute(query, (user_id, ))
    #     # result = cursor.fetchone()
    #     # db.commit()
    #     # return result