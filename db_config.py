import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='33URuumGzezvR7h.root',
        password='rIvGvLjjJuNqbH6L',
        database='student_task_manager1',
        port = 4000
    )

    return connection

# def get_database_connection():
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='aditya2112',
#         database='student_task_manager1'
#     )

#     return connection