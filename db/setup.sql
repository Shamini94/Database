-- Terminate existing connections to allow DROP DATABASE
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'nc_plus_one';

-- Drop database if it exists
DROP DATABASE IF EXISTS nc_plus_one;

-- Recreate clean database
CREATE DATABASE nc_plus_one;