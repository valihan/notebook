import sqlite3

class cl_db:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def user_exists(self, iv_user_id ):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (iv_user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, iv_user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (iv_user_id,))
        return result.fetchone()[0]

    def add_user(self, is_message):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`,`first_name`, `last_name`, `username`, `language_code`, `chat_id`) VALUES (?,?,?,?,?,?)",
           (is_message.from_user.id, is_message.from_user.first_name, is_message.from_user.last_name, is_message.from_user.username, is_message.from_user.language_code, is_message.chat.id))
        return self.conn.commit()
        
    def add_record(self, iv_user, iv_value, iv_date):
        """ Добавляем запись в бд """
        # print("add_record", iv_user, iv_value, iv_date)
        # lv_sql="INSERT INTO log (user_id,value, date) VALUES (" +str(iv_user) +",'"+iv_value+"',datetime("+str(iv_date)+", 'unixepoch'))"        
        lv_sql = "INSERT INTO log (user_id,value) VALUES (" +str(iv_user) +",'"+iv_value+"')"
        # print(lv_sql)
        self.cursor.execute(lv_sql)
        return self.conn.commit()

    def get_records(self, user_id, within = "all"):
        """Получаем историю о доходах/расходах"""
        lv_sql="SELECT user_id, value, date FROM `log`"
        if(within == "day"):
            result = self.cursor.execute(lv_sql+" WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime') ORDER BY `date`",
                (user_id,))
        elif(within == "week"):
            result = self.cursor.execute(lv_sql+" WHERE `user_id` = ? AND `date` BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `date`",
                (user_id,))
        elif(within == "month"):
            result = self.cursor.execute(lv_sql+" WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date`",
                (user_id,))
        elif(within == "year"):
            result = self.cursor.execute(lv_sql+" WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of year') AND datetime('now', 'localtime') ORDER BY `date`",
                (user_id,))
        else:
            result = self.cursor.execute(lv_sql+" WHERE `user_id` = ? ORDER BY `date`",
                (user_id,))        
        return result.fetchall()
    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()