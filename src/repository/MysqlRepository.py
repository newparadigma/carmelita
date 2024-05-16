import mysql.connector

class MysqlRepository:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="mysql",
            user="homestead",
            password="homestead",
            database="homestead"
        )

    def update_user_last_prediction_at(self, user_id):
        # UPDATEUSERQUERY="UPDATE users SET last_prediction_at = now() WHERE telegram_id = '%s';"
        # self.db.cursor().execute(UPDATEUSERQUERY, (user_id, ))
        # self.db.commit()
        cursor = self.db.cursor()
        query = "UPDATE users SET last_prediction_at = now() WHERE telegram_id = '%s';"
        cursor.execute(query, (user_id, ))
        self.db.commit()

    def save_new_user(self, user_id):
        # SAVEUSERQUERY="INSERT INTO users (telegram_id, last_prediction_at) VALUES (%s, now())"
        # self.db.cursor().execute(SAVEUSERQUERY, (user_id, ))
        # self.db.commit()
        cursor = self.db.cursor()
        query = "INSERT INTO users (telegram_id, last_prediction_at) VALUES (%s, now())"
        cursor.execute(query, (user_id, ))
        self.db.commit()

    def check_user_data(self, user_id):
        # CHECKDIFFQUERY="SELECT ((UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(users.last_prediction_at)) > 60 * 60 * 24) as diff FROM users WHERE telegram_id = %s"
        # self.db.cursor().execute(CHECKDIFFQUERY, (user_id, ))
        # result = self.db.cursor().fetchone()
        # self.db.commit()
        # return result
        cursor = self.db.cursor()
        query = "SELECT ((UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(users.last_prediction_at)) > 60 * 60 *24) as diff FROM users WHERE telegram_id = %s"
        cursor.execute(query, (user_id, ))
        result = cursor.fetchone()
        self.db.commit()
        return result
