create table person
(
    person_id     SERIAL PRIMARY KEY,
    SSN           int,
    b_date        date,
    f_name        varchar(100),
    l_name        varchar(100),
    city          varchar,
    house_number  int,
    street        varchar,
    postal_code   varchar(6),
    province      varchar(30),
    email         varchar(100),
    gender        varchar,
    phone_number  varchar,
    care_giver_id int,
    FOREIGN KEY (person_id) REFERENCES person (person_id)
);

create table patient
(
    patient_id SERIAL PRIMARY KEY,
    person_id  int,
    insurance  varchar(100),
    foreign key (person_id) references person (person_id)
);

create table employee
(
    employee_id SERIAL PRIMARY KEY,
    person_id   int,
    salary      bigint,
    foreign key (person_id) references person (person_id)
);

create table manager
(
    employee_id int unique,
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);

create table branch
(
    branch_id  serial primary key,
    manager_id int,
    FOREIGN KEY (manager_id) references manager (employee_id)
);

create table dentist
(
    employee_id int primary key,
    branch_id   int,
    FOREIGN KEY (branch_id) references branch (branch_id),
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);

create table receptionist
(
    employee_id int primary key,
    branch_id   int,
    FOREIGN KEY (branch_id) references branch (branch_id),
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);

create table hygienist
(
    employee_id int primary key,
    branch_id   int,
    FOREIGN KEY (branch_id) references branch (branch_id),
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);

create table "user"
(
    username varchar PRIMARY KEY,
    password varchar,
    person_id int,
    foreign key (person_id) references person (person_id)
);

CREATE TABLE Patient_Records(
	record_id serial primary key,
	patient_id int,
	employee_id int,
	employee_notes varchar(20),
	FOREIGN KEY (employee_id)
	REFERENCES Employee,
	FOREIGN KEY (patient_id)
	REFERENCES Patient
);
	
CREATE TABLE Invoice(
	invoice_id serial primary key,
	patient_id int,
	date_of_issue date,
	FOREIGN KEY (patient_id)REFERENCES Patient
);
	
CREATE TABLE Fee_Charge(
	fee_id serial primary key,
	invoice_id int,
	fee_code int,
	charge int,
	FOREIGN KEY (invoice_id) REFERENCES Invoice
);

CREATE TABLE Review(
	review_id INT primary key,
	professionalism int check(10 >= professionalism and professionalism >= 0),
	communication int check(10 >= communication and communication >= 0),
	cleanliness int check(10 >= cleanliness and cleanliness >= 0),
	review_value INT check(10 >= review_value and review_value >= 0),
	patient_id INT,
	branch_id INt,
	FOREIGN KEY (patient_id) REFERENCES Patient,
	FOREIGN KEY (branch_id) REFERENCES Branch
);


CREATE TABLE Treatment(
	treatment_id int primary key,
	patient_id int,
	treatment_type varchar(50),
	appointment_id int,
	treatment_details varchar(100),
	record_id int,
	FOREIGN KEY (patient_id) REFERENCES Patient,
	FOREIGN KEY (appointment_id) REFERENCES Appointment,
	FOREIGN KEY (record_id) REFERENCES Patient_Records
);

CREATE TABLE Appointment(
	appointment_id INT primary key,
	patient_id INT,
	dentist_id INT,
	appintment_date date,
	start_time timestamp,
	end_time timestamp,
	appointement_type varchar(50),
	status varchar(50),
	room_assigned varchar(50),
	FOREIGN KEY (patient_id)
	REFERENCES Patient,
	FOREIGN KEY (dentist_id) REFERENCES Dentist
);
CREATE TABLE Appointment_Procedure(
	appointment_proc_id INT primary key,
	appointment_id INT,
	procedure_code  VARCHAR(50),
	procedure_type  VARCHAR(50),
	appintment_date date,
	invoice_id int,
	tooth_involved VARCHAR(50),
	amount_of_procedure INT,
	patient_charge INT,
	insurance_charge INT,
	total_charge INT,
	insurance_claim_id INT,
	FOREIGN KEY (appointment_id)
	REFERENCES Appointment,
	FOREIGN KEY (invoice_id)
	REFERENCES Invoice,
	FOREIGN KEY (insurance_claim_id) REFERENCES Insurance_claim
);

CREATE TABLE Insurance_Claim(
	appointment_proc INT PRIMARY KEY,
	payment_id INT,
	FOREIGN KEY(payment_id)
	REFERENCES Payment,
	FOREIGN KEY(appointment_proc_id) REFERENCES Appointment_Procedure
);

CREATE TABLE Payments(
	payment_id int primary key,
	invoice_id INT,
	patient_charge INT,
	insurance_charge INT,
	total_charge INT,
	payment_type VARCHAR,
	FOREIGN KEY (invoice_id) REFERENCES Invoice
);
	
