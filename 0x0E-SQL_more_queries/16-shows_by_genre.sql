-- Script that List all shows and linked genres from the hbtn_0d_tvshows database
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.show_id
ORDER BY tv_shows.title ASC, genre ASC;
