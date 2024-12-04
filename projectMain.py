import sqlite3

# establish connection to SQLite database
conn = sqlite3.connect('pawsome_pets.db')

# instantiate cursor object for query execution
cursor = conn.cursor()

print("============================================================================================")
print("CSC 423 - Pawsome Pets Database Project")
print("Authors: Jade Tustin, Daniel Guthart\n")
print("This Python script creates the database, populates it, shows the tables, and demonstrates a few transactions.")
print("It is designed to be run in one go, by itself.")
print("If you run into issues, try deleting pawsome_pets.db and then try running the script again. Thank you!")
print("============================================================================================")

# *****************************************************************************
# part A: create all necessary relations in the database, if they do not exist
# *****************************************************************************
# the created relations shall adhere to the schema and constraints 
# identified in part 2 of the documentation.
# *****************************************************************************

# create Clinic relation
query = """
    CREATE TABLE IF NOT EXISTS Clinic (
        clinicNo INTEGER PRIMARY KEY
            CHECK(clinicNo BETWEEN 00000 AND 99999),
        name TEXT NOT NULL UNIQUE,
        street TEXT NOT NULL,
        buildingInfo TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL 
            CHECK(LENGTH(state) = 2),
        ZIPcode TEXT NOT NULL 
            CHECK(LENGTH(ZIPcode) = 5),
        telephone TEXT NOT NULL UNIQUE 
            CHECK(LENGTH(telephone) = 10),
        staffNo INTEGER,
        FOREIGN KEY (staffNo) 
            REFERENCES Staff (staffNo) 
            ON DELETE SET DEFAULT
        );
        """
cursor.execute(query)
conn.commit()

# create Staff relation
query = """
    CREATE TABLE IF NOT EXISTS Staff (
        staffNo INTEGER PRIMARY KEY 
            CHECK(staffNo BETWEEN 0100000 AND 9999999),
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        street TEXT,
        buildingInfo TEXT,
        city TEXT,
        state TEXT 
            CHECK(LENGTH(state) = 2),
        ZIPcode TEXT 
            CHECK(LENGTH(ZIPcode) = 5),
        telephone TEXT UNIQUE NOT NULL 
            CHECK(LENGTH(telephone) = 10),
        DOB DATE,
        position TEXT NOT NULL,
        salary REAL NOT NULL 
            CHECK(salary > 0),
        clinicNo INTEGER,
        FOREIGN KEY (clinicNo) 
            REFERENCES Clinic (clinicNo) 
            ON DELETE SET DEFAULT
        );
        """
cursor.execute(query)
conn.commit()

# create Owner relation
query = """
    CREATE TABLE IF NOT EXISTS Owner (
        ownerNo INTEGER PRIMARY KEY 
            CHECK(ownerNo BETWEEN 440000000 AND 999999999),
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        street TEXT NOT NULL,
        buildingInfo TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL 
            CHECK(LENGTH(state) = 2),
        ZIPcode TEXT NOT NULL 
            CHECK(LENGTH(ZIPcode) = 5),
        telephone TEXT UNIQUE NOT NULL 
            CHECK(LENGTH(telephone) = 10)
        );
        """
cursor.execute(query)
conn.commit()

# create Pet relation
query = """
    CREATE TABLE IF NOT EXISTS Pet (
        petNo INTEGER PRIMARY KEY 
            CHECK(petNo BETWEEN 1000000000 AND 6599999999),
        petName TEXT NOT NULL,
        DOB DATE,
        species TEXT NOT NULL,
        breed TEXT,
        color TEXT,
        ownerNo INTEGER NOT NULL,
        clinicNo INTEGER NOT NULL,
        FOREIGN KEY (ownerNo) 
            REFERENCES Owner (ownerNo) 
            ON DELETE CASCADE,
        FOREIGN KEY (clinicNo) 
            REFERENCES Clinic (clinicNo)
            ON DELETE CASCADE
        );
        """
cursor.execute(query)
conn.commit()

# create Examination relation
query = """
    CREATE TABLE IF NOT EXISTS Examination (
        examNo INTEGER PRIMARY KEY 
            CHECK(examNo BETWEEN 00000000000 AND 99999999999),
        chiefComplaint TEXT NOT NULL,
        description TEXT NOT NULL,
        dateSeen DATE NOT NULL,
        actionsTaken TEXT NOT NULL,
        petNo INTEGER NOT NULL,
        staffNo INTEGER NOT NULL,
        FOREIGN KEY (petNo) 
            REFERENCES Pet (petNo) 
            ON DELETE CASCADE,
        FOREIGN KEY (staffNo) 
            REFERENCES Staff (staffNo) 
            ON DELETE SET NULL
        );
        """
cursor.execute(query)
conn.commit()
print("All tables were created successfully; no errors occurred.")
print("============================================================================================")


# *****************************************************************************
# part B: create at least 5 tuples for each relation in the database.
# *****************************************************************************

# tuples for Clinic
query = """
    INSERT INTO Clinic 
        (clinicNo, name, 
            street, buildingInfo, city, state, ZIPcode,
            telephone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (10001, "University Clinic",
        "123 Corniche Ave", "Suite 101",
        "Miami", "FL", "33101",
        "3051234567"),
    (10002, "Miami Beach Pet Clinic", 
        "23 Ocean Dr", "Suite 201", 
        "Miami Beach", "FL", "33139", 
        "3059876543"),
    (10003, "Miller Vet", 
        "234 Miller Dr", "Suite 300", 
        "Coral Gables", "FL", "33146",
        "3052345678"),
    (10004, "Pet Clinic", 
        "5000 San Amaro Dr", "Suite 100",
        "Miami", "FL", "33125",
        "3058765432"),
    (10005, "Miami Vet", 
        "1527 Albenga Ave", "Suite 1", 
        "Miami", "FL", "33010",
        "3056543210"),
    ])
conn.commit()

print("Clinic relation successfully populated.")
print("Showing contents of Clinic...\n")
query = "SELECT * FROM Clinic;"
cursor.execute(query)
contents = cursor.fetchall()
print("CLINIC NUMBER / NAME / STREET / BUILDING INFO / CITY / STATE / ZIP / TELEPHONE / MANAGER NUMBER")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")

# tuples for Staff
query = """
    INSERT INTO Staff 
        (staffNo, firstName, lastName, 
            street, buildingInfo, city, state, ZIPcode, 
            telephone, DOB, position, salary, clinicNo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (1000001, "John", "Doe",
        "123 Biscayne Blvd", "Building 1",
        "Miami", "FL", "33131",
        "3055551234", "1985-06-15", "Veterinarian", 75000, 10001),
    (1000002, "Jane", "Allen", 
        "456 Brickell Ave", "Suite 2A",
        "Miami", "FL", "33129",
        "3055555678", "1990-02-25", "Assistant", 45000, 10002),
    (1000003, "Alex", "Smith", 
        "789 Flagler St", "Unit 3B", 
        "Miami", "FL", "33130", 
        "3055551212", "1988-09-10", "Technician", 40000, 10003),
    (1000004, "Emil", "Lee", 
        "101 Coral Way", "Apt 4C", 
        "Miami", "FL", "33145", 
        "3055551313", "1995-12-20", "Receptionist", 35000, 10004),
    (1000005, "Sally", "Jones",
        "202 Little Havana Blvd", "Floor 5", 
        "Miami", "FL", "33135", 
        "3055551414", "1980-04-30", "Veterinarian", 80000, 10005),
    ])
conn.commit()

print("Staff relation successfully populated.")
print("Showing contents of Staff...\n")
query = "SELECT * FROM Staff;"
cursor.execute(query)
contents = cursor.fetchall()
print("STAFF NUMBER / FIRST NAME / LAST NAME / STREET / BUILDING INFO / CITY / STATE / ZIP / TELEPHONE / DOB / POSITION / SALARY / CLINIC NUMBER")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")

# tuples for Owner
query = """
    INSERT INTO Owner 
        (ownerNo, firstName, lastName, 
            street, buildingInfo, city, state, ZIPcode,
            telephone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (440000001, "Jeremy", "Brown", 
        "789 Ponce De Leon", "Apt 2", 
        "Miami", "FL", "33133",
        "7863334444"),
    (440000002, "Bob", "White",
        "456 Animal St", "House", 
        "Miami", "FL", "33132", 
        "7865556666"),
    (440000003, "Stephen", "Green",
        "123 Palm Rd", "Apt 3", 
        "Miami", "FL", "33156",
        "7867778888"),
    (440000004, "Daisy", "Blue", 
        "456 Juniper Cv", "Unit 5", 
        "Miami", "FL", "33176", 
        "7869990000"),
    (440000005, "Andrew", "Red", 
        "789 Cedar Ct", "House", 
        "Miami", "FL", "33186", 
        "7861122233"),
    ])
conn.commit()

print("Owner relation successfully populated.")
print("Showing contents of Owner...\n")
query = "SELECT * FROM Owner;"
cursor.execute(query)
contents = cursor.fetchall()
print("OWNER NUMBER / FIRST NAME / LAST NAME / STREET / BUILDINGINFO / CITY / STATE / ZIP / TELEPHONE")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")

# tuples for Pet
query = """ 
    INSERT INTO Pet 
        (petNo, petName, 
            DOB, species, breed, color,
            ownerNo, clinicNo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (1000000001, "Bo", 
        "2020-05-01", "Cat", "Persian", "White",
        440000001, 10001),
    (1000000002, "Ruby",
        "2018-09-12", "Dog", "Golden Retriever", "Golden", 
        440000002, 10002),
    (1000000003, "Max", 
        "2019-06-15", "Dog", "Beagle", "Tricolor", 
        440000003, 10003),
    (1000000004, "Bella", 
        "2021-07-21", "Cat", "Siamese", "Brown", 
        440000004, 10004),
    (1000000005, "Duke", 
        "2017-11-11", "Dog", "Labrador", "Fawn", 
        440000005, 10005),
    ])
conn.commit()

print("Pet relation successfully populated.")
print("Showing contents of Pet...\n")
query = "SELECT * FROM Pet;"
cursor.execute(query)
contents = cursor.fetchall()
print("PET NUMBER / NAME / DOB / SPECIES / BREED / COLOR / OWNER NUMBER / CLINIC NUMBER")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")

# tuples for Examination
query = """
    INSERT INTO Examination 
        (examNo, chiefComplaint, 
            description, dateSeen, actionsTaken,
            petNo, staffNo)
    VALUES (?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (10000000001, "Fever", 
        "Physical exam", "2024-01-01", "Prescribed meds", 
        1000000001, 1000001),
    (10000000002, "Checkup", 
        "Routine exam", "2024-01-15", "All clear", 
        1000000002, 1000002),
    (10000000003, "Coughing",
        "Chest X-ray", "2024-02-01", "Prescribed meds",
        1000000003, 1000003),
    (10000000004, "Vomiting",
        "Stomach exam", "2024-02-10", "Dietary advice", 
        1000000004, 1000004),
    (10000000005, "Limping",
        "Leg X-ray", "2024-02-15", "Bandage applied",
        1000000005, 1000005),
    ])
conn.commit()

print("Examination relation successfully populated.")
print("Showing contents of Examination...\n")
query = "SELECT * FROM Examination;"
cursor.execute(query)
contents = cursor.fetchall()
print("EXAM NUMBER / CHIEF COMPLAINT / DESCRIPTION / DATE SEEN / ACTIONS TAKEN / PET NUMBER / STAFF NUMBER")
for row in contents:
    print(row)
print("============================================================================================")
print("All relations successfully populated with the provided tuples.")
print("============================================================================================")


# *****************************************************************************
# part C: develop 5 SQL queries using embedded SQL
# *****************************************************************************
# these queries shall correspond to the transactions specified
# in part 2 of the documentation. 
# *****************************************************************************

# register a new owner and their pet
print("Transaction 1: Register a new owner and their pet.\n")
query = """
    INSERT INTO Owner 
        (ownerNo, firstName, lastName, 
            street, buildingInfo, city, state, ZIPcode,
            telephone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
cursor.execute(query, 
        (440000006, "Emma", "Black", 
            "400 Old Town Rd", "House", 
            "Miami", "FL", "33146", 
            "3053339999"))

query = """
    INSERT INTO Pet 
        (petNo, petName, 
            DOB, species, breed, color, 
            ownerNo, clinicNo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
cursor.execute(query, 
        (1000000006, "Rosie", 
            "2020-12-12", "Dog", "Labrador", "White", 
            440000006, 10001))
conn.commit()

print("After transaction 1... (showing contents of Owner)\n")

query = "SELECT * FROM Owner;"
cursor.execute(query)
postregistration = cursor.fetchall()

print("OWNER NUMBER / FIRST NAME / LAST NAME / STREET / BUILDINGINFO / CITY / STATE / ZIP / TELEPHONE")
for row in postregistration:
    print(row)
print()

print("After transaction 1... (showing contents of Pet)\n")

query = "SELECT * FROM Pet;"
cursor.execute(query)
postregistration = cursor.fetchall()

print("PET NUMBER / NAME / DOB SPECIES / BREED / COLOR / OWNER NUMBER / CLINIC NUMBER")
for row in postregistration:
    print(row)
print("--------------------------------------------------------------------------------------------")

# assign a staff member to manage a clinic
print("Transaction 2: Assign a staff member to manage a clinic.\n")
query = """
    UPDATE Clinic
    SET staffNo = ?
        WHERE clinicNo = ?
        """
cursor.execute(query, (1000001, 10001))

print("After transaction 2... (showing contents of Clinic)\n")
query = "SELECT * FROM Clinic;"
cursor.execute(query)
postassignment = cursor.fetchall()
print("CLINIC NUMBER / NAME / STREET / BUILDING INFO / CITY / STATE / ZIP / TELEPHONE / MANAGER NUMBER")
for row in postassignment:
    print(row)
conn.commit()
print("--------------------------------------------------------------------------------------------")

# log a pet’s examination
print("Transaction 3: Log a pet's examination.\n")
query = """
    INSERT INTO Examination 
        (examNo, chiefComplaint,
            description, dateSeen, actionsTaken,
            petNo, staffNo)
    VALUES (?, ?, ?, ?, ?, ?, ?)
        """
cursor.execute(query, 
        (10000000006, "Stomach Infection",
            "Ear cleaning", "2024-03-01", "Prescribed antibiotics",
            1000000006, 1000001))

print("After transaction 2... (showing contents of Examination)\n")
query = "SELECT * FROM Examination;"
cursor.execute(query)
examinations = cursor.fetchall()
print("EXAM NUMBER / CHIEF COMPLAINT / DESCRIPTION / DATE SEEN / ACTIONS TAKEN / PET NUMBER / STAFF NUMBER")
for row in examinations:
    print(row)
conn.commit()
print("--------------------------------------------------------------------------------------------")

# retrieve all examinations for a specific pet
print("Transaction 4: Retrieve all examinations for a specific pet. (petID = 1000000001)\n")
pet_id = 1000000001
query = """ 
    SELECT * FROM Examination
        WHERE petNo = ?
        """
cursor.execute(query, (pet_id,))
examinations = cursor.fetchall()
print("After query... (showing results obtained from transaction on Examination)\n")
print("EXAM NUMBER / CHIEF COMPLAINT / DESCRIPTION / DATE SEEN / ACTIONS TAKEN / PET NUMBER / STAFF NUMBER")
for row in examinations:
    print(row)
conn.commit()
print("--------------------------------------------------------------------------------------------")

# list all staff working at a specific clinic
print("Transaction 5: List all staff working at a specific clinic. (clinicID = 10001)\n")
clinic_id = 10001
query = """
    SELECT * FROM Staff
        WHERE clinicNo = ?
        """
cursor.execute(query, (clinic_id,))
stafflist = cursor.fetchall()
print("After query... (showing results obtained from transaction on Staff)\n")
print("STAFF NUMBER / FIRST NAME / LAST NAME / STREET / BUILDING INFO / CITY / STATE / ZIP / TELEPHONE / DOB / POSITION / SALARY / CLINIC NUMBER")
for row in stafflist:
    print(row)
conn.commit()
print("============================================================================================")

