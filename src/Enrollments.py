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
        if not ("call_number" in keys and "uni" in keys):
            raise ValueError
        sql = "SELECT * FROM courses.student_enrollments where call_number=%s and uni=%s"
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=(keys["call_number"], keys["uni"]))
        result = cur.fetchone()

        return result

    @staticmethod
    def update_by_key(param, body):
        if not ("call_number" in param and "uni" in param):
            raise ValueError
        content = []
        if "project_id" in body:
            content.append("project_id=\"" + body["project_id"] + "\"")
        sql = "UPDATE courses.student_enrollments SET " + ", ".join(content) + " WHERE call_number=%s AND uni=%s"
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=(param["call_number"], param["uni"]))
        result = cur.fetchone()

        return result

    @staticmethod
    def insert_by_key(courses):
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        if "call_number" not in courses or "uni" not in courses:
            raise ValueError("call_number or uni")
        call_number = courses["call_number"] if "call_number" in courses else ""
        uni = courses["uni"] if "uni" in courses else ""
        project_id = courses["project_id"] if "project_id" in courses else ""
        sql = "INSERT INTO courses.student_enrollments (call_number, uni, project_id) " \
              "VALUES (%s, %s, %s)"
        cur.execute(sql, args=(call_number, uni, project_id))
        return

    @staticmethod
    def delete_by_param(param):
        if "call_number" in param and "uni" in param:
            keys = (param["call_number"], param["uni"])
        else:
            raise ValueError
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        sql = "DELETE FROM courses.student_enrollments WHERE call_number = %s and uni=%s"
        cur.execute(sql, args=keys)
        return

    @staticmethod
    def get_by_param(param):
        where_clause, where_params = [], []
        if "uni" in param:
            where_clause.append("uni=%s")
            where_params.append(param["uni"])
        if "project_id" in param:
            where_clause.append("project_id=%s")
            where_params.append(param["project_id"])
        if "call_number" in param:
            where_clause.append("call_number=%s")
            where_params.append(param["call_number"])
        if not where_clause:
            sql = "SELECT * FROM courses.student_enrollments"
        else:
            sql = "SELECT * FROM courses.student_enrollments WHERE " + ' AND '.join(where_clause)
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=where_params)
        return cur.fetchall()

    @staticmethod
    def join_s(uni):
        conn = Enrollments._get_connection()
        cur = conn.cursor()
        sql = "SELECT * FROM courses.student_enrollments se JOIN courses.student_sections ss on se.call_number = ss.call_number WHERE uni = %s"
        cur.execute(sql, uni)
        result = cur.fetchall()
        return result
