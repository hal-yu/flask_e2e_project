INSERT INTO doctors(
    first_name,
    last_name,
    specialization,
    contact_number)
VALUES
('Atsumu', 'Miya', 'Psychiatry', '6461115454'),
('Osamu', 'Miya', 'Internal Medicine', '6461115456'),
('Satoru', 'Gojo', 'Cardiology', '6462221314'),
('Chuuya', 'Nakahara', 'Pediatrics', '6461211218'),
('Ryoma', 'Echizen', 'Sports Medicine', '6466661234');

INSERT INTO patients (
    first_name,
    last_name,
    date_of_birth,
    primary_doctor_id,
    contact_number
)
VALUES
('Kita', 'Shinsuke', '2000-02-16', 1, '6462211259'),
('Kageyama', 'Tobio', '2000-05-07', 2, '6461514547'),
('Hinata', 'Shouyo', '2000-10-10', 2, '9175451122'),
('Suna', 'Rinatro', '2000-12-18', 3, '9174488545'),
('Kuroo', 'Tetsurou', '1999-12-17', 1, '9176543210'),
('Bokuto', 'Koutarou', '1999-03-20', 3, '9179876543'),
('Tsukishima', 'Kei', '2000-11-22', 2, '6468886543');

INSERT INTO appointments (
    doctor_id, 
    patient_first_name,
    patient_last_name, 
    appointment_date,
    appointment_time
)
VALUES
    (1, 'Kita', 'Shinsuke', '2023-01-15', '10:00:00'),
    (2, 'Kageyama', 'Tobio', '2023-02-20', '14:30:00'),
    (2, 'Hinata', 'Shouyo', '2023-03-05', '11:45:00'),
    (3, 'Suna', 'Rinatro', '2023-03-18', '09:15:00'),
    (1, 'Kuroo', 'Tetsurou', '2023-04-02', '13:00:00'),
    (3, 'Bokuto', 'Koutarou', '2023-04-10', '15:30:00'),
    (2, 'Tsukishima', 'Kei', '2023-05-12', '12:45:00');




