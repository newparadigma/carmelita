import mysql.connector

class repository.MysqlRepository:
  def __init__(self):
    self.db = mysql.connector.connect(
        host="mysql",
        user="homestead",
        password="homestead",
        database="homestead"
    )

    def update_user_last_prediction_at(self, user_id):
        query = "UPDATE users SET last_prediction_at = now() WHERE telegram_id = '%s';"
        self.db.cursor.execute(query, (user_id, ))
        self.db.commit()

    def save_new_user(self, user_id):
        query = "INSERT INTO users (telegram_id, last_prediction_at) VALUES (%s, now())"
        self.db.cursor.execute(query, (user_id, ))
        self.db.commit()

    # отдает ответ на вопрос "прошло ли 24 часа с момента последнего предсказания для пользователя если он был"
    def get_diff(self, user_id):
        query = "SELECT ((UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(users.last_prediction_at)) > 60 * 60 *24) as diff FROM users WHERE telegram_id = %s LIMIT 1"
        self.db.cursor.execute(query, (user_id, ))
        result = self.db.cursor.fetchone()
        db.commit()
        return result