INSERT INTO cities (name, country)
SELECT name, country
FROM sz_cities

INSERT INTO fop (fio, address, kved)
SELECT FIO, ADDRESS, KVED
FROM sz_fop

INSERT INTO jobs (group_name_major, group_name_minor, name, name_long, def)
SELECT `Major Group Name`, `Minor Group Name`, `Broad Occupation Name`, `Detailed Occupation Name`, `Definition`
FROM sz_jobs