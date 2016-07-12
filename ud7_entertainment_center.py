import ud7_media
import fresh_tomatoes

toy_story=ud7_media.Movie("Toy Story",30,"Story of a boy and his toys","http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline

avatar=ud7_media.Movie("Avatar",50,"Story about aliens","https://www.movieposter.com/posters/archive/main/98/MPW-49246","https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print avatar.duration

#avatar.show_trailer()

school_of_rock=ud7_media.Movie("School of Rock",45,"fun story","http://3.bp.blogspot.com/-LIzGt3Rbd_I/USLKZc_VkHI/AAAAAAAADl4/ose8aai1RPM/s1600/Screen+Shot+2013-02-18+at+4.39.37+PM.png","https://www.youtube.com/watch?v=XCwy6lW5Ixc")

movies=[toy_story,avatar,school_of_rock]
fresh_tomatoes.open_movies_page(movies)

#print ud7_media.Movie.VALID_RATINGS

#print ud7_media.Movie.__doc__

