DROP DATABASE IF EXISTS stroke;

CREATE DATABASE stroke;
CREATE USER strokeuser WITH PASSWORD 'stroke';
GRANT ALL PRIVILEGES ON DATABASE stroke TO strokeuser;