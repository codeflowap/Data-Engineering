# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id text, start_time time, user_id int, 
                            level text, song_id text, artist_id text, session_id int, location text, user_agent text);
                            """)

user_table_create = (""" CREATE TABLE IF NOT EXISTS user (user_id int, first_name text, last_name text, gender text, level 
                        text); """)

song_table_create = (""" CREATE TABLE IF NOT EXISTS song (song_id text, title text, artist_id text, year int, duration float8);
                        """)

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artist (artist_id text, name text, location txt, latitude float8, longitude float8);
                        """)

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time time, hour int, day int, week int, month int, year int, weekday int);
                    """)

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]