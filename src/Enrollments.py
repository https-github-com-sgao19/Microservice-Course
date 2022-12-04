class Enrollments:

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
    def get_by_key(keys):
        sql = "SELECT * FROM courses.enrollments where call_number=%s and uni=%s"
        conn = Courses._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=keys)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_by_query(query):
        sql = query
        conn = Courses._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def update_by_key(keys, courses):
        conn = Courses._get_connection()
        cur = conn.cursor()
        content = []
        if "project_id" in courses:
            content.append("project_id = \"" + courses["project_id"] + "\"")
        sql = "UPDATE courses.enrollments SET " + ", ".join(content) + " WHERE call_number=%s and uni=%s"
        res = cur.execute(sql, args=keys)
        result = cur.fetchone()

        return result

    @staticmethod
    def insert_by_key(courses):
        conn = Courses._get_connection()
        print("connect")
        cur = conn.cursor()
        if "call_number" not in courses or "uni" not in courses:
            raise ValueError("call_number or uni")
        call_number = courses["call_number"] if "call_number" in courses else ""
        uni = courses["uni"] if "uni" in courses else ""
        project_id = courses["project_id"] if "project_id" in courses else ""
        sql = "INSERT INTO courses.enrollments (call_number, uni, project_id) " \
              "VALUES (%s, %s, %s)"
        cur.execute(sql, args=(call_number, uni, project_id))
        result = cur.fetchone()

        return result

    @staticmethod
    def delete_by_key(keys):
        conn = Courses._get_connection()
        cur = conn.cursor()
        sql = "DELETE FROM courses.enrollments WHERE call_number = %s and uni=%s"
        cur.execute(sql, args=keys)
        result = cur.fetchone()

        return result