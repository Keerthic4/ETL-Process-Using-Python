import sqlite3 
import pandas as pd

connection = sqlite3.connect("C:\\recommendation.sqlite")

get_course_rating = pd.read_sql_query("SELECT course_id, rating from ratings", connection)

recommendPandas = (get_course_rating.groupby(['course_id'],).mean())
recommendPandasSorted = recommendPandas.sort_values(by=['rating', 'course_id'], ascending=[False,False])
print(recommendPandasSorted)

recommendPandasSorted.to_sql("recommendPandas", connection, if_exists="replace")
connection.close()