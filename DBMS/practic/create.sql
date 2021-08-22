--drop database Practic
create database Practic
go
use Practic
go

create table CoffeeShops(
CSid int primary key identity(1,1),
CSName VARCHAR(50),
Address VARCHAR(50),
)
create table Customers(
Cid int primary key identity(1,1),
CName VARCHAR(50)
)

create table ProductCategories(
PCid int primary key identity(1,1),
PCName varchar(50),
PCDescription varchar(100)
)

create table CoffeeProducts(
CPid int primary key identity(1,1),
CPName varchar(50),
PCid int foreign key references ProductCategories(PCid),
)


create table Likes(
Cid int	references Customers(Cid),
CPid int references CoffeeProducts(CPid),
CONSTRAINT pk_Like PRIMARY KEY(Cid,CPid)
)

create table Orders(
Cid int references Customers(Cid),
CSid int references CoffeeShops(CSid),
CPid int references CoffeeProducts(CPid),
Price int,
Date date,
Time time,
CONSTRAINT pk_Orders PRIMARY KEY(Cid, CSid, CPid)
)

INSERT CoffeeShops VALUES('Coffee shop', 'Cluj-Napoca'), ('Another coffee shop','Timisoara')
INSERT Customers VALUES('Gigel'), ('Marcel')
INSERT ProductCategories VALUES('Category1', 'desc1'), ('Category 2', 'description 2')
INSERT CoffeeProducts VALUES('coffee1', 1), ('coffee2',2)
INSERT Likes VALUES (1,1), (1,2)
INSERT Orders VALUES (1,1,1,10,'2019-09-10','13:34')

GO
select * from CoffeeShops
select * from Customers
select * from ProductCategories
select * from CoffeeProducts
select * from Orders
select * from likes
select * from Orders



UPDATE Customers SET CName='GIGEL' WHERE Cid = 2
select * from Customers