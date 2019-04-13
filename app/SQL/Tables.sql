--Sql to create PHD tables 
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Users](
	[UserID] [int] IDENTITY(1,1) NOT NULL,
	[Level] [int] NOT NULL,
	[Username] [varchar](16) NOT NULL UNIQUE,
	[FirstName] [varchar](128) NOT NULL ,
	[LastName] [varchar](128) NOT NULL,
	[Email] [varchar](128)NOT NULL,
	[Password] [varchar](256) NOT NULL,
	[PasswordResetDate] [datetime] NOT NULL DEFAULT GETDATE(),
	[Active] [bit] NOT NULL DEFAULT 0,
	[Authenticated] [bit] NOT NULL DEFAULT 0,

PRIMARY KEY CLUSTERED 
(
	[UserID] ASC
)
)

-----------------------------------------------------------------------
CREATE TABLE [dbo].[Tickets](
	[TicketID] [int] IDENTITY(1,1) NOT NULL,
	[Title] [varchar](128) NOT NULL,
	[Category] [varchar](128) NOT NULL,
	[CreatedUserID] [int] NOT NULL,
	[Status] [varchar](128) NOT NULL,
	[CreateDate] [datetime] DEFAULT GETDATE(),
	[ClosedDate] [datetime] DEFAULT NULL,
	[Department] [varchar] (128)NOT NULL,
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
	[UserID] [int] NOT NULL,
	[Category] [varchar](128) NOT NULL,
	[Title] [varchar](128) NOT NULL,
	[Status] [varchar](128) NOT NULL,
	[Department] [varchar](128) NOT NULL,
	[Description] [varchar](280) NOT NULL,
	[Date] [datetime] NOT NULL,


PRIMARY KEY CLUSTERED 
(
	[TicketHistoryID] ASC
)
)

-----------------------------------------------------------------------
CREATE TABLE [dbo].[RelatedTickets](
	[TicketID1] [int] NOT NULL,
	[TicketID2] [int] NOT NULL,

)

-----------------------------------------------------------------------

CREATE TABLE [dbo].[TicketAttachments](
	[TicketID] [int] NOT NULL,
	[FilePath] [varchar] (128) NOT NULL,

)

-----------------------------------------------------------------------
CREATE TABLE [dbo].[Categories](
	[Description] [varchar] (32) NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[Description] ASC
)
)

CREATE TABLE [dbo].[Status](
	[Description] [varchar] (32) NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[Description] ASC
)
)
-----------------------------------------------------------------------
CREATE TABLE [dbo].[Departments](
	[Description] [varchar] (32) NOT NULL,

PRIMARY KEY CLUSTERED 
(
	[Description] ASC
)
)

