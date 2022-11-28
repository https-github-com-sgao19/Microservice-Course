import pymysql
from os import getenv


# user = "admin"
# password = "12345678"
# host = "course.ceqqavijgmdi.us-east-1.rds.amazonaws.com"

class Courses:

    def __init__(self):
        pass

    @staticmethod
    def _get_connection():
        conn = pymysql.connect(
            user=getenv("USER"),
            password=getenv("PWD"),
            host=getenv("HOST"),
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):
        sql = "SELECT * FROM courses.courses where call_number=%s";
        conn = Courses._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def update_by_key(call_number, courses):
        conn = Courses._get_connection()
        cur = conn.cursor()
        content = []
        if "class_title" in courses:
            content.append("class_title = \"" + courses["class_title"] + "\"")
        if "instructor" in courses:
            content.append("instructor = \"" + courses["instructor"] + "\"")
        if "day" in courses:
            content.append("day = \"" + courses["day"] + "\"")
        if "time_Location" in courses:
            content.append("time_Location = \"" + courses["time_Location"] + "\"")
        #sql = "UPDATE f22_databases.columbia_students SET " + ", ".join(content) + " WHERE guid = \"" + uni + "\""
        #print(sql)
        sql = "UPDATE courses.courses SET " + ", ".join(content) + " WHERE call_number = %s"
        res = cur.execute(sql, args=call_number)
        result = cur.fetchone()

        return result

    @staticmethod
    def insert_by_key(courses):
        conn = Courses._get_connection()
        print("connect")
        cur = conn.cursor()
        if "call_number" not in courses:
            raise ValueError("call_number")
        call_number = courses["call_number"] if "call_number" in courses else ""
        class_title = courses["class_title"] if "class_title" in courses else ""
        instructor = courses["instructor"] if "instructor" in courses else ""
        day = courses["day"] if "day" in courses else ""
        time_Location = courses["time_Location"] if "time_Location" in courses else ""
        sql = "INSERT INTO courses.courses (call_number, class_title, instructor, day, time_Location) " \
              "VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, args=(call_number, class_title, instructor, day, time_Location))
        result = cur.fetchone()

        return result

    @staticmethod
    def delete_by_key(call_number):
        conn = Courses._get_connection()
        cur = conn.cursor()
        sql = "DELETE FROM courses.courses WHERE call_number = %s"
        cur.execute(sql, args=call_number)
        return