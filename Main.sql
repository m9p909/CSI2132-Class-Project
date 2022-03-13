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
    person_id int,
    insurance varchar(100),
    foreign key (person_id) references person(person_id)
)