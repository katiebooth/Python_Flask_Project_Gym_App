DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;

CREATE TABLE members (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  premium BOOLEAN,
  active BOOLEAN
);

CREATE TABLE classes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  date DATE,
  time VARCHAR(255),
  price INT,
  capacity INT,
  premium BOOLEAN
);

CREATE TABLE bookings(
  id BIGSERIAL PRIMARY KEY,
  member_id INT REFERENCES members(id) ON DELETE CASCADE,
  classes_id INT REFERENCES classes(id) ON DELETE CASCADE
);