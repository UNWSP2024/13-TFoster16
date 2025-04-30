#Timothy Foster, 4/29/25, Cities Database Program

#Import the sqlite module.
import sqlite3

def main():

    #Establish a connection for the database.
    connection = sqlite3.connect("citiesforprogram2.db")

    #Create the cursor object.
    cursor = connection.cursor()

    #Create the database and its values.
    cursor.execute("create table cities (number integer, name text, population integer)")

    #Create a list with the values for the cities.
    cities = [(1, 'Tokyo', 38001000),
                (2, 'Delhi', 25703168),
                (3, 'Shanghai', 23740778),
                (4, 'Sao Paulo', 21066245),
                (5, 'Mumbai', 21042538),
                (6, 'Mexico City', 20998543),
                (7, 'Beijing', 20383994),
                (8, 'Osaka', 20237645),
                (9, 'Cairo', 18771769),
                (10, 'New York', 18593220),
                (11, 'Dhaka', 17598228),
                (12, 'Karachi', 16617644),
                (13, 'Buenos Aires', 15180176),
                (14, 'Kolkata', 14864919),
                (15, 'Istanbul', 14163989),
                (16, 'Chongqing', 13331579),
                (17, 'Lagos', 13122829),
                (18, 'Manila', 12946263),
                (19, 'Rio de Janeiro', 12902306),
                (20, 'Guangzhou', 12458130)]

    #Insert the values from the cities list and insert them into the cities database.
    cursor.executemany("insert into cities values (?, ?, ?)", cities)

    #Print each row of the cities database using a for loop.
    for row in cursor.execute("select * from cities"):
        print(row)

    #Close the connection.
    connection.close()

if __name__ == "__main__":
    main()
