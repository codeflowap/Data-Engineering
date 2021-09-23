songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songtable (artist text, firstName text, gender text,
                            itemInSession text, lastName text, length text, level text, location text,sessionId text,
                            song text, userId text);
                            """)

songtable_table_drop = "DROP TABLE songtable"

create_table_queries = [songplay_table_create]
drop_table_queries = [songtable_table_drop]

songtable_table_insert = """ INSERT INTO songtable (artist, firstName, gender, itemInSession, lastName, length, level,
                                location, sessionId, song, userId) 
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """