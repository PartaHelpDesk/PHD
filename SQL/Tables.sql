/****** Object:  Table [dbo].[users]    Script Date: 3/6/2019 4:36:47 PM ******/
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
