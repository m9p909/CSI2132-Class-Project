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
	record_id int primary key,
	patient_id int,
	employee_id int,
	employee_notes varchar(20),
	FOREIGN KEY (employee_id)
	REFERENCES Employee,
	FOREIGN KEY (patient_id)
	REFERENCES Patient
);
	
CREATE TABLE Invoice(
	invoice_id int primary key,
	patient_id int,
	date_of_issue date,
	FOREIGN KEY (patient_id),
	REFERENCES Patient
);
	
CREATE TABLE Fee_Charge(
	fee_id int primary key,
	invoice_id int,
	fee_code int,
	charge int,
	FOREIGN KEY (invoice_id),
	REFERENCES Invoice
);
	
