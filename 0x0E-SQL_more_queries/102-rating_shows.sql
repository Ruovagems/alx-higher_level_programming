-- Script that List all shows by their rating from the hbtn_0d_tvshows_rate database
SELECT tv_shows.title, SUM(ratings.rating) AS rating_sum
FROM tv_shows
LEFT JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
