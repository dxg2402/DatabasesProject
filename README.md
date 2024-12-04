# Pawsome Pets

## Case Study
From the project specification...
> A company called Pawsome Pets runs multiple clinics. The company would like for their data to be stored in a database. The following description was obtained during the analysis phase:

> “Each of the Pawsome Pets clinics has several staff members and a member of staff manages at most one clinic (not all staff manage clinics). Each clinic has a unique clinic number (clinicNo) and each member of staff has a unique staff number (staffNo). Additionally, the company would like to store each clinic’s name, address and telephone number, as well as the staff’s name, address, telephone number, DOB, position and salary. 
> When a pet owner contacts a clinic, the owner’s pet is registered with the clinic. An owner can own one or more pets, but a pet can only be registered at one clinic. Each owner has a unique owner number (ownerNo), a name, an address and a telephone number. Each pet has a unique pet number (petNo), name, DOB, animal species, breed and color.
> When the pet comes to the clinic, it undergoes an examination by a member of the consulting staff. The database should store the following information for each examination: chief complaint (i.e., the main cause for the visit), description (i.e., what was done during the examination), date seen and actions taken (e.g., a treatment was prescribed, tests were ordered). A unique examination number (examNo) is assigned to each examination.”

## Project Overview
This case study and corresponding project serves as an exercise in the major steps of designing and operating a database management system (DBMS).
The project is broken up into three parts, each corresponding to an important step in the process of realizing such a system:
1. the design of a conceptual data model, where key entities and relationships are identified and a basic entity-relationship diagram provided
2. the development of a logical data model, which builds on the conceptual model by introducing constraints, domains, and proper logical structuring for identified relationships
3. the implementation, which uses SQLite and Python to provide database functionalities

## Project Contents
*/docs*
This folder contains all of the documentation for the project. Separate reports are included for each phase of the project. Reading each report is encouraged, as it explains elements of the implemented design and provides rationale for various decisions made throughout the process.

*pawsomePets_demo.py*
This Python script creates the database on a local machine, populates it with data, and automatically validates the database by performing sample transactions identified in the documentation. The program outputs the data in each table after initialization and population, as well as the results from the sample transactions.
Running this script requires Python 3 to be installed on the user's computer, in addition to either a Python IDE (e.g. PyCharm) or a terminal window.
If ran using the terminal, the script can be executed using the following command:
```
python3 pawsomePets_demo.py
```
