# DROP TABLES

songplay_table_drop = "DROP TABLE songplays"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE times"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id text, start_time time, user_id int, 
                            level text, song_id text, artist_id text, session_id int, location text, user_agent text);
                            """)

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (user_id int, first_name text, last_name text, gender text, level 
                        text); """)

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (song_id text, title text, artist_id text, year int, duration float8);
                        """)

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (artist_id text, name text, location text, latitude float8, longitude float8);
                        """)

time_table_create = (""" CREATE TABLE IF NOT EXISTS times (start_time time, hour int, day int, week int, month int, year int, weekday int);
                    """)

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

song_table_insert = (""" INSERT INTO songs (song_id, title, artist_id, year, duration) 
                        VALUES (%s, %s, %s, %s, %s) """)

time_table_insert = (""" INSERT INTO times (start_time, hour, day, week, month, year, weekday)
                        VALUES (%s, %s, %s, %s, %s, %s, %s) """)

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s) """)