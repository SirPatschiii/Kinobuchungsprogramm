class Booking:
    def __init__(self):
        print("Booking works!")

    def selected_cinema(self, cinema_title):
        self.selected_cinema = cinema_title

    def get_selected_cinema(self):
        return self.selected_cinema

    def selected_movie(self, movie_title_lbl):
        self.selected_movie = movie_title_lbl

    def get_selected_movie(self):
        return self.selected_movie

    def selected_event(self, event_rad_selection):
        self.selected_event = event_rad_selection

    def get_selected_event(self):
        print(self.selected_event)
        return self.selected_event

