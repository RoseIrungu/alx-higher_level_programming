-- script that creates the database hbtn_0d_usa
-- create table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO GENRATE NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
