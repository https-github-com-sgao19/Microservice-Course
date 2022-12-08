import pymysql
from os import getenv

class Enrollments:

    def __init__(self):
        pass

    @staticmethod
    def _get_connection():
        conn = pymysql.connect(
            user="admin",
            password="12345678",
            host="course.ceqqavijgmdi.us-east-1.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(keys):
        sql = "SELECT * FROM courses.student_enrollments where call_number=%s and uni=%s"
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=(keys["call_number"], keys["uni"]))
        result = cur.fetchone()

        return result

    @staticmethod
    def update_by_key(keys, courses):
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        content = []
        if "project_id" in courses:
            content.append("project_id=\"" + courses["project_id"] + "\"")
        sql = "UPDATE courses.student_enrollments SET " + ", ".join(content) + " WHERE call_number=%s AND uni=%s"
        res = cur.execute(sql, args=(keys["call_number"], keys["uni"]))
        result = cur.fetchone()

        return result

    @staticmethod
    def insert_by_key(courses):
        conn = Enrollments._get_connection()
        print("connect")
        cur = conn.cursor()
        if "call_number" not in courses or "uni" not in courses:
            raise ValueError("call_number or uni")
        call_number = courses["call_number"] if "call_number" in courses else ""
        uni = courses["uni"] if "uni" in courses else ""
        project_id = courses["project_id"] if "project_id" in courses else ""
        sql = "INSERT INTO courses.student_enrollments (call_number, uni, project_id) " \
              "VALUES (%s, %s, %s)"
        print(call_number, uni, project_id)
        cur.execute(sql, args=(call_number, uni, project_id))

    @staticmethod
    def delete_by_key(keys):
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        sql = "DELETE FROM courses.student_enrollments WHERE call_number = %s and uni=%s"
        cur.execute(sql, args=keys)
        result = cur.fetchone()

        return result
    @staticmethod
    def get_by_template(self, limit=10, offset=0):
        sql = "SELECT * FROM courses.student_enrollments LIMIT %s OFFSET %s"
        cur = self.conn.cursor()
        cur.execute(sql, args=(limit, offset))
        return cur.fetchall()