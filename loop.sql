select * from films;
create table filmscopy as select * from films; 
select * from filmscopy;


DO $$
DECLARE
    film_id     	filmscopy.film_id%TYPE;
    film_name   	filmscopy.film_name%TYPE;
	film_overview  	filmscopy.film_overview%TYPE;
	genre_id		filmscopy.genre_id%TYPE;
	director_id 	filmscopy.director_id%TYPE;
	year_id 		filmscopy.year_id%TYPE;
	

BEGIN
    film_id := 100;
    film_name := 'Film';
	film_overview := 'Overview of the film ';
	genre_id := 1;
	director_id := 1;
	year_id := 1;
	
    FOR counter IN 1..5
        LOOP
            INSERT INTO filmscopy(film_id, film_name, film_overview, genre_id, director_id, year_id)
            VALUES (film_id + counter, film_name || counter, film_overview || counter, genre_id, director_id, year_id);
        END LOOP;
END
$$