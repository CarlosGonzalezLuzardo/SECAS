from oic.utils.userinfo import UserInfo
import pyotp
import json
import bcrypt
import shelve
import os.path


# PASSWD = {
#     "diana": "krall",
#     "babs": "howes",
#     "upper": "crust"
# }

# TOTP_SECRETS = {
#     "diana": "base32secret3232",
#     "babs": "base32secret3233",
#     "upper": "base32secret3234"
# }

# questions = {
#     'diana': {
#         "question": 'have you lost your marbles',
#         'answer': 'yes'
#     },
#     'babs':{
#         "question": 'have you lost your marbles',
#         'answer': 'no'
#     },
#     'upper':{
#         "question": 'where did you lost your marbles',
#         'answer': 'miskatonic'
#     }
# }

FNAME = 'data.db'

class UserManager(UserInfo):
    # def __init__(self, db=None):
        # super(UserManager, self).__init__(db)
    def __init__(self,users_json_filepath):
        self.filepath = users_json_filepath
        with open(users_json_filepath, 'r') as users_json_file:
            users = json.load(users_json_file)
            super(UserManager, self).__init__(users)


    """
    CREATE
    R
    U
    D
    """

    def create_user(username,password,question,answer):
        random_secret = 0
        try:
            if not os.path.isfile(FNAME):
                PASSWD = {}
                with open(FNAME, 'w') as f:
                    json.dump(PASSWD, f)
                f.close()

            with open(FNAME,'r+') as f:
                PASSWD = json.load(f)
                if username not in PASSWD:
                    random_secret = pyotp.random_base32()
                    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                    hashedanswer = bcrypt.hashpw(answer.encode(), bcrypt.gensalt())

                    newdata = {'totp':random_secret,'pwd':hashed.decode(),'question':question,'answer':hashedanswer.decode()}
                    PASSWD[username] = newdata

                    f.seek(0)
                    f.truncate()
                    json.dump(PASSWD, f)
                else:
                    f.close()
                    raise RuntimeError("Username already in use")
            f.close()
        except RuntimeError:
            raise RuntimeError
        return random_secret




    """
    C
    READ
    U
    D
    """



    def _read_totp(username):
        """Read totp in database"""
        totp=0
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                TOTP_SECRETS = json.load(f)
                if username in TOTP_SECRETS:
                    totp = TOTP_SECRETS[username]['totp']
                else:
                    raise RuntimeError("Username not found")
            f.close()

            return totp
        else:
            raise RuntimeError("DB could not be found!")



    def _read_password(username):
        """Read password in database"""
        ret=0
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                DB = json.load(f)
                if username in DB:
                    ret = DB[username]['pwd'].encode()
                else:
                    raise RuntimeError("Username not found")
            f.close()

            return ret
        else:
            raise RuntimeError("DB could not be found!")



    def _read_lostqstn(username):
        """
            Password Recovery Function:
            Read recovery phrase
        """
        ret=0
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                DB = json.load(f)
                if username in DB:
                    ret = DB[username]['question']
                else:
                    raise RuntimeError("Username not found")
            f.close()

            return ret
        else:
            raise RuntimeError("DB could not be found!")



    def verify_lostpwd(username, password):
        """
            Password Recovery Function:
            Verify answer to recovery phrase
        """
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                DB = json.load(f)
                if username in DB:
                    ret = DB[username]['answer'].encode()
                    hashed = bcrypt.hashpw(password.encode(), ret)
                    if ret == hashed:
                        return True
                    else:
                        return False
                else:
                    raise RuntimeError("Username not found")
            f.close()

            return False
        else:
            raise RuntimeError("DB could not be found!")



    def verify_match(username, password):
        """Returns true if password is correct"""
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                DB = json.load(f)
                if username in DB:
                    ret = DB[username]['pwd'].encode()
                    hashed = bcrypt.hashpw(password.encode(), ret)
                    if ret == hashed:
                        return True
                    else:
                        return False
                else:
                    raise RuntimeError("Username not found")
            f.close()

            return False
        else:
            raise RuntimeError("DB could not be found!")
    """
    C
    R
    UPDATE
    D
    """

    def _update_password(username, password):
        """Change password in database"""
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                DB = json.load(f)
                if username in DB:
                    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                    DB[username]['pwd']=hashed.decode()
                    f.seek(0)
                    f.truncate()
                    json.dump(DB, f)
                else:
                    raise RuntimeError("Update failed: Username %s not found" % username)
            f.close()
            return username
        else:
            raise RuntimeError("DB could not be found!")

    def _reset_totp(username):
        """Reset totp in database"""
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                DB = json.load(f)
                if username in DB:
                    password=pyotp.random_base32()
                    DB[username]['totp']=password
                    f.seek(0)
                    f.truncate()
                    json.dump(DB, f)
                else:
                    raise RuntimeError("Username not found")
            f.close()
            return password
        else:
            raise RuntimeError("DB could not be found!")

    """
    C
    R
    U
    DELETE
    """

    def _delete_user(username):
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                DB = json.load(f)
                if username in DB:
                    print(DB[username])
                    del DB[username]
                    f.seek(0)
                    f.write(json.dumps(DB))
                    f.truncate()
                else:
                    raise RuntimeError("Username not found")
            f.close()
            return True
        else:
            raise RuntimeError("DB could not be found!")


    def verify_username(username):
        if os.path.isfile(FNAME):
            with open(FNAME, 'r+') as f:
                DB = json.load(f)
                if username in DB:
                    return True
                else:
                    return False
            f.close()
        else:
            raise RuntimeError("DB could not be found!")