-- Script that List all Comedy shows from the hbtn_0d_tvshows database
SELECT tv_shows.title -- Query to jion tables
FROM tv_shows
JOIN tv_genres ON tv_shows.id = tv_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
