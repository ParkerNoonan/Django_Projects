# Django_Projects
Summary
This was a python project that I created for work. It streamlined the development of two documents that I routinely work with.
The information for the documents was archived in a Postgres database, along with other relevant project data, and called on to
both size the correct actuators for the valves we were remotely controlling but also automate the creation of the design basis manual and 
actuator data sheets. Both documents share a significant amount of information and it is tedious to review by hand.

How the program worked:
Creating Design Basis Manual
1. User goes to first page and logs project information into Django form.
2. Form is then presented to user in read-only format for review.
3. If submitted, project information saved in Postgres database.
4. User can go to a Project page and pick a project to do CRUD operations on (review, update, or delete).

Actuator datasheet
1. User chooses a project to add and actuator to.
2. Program retrieves project information from database and presents dropdown menu for user to pick valve.
3. Program calculates the minimum and maximum valve torques and pulls only actuators from the database that meet these torques.
4. User picks actuator and submits it. Database is queried for info on not only the project but also the site to put together the actuator datasheet.

