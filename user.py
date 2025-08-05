id = 1  # User's ID
email = "example@example.abc"  # User's Email
password = "12345"  # User's Password
products_id = [1, 2, 3, 4, 5]  # User's Products

class User:
    def __init__(self, userid, useremail, userpassword, userproducts_id):
        self.userid = userid
        self.useremail = useremail
        self.userpassword = userpassword
        self.userproducts_id = userproducts_id
    
    def user_identify(self):
        print(f"UserId: {self.userid}, UserEmail: {self.useremail}, UserPassword: {'*' * len(self.userpassword)}, UserProductsIDs: {self.userproducts_id}")

user = User(id, email, password, products_id)
user.user_identify()