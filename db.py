from config import host, db_name, user, password
import psycopg2



def bot_id(id, fn, ln):
    try:
        # connect to exists database
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        connection.autocommit = True

            # the cursor for perfoming database operations
            # cursor = connection.cursor()

        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT user_bot_id 
                               FROM chat_bot.users 
                               WHERE user_bot_id = '{id}'"""
                           )

            if cursor.fetchone() == None:
                cursor.execute(f"""INSERT INTO chat_bot.users(first_name, last_name, user_bot_id) 
                                  VALUES('{fn}', '{ln}', '{id}')""")




    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')