from functools import wraps
import time
import sqlite3
from datetime import datetime


def performanceRecorder(func):
    wraps(func)

    def wrapper(*args, **kwargs):
        funcName = func.__name__
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError as error:
            raise error

        finally:
            stop_time = time.time()
            execTime = stop_time - start_time
            data = datetime.now().isoformat()
            with sqlite3.connect("database.db") as connection:
                cursor = connection.cursor()
                cursor.execute("""INSERT INTO performance (
                            func_name,
                            exec_time,
                            date
                        )
                        VALUES (
                            ?,
                            ?,
                            ?
                            
                        );
""", [funcName, execTime, data])

    return wrapper
