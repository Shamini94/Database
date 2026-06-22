# Tech Events & Meetups Platform

## Overview
  This project is a database-driven tech events & meetups management system that stores and organises information about meetups, workshops and community events. It allows users to track event details such as titles, descriptions, schedules, organisers, and venues, and supports querying and analysis of events using SQL.

## Technologies Used
- PostgreSQL
- SQL for querying and analysis
- JSON for initial data reresentation
- Relational data modelling (organisers, venues, events)

## Database setup
 To create a clean local database environment, run the setup script:

```bash
psql -f db/setup.sql 

## Environment Setup

This project uses environment variables to manage local configuration (including database credentials).

### 1. Create your `.env` file

A `.env.example` file is provided in the repository with all required keys.  
To run the project locally, create your own `.env` file in the project root:

```bash
cp .env.example .env