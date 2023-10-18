--  creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS 'hbtn_0d_usa'.'cities' (
    PRIMARY KEY('id'),
    'id'    INT    NOT NUL      AUTO_INCREMENT,
    'state_id'  INT     NOT NULL
    'name'  VARCHAR(256) NOT NUL
    FOREIGN_KEY('state_id'),
    REFERENCES 'hbtn_0d_usa'.'states'('id')
);