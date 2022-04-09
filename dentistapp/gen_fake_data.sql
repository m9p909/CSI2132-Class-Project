-- create manager
insert into person
values (123,
        '02 / 14 / 10',
        'manager',
        'frog',
        'the future',
        12,
        'potato street',
        '111111',
        'ON',
        'adsa@ad.com',
        'Male',
        '1111111');

INSERT into employee
values (123, 1000000);

insert into manager
values (123);



insert into branch(city, manager_id)
values ('cool city', 123);

insert into branch(city, manager_id)
values ('bad city', 123);

-- create dentist
insert into person
values (321,
        '02 / 14 / 10',
        'dentist',
        'frog',
        'the future',
        12,
        'potato street',
        '111111',
        'ON',
        'adsa@ad.com',
        'Male',
        '1111111');
INSERT into employee
values (321, 1000000);

insert into dentist
values (321, 1);

--Create patient--
insert into person
values (555,
        '02 / 14 / 10',
        'patient',
        'frog',
        'the future',
        12,
        'potato street',
        '111111',
        'ON',
        'adsa@ad.com',
        'Male',
        '1111111');

INSERT INTO patient
VALUES (555, '111111');


INSERT INTO procedure
VALUES ('scal', 'Scaling');

INSERT INTO procedure
VALUES ('fluo', 'Fluoride');

INSERT INTO procedure
VALUES ('remove', 'removal');

INSERT INTO procedure
VALUES ('cavity', 'Cavity Filling');





INSERT INTO person(person_id, b_date, f_name, l_name, city, house_number, street, postal_code, 
            province, email, gender, phone_number) 
            VALUES (43,TO_DATE('20220303', 'YYYYMMDD'),'Pascal','Siakam','Toronto',43,'yonge st','123456',
           'On','spicyP@gmail.com', 
            'male',123456789);
            INSERT  INTO patient(patient_id, insurance)
            VALUES (43, 'idk');
                        
                        
INSERT INTO person(person_id, b_date, f_name, l_name, city, house_number, street, postal_code, 
            province, email, gender, phone_number) 
            VALUES (222,TO_DATE('20220303', 'YYYYMMDD'),'Gary','Trent','Toronto',23,'yonge st','123456',
           'On','gt3@gmail.com', 
            'male',123456789);
            INSERT  INTO patient(patient_id, insurance)
            VALUES (222, 'idk');
                        
                        
INSERT INTO person(person_id, b_date, f_name, l_name, city, house_number, street, postal_code, 
            province, email, gender, phone_number) 
            VALUES (456,TO_DATE('20220303', 'YYYYMMDD'),'OG','Annunoby','Toronto',23,'yonge st','123456',
           'On','imOG@gmail.com', 
            'male',123456789);
            INSERT  INTO patient(patient_id, insurance)
            VALUES (456, 'idk');
                        

                        
                        
INSERT INTO person(person_id, b_date, f_name, l_name, city, house_number, street, postal_code, 
            province, email, gender, phone_number) 
            VALUES (2323,TO_DATE('20220303', 'YYYYMMDD'),'Fred','Vanvleet','Toronto',23,'yonge st','123456',
           'On','steadyfreddy@gmail.com', 
            'male',123456789);
            INSERT  INTO Employee(employee_id, salary)
            VALUES (2323, 500000000);
                        
INSERT  INTO Dentist(employee_ID, branch_id)
                VALUES (2323,2);                        


INSERT INTO person(person_id, b_date, f_name, l_name, city, house_number, street, postal_code, 
            province, email, gender, phone_number) 
            VALUES (236,TO_DATE('20220303', 'YYYYMMDD'),'Lebron','James','Cleveland',23,'yonge st','123456',
           'On','goatjames@gmail.com', 
            'male',123456789);
            INSERT  INTO Employee(employee_id, salary)
            VALUES (236, 500000000);
                        
INSERT  INTO Dentist(employee_ID, branch_id)
                VALUES (236,1); 
                                
                                
                                

INSERT INTO appointment(patient_id,dentist_id,appointment_date,start_time,end_time,appointement_type,appointement_status,room_assigned)
            VALUES(43,2323,TO_DATE('20220303','YYYYMMDD'),TO_TIMESTAMP('20220303 10', 'YYYYMMDD HH'), TO_TIMESTAMP('20220303 11', 'YYYYMMDD HH'), 'Checkup','Available', 57);

INSERT INTO appointment(patient_id,dentist_id,appointment_date,start_time,end_time,appointement_type,appointement_status,room_assigned)
            VALUES(222,2323,TO_DATE('20220507','YYYYMMDD'),TO_TIMESTAMP('20220507 10', 'YYYYMMDD HH'), TO_TIMESTAMP('20220507 11', 'YYYYMMDD HH'), 'Wisdom teeth removal','Available', 23);


INSERT INTO appointment(patient_id,dentist_id,appointment_date,start_time,end_time,appointement_type,appointement_status,room_assigned)
            VALUES(456,236,TO_DATE('20220527','YYYYMMDD'),TO_TIMESTAMP('20220527 10', 'YYYYMMDD HH'), TO_TIMESTAMP('20220527 11', 'YYYYMMDD HH'), 'Filling','No show', 23);


INSERT INTO appointment(patient_id,dentist_id,appointment_date,start_time,end_time,appointement_type,appointement_status,room_assigned)
            VALUES(555,236,TO_DATE('20220527','YYYYMMDD'),TO_TIMESTAMP('20220527 6', 'YYYYMMDD HH'), TO_TIMESTAMP('20220527 8', 'YYYYMMDD HH'), 'Checkup','Available', 23);

