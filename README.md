Technologies Used:

Flask for the web application.
PostgreSQL for the database.
Docker for containerization.
Setup Instructions:

Clone this repository to your local machine.
Create a PostgreSQL database named after your own name (e.g., “Abbos”).
Insert at least 5 real courses from Webster University’s timetable into the database.
Customize the HTML header to display your name as the student.
Build and run the Flask app inside a Docker container using the provided Dockerfile.
How to Run the Application:

Ensure Docker is installed on your system.
Run the following commands:
arduino
Copy code
docker build -t university-timetable .
docker run -p 5000:5000 university-timetable
Open a browser and navigate to http://localhost:5000 to view the application.
Screenshots: [Include screenshots of the final web application here.]

Acknowledgements:

Webster University for providing the course data.
Docker and Flask for the application setup.

![image](https://github.com/user-attachments/assets/822d6f72-eb70-40a6-bfca-3e0ded584343)
