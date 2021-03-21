class UserData:
    def __init__(self, user_id):
        self.user_id = user_id
        self.status_id = 0
        self.current_vin = ""
        self.current_zn = ""

    def set_user_status(self, status_id):
        self.status_id = status_id
