import webbrowser
class Video():
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
class Movie(Video):
    """ List of movies and its information"""
    VALID_RATINGS=['A','UA','U']
    
    def __init__(self,movie_title,movie_duration,movie_storyline,poster_image,trailer_youtube):
        Video.__init__(self,movie_title,movie_duration)
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TVshows(Video):
    def __init__(self,tv_title,tv_duration,tv_no_of_ep):
        Video.__init__(self,tv_title,tv_duration)
        self.noofep=tv_no_of_ep
        
        
