--Sql to create PHD tables 
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Users](
	[UserID] [int] IDENTITY(1,1) NOT NULL,
	[FirstName] [varchar](128) NOT NULL,
	[LastName] [varchar](128) NOT NULL,
	[Email] [varchar](128)NOT NULL,
	[Password] [varchar](256) NOT NULL,
	[Active] [bit] NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[UserID] ASC
)
)

-----------------------------------------------------------------------
CREATE TABLE [dbo].[Tickets](
	[TicketID] [int] IDENTITY(1,1) NOT NULL,
	[Category] [int] NOT NULL,
	[Title] [varchar](128) NOT NULL,
	[CreatedUserID] [int] NOT NULL,
	[Status] [int] NOT NULL,
	[CreateDate] [datetime] NOT NULL,
	[ClosedDate] [datetime] NOT NULL,
	[Department] [int] NOT NULL,
	[Location] [int] NOT NULL,
	[Description] [varchar](280) NOT NULL 


PRIMARY KEY CLUSTERED 
(
	[TicketID] ASC
)
)
-----------------------------------------------------------------------

CREATE TABLE [dbo].[TicketHistory](
	[TicketHistoryID] [int] IDENTITY(1,1) NOT NULL,
	[TicketID] [int] NOT NULL,
	[Category] [int] NOT NULL,
	[Title] [varchar](128) NOT NULL,
	[Status] [int] NOT NULL,
	[Department] [int] NOT NULL,
	[Location] [int] NOT NULL,
	[Description] [varchar](280) NOT NULL,
	[Date] [datetime] NOT NULL,


PRIMARY KEY CLUSTERED 
(
	[TicketHistoryID] ASC
)
)

-----------------------------------------------------------------------
CREATE TABLE [dbo].[RelatedTickets](
	[RelatedTicketID] [int] IDENTITY(1,1) NOT NULL,
	[TicketID1] [int] NOT NULL,
	[TicketID2] [int] NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[RelatedTicketID] ASC
)
)

-----------------------------------------------------------------------

CREATE TABLE [dbo].[TicketAttachments](
	[TicketID] [int] NOT NULL,
	[FilePath] [varchar] (128) NOT NULL,

)

-----------------------------------------------------------------------
CREATE TABLE [dbo].[Categories](
	[CategoryID] [int] IDENTITY(1,1) NOT NULL,
	[Description] [varchar] (32) NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[CategoryID] ASC
)
)

CREATE TABLE [dbo].[Status](
	[StatusID] [int] IDENTITY(1,1) NOT NULL,
	[Description] [varchar] (32) NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[StatusID] ASC
)
)
-----------------------------------------------------------------------
CREATE TABLE [dbo].[Departments](
	[DepartmentID] [int] IDENTITY(1,1) NOT NULL,
	[Description] [varchar] (32) NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[DepartmentID] ASC
)
)

-----------------------------------------------------------------------
CREATE TABLE [dbo].[Locations](
	[LocationID] [int] IDENTITY(1,1) NOT NULL,
	[Description] [varchar] (32) NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[LocationID] ASC
)
)