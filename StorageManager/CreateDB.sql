CREATE USER zno_admin WITH PASSWORD 'qwerty';
CREATE DATABASE zno WITH OWNER zno_admin;
\c zno zno_admin

CREATE TABLE University(
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE Faculty(
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE Speciality(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    edu_program TEXT NOT NULL,
    UNIQUE(name, edu_program)
);

CREATE TABLE Entrants(
    id SERIAL PRIMARY KEY,
    university_id INTEGER REFERENCES University(id) ON DELETE CASCADE ON UPDATE CASCADE,
    faculty_id INTEGER REFERENCES Faculty(id) ON DELETE CASCADE ON UPDATE CASCADE,
    speciality_id INTEGER REFERENCES Speciality(id) ON DELETE CASCADE ON UPDATE CASCADE,
    year INTEGER CHECK (year >= 2019 AND year <= date_part('year', CURRENT_DATE)::INTEGER) NOT NULL,
    priority INTEGER CHECK (priority >= 0 AND priority <= 5) NOT NULL,
    point NUMERIC(6,3) CHECK (point >= 100 AND priority <= 200) NOT NULL,
    points JSONB,
    coeficients CHAR(2)[],
    quoats CHAR(3)[]
);
