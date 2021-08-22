use MiniFacebook_IE
Go
BEGIN TRAN
WAITFOR DELAY '00:00:05'
UPDATE Categories SET CDescription='interesting546465' WHERE Cid = 2
COMMIT TRAN