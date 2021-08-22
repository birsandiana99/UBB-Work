create database practicDB
go
use practicDB
go
create table Course(
CourseID int primary key identity,
Name varchar(50),
Credits int,
EnrolledStudents int,
StartDate date,
EndDate date
)



insert into Course values ('FP', 20, 150 ,  '2000-04-04', '2000-04-05'), ('OS', 20, 150 ,  '2000-04-04', '2000-04-05')
select * from Course

update Course set EnrolledStudents=150 where CourseID=2