import sqlite3
import os

os.remove("example.db")
con = sqlite3.connect("example.db")
cur = con.cursor()

# TASK 2A
print("Creating of tables intiated")
cur.execute("""""")

cur.execute("""""")

cur.execute("""""")

cur.execute("""""")

cur.execute("""""")

cur.execute("""""")

cur.execute("""CREATE TABLE "Довідник рецептів для замовника" (
			"ID"	INTEGER,
			"ID Рецепту"	INTEGER NOT NULL,
			FOREIGN KEY("ID Рецепту") REFERENCES "Рецепт приготування ліків"("ID"),
			PRIMARY KEY("ID" AUTOINCREMENT)
			);""")

cur.execute("""CREATE TABLE "Замовлення" (
			"ID"	INTEGER,
			"ПІБ Лікаря"	TEXT,
			"ПІБ Пацієнта"	TEXT NOT NULL,
			"Вік"	INTEGER NOT NULL,
			"Діагноз"	TEXT,
			"ID Повного рецепту"	INTEGER NOT NULL,
			"Час видачі замовлення"	TEXT NOT NULL,
			PRIMARY KEY("ID" AUTOINCREMENT)
			);""")

cur.execute("""CREATE TABLE "Виконані замовлення" (
			"ID Замовлення"	INTEGER,
			FOREIGN KEY("ID Замовлення") REFERENCES "Замовлення"("ID"),
			PRIMARY KEY("ID Замовлення")
			);""")
con.commit()
input("Creation is done!\n###############")

# TASK 2B
print("Database editing is initiated")
cur.execute("""ALTER TABLE "Parent"
			   ADD "E-mail" TEXT NOT NULL;""")

cur.execute("""ALTER TABLE "Parent"
			   DROP COLUMN "Date of birth";""")

cur.execute("""INSERT INTO "Parent" ("Full name", "Phone number", "Adress", "E-mail", "Kid")
			   VALUES ("Peter Parker", 1234567890, "Cool.st 100, apt. 200", "regularman@mail.com", "No one?");""")

cur.execute("""INSERT INTO "Student" ("Class ID", "First Name", "Last Name", "Gender", "Date of birth")
			   VALUES (1, "Alex", "Anderson", "Male", "1.1.2009");""")

cur.execute("""UPDATE "Parent"
			   SET "E-mail" = "spiderman@mail.com"
			   WHERE "Full name" = "Peter Parker";""")
con.commit()
input("Editing is done!\n###############")

# TASK 2C
print("Deletition initiated")
cur.execute("DROP TABLE School;")
cur.execute("DELETE FROM Parent WHERE ID = 1;")
con.commit()
input("Deletition is done!\n###############")

# TASK 2D
print("Sadly, SQLite doesn't support the ADD CONSTRAINT variant of the ALTER TABLE command")

ALTER TABLE Orders
ADD CONSTRAINT Название
FOREIGN KEY (Куда) REFERENCES Persons(Откуда)
ON DELETE CASCADE;

con.close()