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
values (123, 1000000);
insert into dentist
values (123);



insert into branch(city, manager_id)
values ('cool city', 123);

insert into branch(city, manager_id)
values ('bad city', 123);


INSERT INTO procedure
VALUES ('scal', 'Scaling');

INSERT INTO procedure
VALUES ('fluo', 'Fluoride');

INSERT INTO procedure
VALUES ('remove', 'removal');

INSERT INTO Appointment_procedure
VALUES ('cavity', 'Cavity Filling');


