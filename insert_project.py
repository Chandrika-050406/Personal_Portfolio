import sqlite3

conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

projects = [

(
"EDA Business Intelligence",
"Performed exploratory data analysis using Python and visualization libraries."
),

(
"Data Cleaning Project",
"Cleaned and transformed raw datasets using Excel and Python."
),

(
"Portfolio Website",
"Full-stack portfolio built with Flask and SQLite."
)

]

cursor.executemany(
"INSERT INTO projects(title,description) VALUES (?,?)",
projects
)

conn.commit()
conn.close()

print("Projects Added Successfully")