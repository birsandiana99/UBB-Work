use practicDB
go
-- first version - as it is
-- second version
--set transaction isolation level READ UNCOMMITTED
-- third version
set transaction isolation level READ COMMITTED
-- forth version
--set transaction isolation level REPEATABLE READ
BEGIN TRAN
update Course set EnrolledStudents=EnrolledStudents + 20 
where CourseID = 2
waitfor delay '00:00:10'
select * from Course where CourseID = 2

update Course
set EnrolledStudents = EnrolledStudents + 10
where CourseID = 2

COMMIT TRAN