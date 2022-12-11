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
    def get_by_params(params):
        conn = Projects._get_connection()
        cur = conn.cursor()
        where_args = []
        if len(params) == 0:
            sql = "SELECT * FROM courses.student_projects"
        else:
            where_condition = []
            for k, v in params.items():
                where_condition.append(k + "=%s")
                where_args.append(v)
            sql = "SELECT * FROM courses.student_projects WHERE " + " AND ".join(where_condition)

        cur.execute(sql, args=where_args)
        result = cur.fetchall()
        return result

    @staticmethod
    def get_by_course(call_number):
        sql = "SELECT * FROM courses.student_projects WHERE courses.student_projects.call_number = %s"
        conn = Projects._get_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (call_number,))
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
        res = cur.execute(sql, args=project_number)
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