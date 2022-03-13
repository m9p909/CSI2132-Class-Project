INSERT INTO person(SSN,b_date,f_name,l_name,city,house_number,street,postal_code,province,email,gender,phone_number) VALUES (564847154, '1984-05-19', 'John', 'Smith', 'Ottawa', 97, 'Laurier','K2W5E9', 'Ontario', 'jsmith@gmail.com', 'Male', '6135421874');
INSERT INTO patient(person_id,insurance) VALUES (1,10);

INSERT INTO branch(city) VALUES ('Ottawa');
INSERT INTO person(SSN,b_date,f_name,l_name,city,house_number,street,postal_code,province,email,gender,phone_number) VALUES (659874512, '1964-01-09', 'Sarah', 'Whyte', 'Ottawa', 25, 'Burns','K0P7G2', 'Ontario', 'swhyte@gmail.com', 'Female', '613879648');
INSERT INTO employee(person_id,salary) VALUES (2,100000);
INSERT INTO dentist(employee_id,branch_id) VALUES (1,1);

SELECT employee_id , d.branch_id 
FROM dentist d, branch b 
WHERE d.branch_id=b.branch_id;

INSERT INTO appointment(patient_id,dentist_id,appointment_date,start_time,end_time,appointement_type,appointement_status,room_assigned) VALUES(1,1, '2008-09-18','2008-09-18 13:00:00', '2008-09-18 14:00:00', 'dental', 'confirmed', '12');

SELECT appointment_id,patient_id,a.dentist_id,appointment_date,start_time,end_time,appointement_type,appointement_status,room_assigned
FROM appointment a, dentist d
WHERE a.dentist_id = d.employee_id;

SELECT DISTINCT appointement_type
FROM appointment

