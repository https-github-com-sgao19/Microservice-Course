import pymysql
from os import getenv


class Projects:

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
    def get_by_key(key):
        sql = "SELECT * FROM courses.student_projects where project_id=%s"
        conn = Projects._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_by_param(param):
        where_clause, where_params = [], []
        if "project_id" in param:
            where_clause.append("project_id=%s")
            where_params.append(param["project_id"])
        if "call_number" in param:
            where_clause.append("call_number=%s")
            where_params.append(param["call_number"])
        if "project_name" in param:
            where_clause.append("project_name=%s")
            where_params.append(param["project_name"])
        if "group_name" in param:
            where_clause.append("group_name=%s")
            where_params.append(param["group_name"])
        if "description" in param:
            where_clause.append("description=%s")
            where_params.append(param["description"])
        if not where_clause:
            sql = "SELECT * FROM courses.student_projects"
        else:
            sql = "SELECT * FROM courses.student_projects WHERE " + ' AND '.join(where_clause)
        conn = Projects._get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, where_params)
                result = cur.fetchall()
                return result

    @staticmethod
    def update_by_key(project_number, courses):
        conn = Projects._get_connection()
        cur = conn.cursor()
        content = []
        if "project_name" in courses:
            content.append("project_name = \"" + courses["project_name"] + "\"")
        if "group_name" in courses:
            content.append("group_name = \"" + courses["group_name"] + "\"")
        if "group_member" in courses:
            content.append("group_member = \"" + courses["group_member"] + "\"")
        if "description" in courses:
            content.append("description = \"" + courses["description"] + "\"")
        sql = "UPDATE courses.student_projects SET " + ", ".join(content) + " WHERE project_id = %s"
        cur.execute(sql, args=project_number)
        result = cur.fetchone()
        return result

    @staticmethod
    def insert_by_key(courses):
        conn = Projects._get_connection()
        print("connect")
        cur = conn.cursor()
        if "project_id" not in courses:
            raise ValueError("project_id")
        project_id = courses["project_id"] if "project_id" in courses else ""
        project_name = courses["project_name"] if "project_name" in courses else ""
        group_name = courses["group_name"] if "group_name" in courses else ""
        description = courses["description"] if "description" in courses else ""
        call_number = courses["call_number"] if "call_number" in courses else ""
        sql = "INSERT INTO courses.student_projects (project_id, project_name, group_name, description,call_number) " \
              "VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, args=(project_id, project_name, group_name, description, call_number))

    @staticmethod
    def delete_by_key(project_id):
        conn = Projects._get_connection()
        cur = conn.cursor()
        sql = "DELETE FROM courses.student_projects WHERE project_id = %s"
        cur.execute(sql, args=project_id)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_by_template(self, limit=10, offset=0):
        sql = "SELECT * FROM courses.student_projects LIMIT %s OFFSET %s"
        cur = self.conn.cursor()
        cur.execute(sql, args=(limit, offset))
        return cur.fetchall()
