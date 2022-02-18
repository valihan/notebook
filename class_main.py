import constant
import math
from db import cl_db


class cl_main:
    mv_debug = 0

    def switch_debug(self):
        if self.mv_debug == 0:
            self.mv_debug = 1
        else:
            self.mv_debug = 0
        return self.mv_debug

    def switch_debug9(self):
        if self.mv_debug == 0:
            self.mv_debug = 9
        else:
            self.mv_debug = 0
        return self.mv_debug

    def dprint(self, iv_output):
        if self.mv_debug > 0:
            print(iv_output)

    def dprint9(self, iv_output):
        if self.mv_debug == 9:
            print(iv_output)

    def __init__(self):
        self.mo_db = cl_db(constant.gc_db_name)

    def check_user(self, is_message):
        # Проверить, есть ли такой пользователь. Если нет - добавить
        if(not self.mo_db.user_exists(is_message.from_user.id)):
            mo_db.add_user(is_message)

    def start(self, is_message):
        self.check_user(is_message)
        return constant.gc_msg_welcome

    def main(self, is_message):
        # Проверить, есть ли такой пользователь.
        self.check_user(is_message)
        lv_response = ""
        self.dprint("main" + is_message.from_user.first_name + is_message.text )
        try:
            lv_response = self.mo_db.add_record(is_message.from_user.id, is_message.text, is_message.date)
            return constant.gc_msg_added
        except:
            print("response=",lv_response)
            return constant.gc_msg_error

    def history(self, is_message):
        lv_response = ""
        cmd_variants = ('/history', '/h', '!history', '!h')
        lv_cmd = is_message.text
        for lv_var in cmd_variants:
            lv_cmd = lv_cmd.replace(lv_var, '').strip()
        lv_within = 'day'
        if(len(lv_cmd)):
            for k in constant.within_als:
                for als in constant.within_als[k]:
                    if(als == lv_cmd):
                        lv_within = k
        self.dprint("within=", lv_within)
        self.log(is_message, lv_within)

    def log(self, is_message, iv_within):
        print(iv_within)
        lt_records = self.mo_db.get_records(is_message.from_user.id, iv_within)
        if(len(lt_records)):
            lv_response = constant.gc_msg_report + " {constant.within_als[iv_within][-1]}\n\n"
            for lv_record in lt_records:
                lv_response += f"{lv_record[1]}"
                lv_response += f" ({lv_record[2]})\n"
            return lv_response
        else:
            return constant.gc_msg_records_not_found

    def log_day(self, is_message):
        return self.log(is_message, 'day')
    def log_week(self, is_message):
        return self.log(is_message, 'week')
    def log_month(self, is_message):
        return self.log(is_message, 'month')
    def log_year(self, is_message):
        return self.log(is_message, 'year')
