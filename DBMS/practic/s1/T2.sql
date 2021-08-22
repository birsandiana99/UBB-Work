use practicDB
go
-- first version - as it is
-- second version
--set transaction isolation level READ UNCOMMITTED
-- third version
set transaction isolation level REPEATABLE READ
-- forth version
--set transaction isolation level READ COMMITTED
BEGIN TRAN
update Course set EnrolledStudents = EnrolledStudents + 10
where CourseID=2

waitfor delay '00:00:10'
ROLLBACK TRAN