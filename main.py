import webapp2
import jinja2
import os
from google.appengine.api import users
from models import User

the_jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = [],
    autoescape = True
)

def logged_in():
    user = users.get_current_user()
    status = ""
    if user:
        status = "Sign Out"
    else:
        status = "Sign In"
    return status

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        status = logged_in()
        link = users.create_logout_url('/login')
        if status == "Sign In":
            link = '/login'
        welcome_template = the_jinja_environment.get_template('templates/welcome.html')
        temp_dict = {'status': status, 'link': link}
        self.response.write(welcome_template.render(temp_dict))

class DiscountPage(webapp2.RequestHandler):
    def get(self):
        discount_template = the_jinja_environment.get_template('templates/discount.html')
        self.response.write(discount_template.render())

class EventsPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        events_template = the_jinja_environment.get_template('templates/events.html')
        temp_dict = {'status': status, 'link': link, 'college': college}
        self.response.write(events_template.render(temp_dict))
        if user:
            self.response.write('''This is your college %s'''%(college))
            self.response.write('''
                <h3>%s</h3>
                <p>This is the events page for %s</p>'''
                % (college, college))
        else:
            self.response.write('''
                <div class="tab">
                    <button class="tablinks" onclick="openCollege(event, 'Georgia Tech')">Georgia Tech</button>
                    <button class="tablinks" onclick="openCollege(event, 'Georgia State University')">Georgia State University</button>
                    <button class="tablinks" onclick="openCollege(event, 'Emory University')">Emory University</button>
                    <button class="tablinks" onclick="openCollege(event, 'Spelman College')">Spelman College</button>
                </div>

                <div id="Georgia Tech" class="tabcontent" style="display: none;">
                    <h3>Georgia Tech</h3>
                    <p>This is the events page for Georgia Tech</p>
                </div>

                <div id="Georgia State University" class="tabcontent" style="display: none;">
                    <h3>Georgia State University</h3>
                    <p>This is the events page for Georgia State University</p>
                </div>

                <div id="Emory University" class="tabcontent" style="display: none;">
                    <h3>Emory University</h3>
                    <p>This is the events page for Emory University</p>
                </div>

                <div id="Spelman College" class="tabcontent" style="display: none;">
                    <h3>Spelman College</h3>
                    <p>This is the events page for Spelman College</p>
                </div>''')

class LoginPage(webapp2.RequestHandler):
    def get(self):
        # login_template = the_jinja_environment.get_template('templates/login.html')
        user = users.get_current_user()
        if not user:
            self.response.write('''
                Please log in to our site! <br>
                <a href="%s">Sign in</a><br><br>
                Or sign up now!<br><a href="%s">Sign Up</a>'''
                % (users.create_login_url('/login'), users.create_login_url('/login')))
        else:
            email_address = user.nickname()
            cssi_user = User.get_by_id(user.user_id())
            signout_link_html = '<a href="%s">Sign Out</a>' %(users.create_logout_url('/login'))
            if cssi_user:
                self.response.write('''Welcome %s %s (%s)! <br> You go to %s! <br> %s''' % (cssi_user.first_name, cssi_user.last_name, cssi_user.college, email_address, signout_link_html))
            else:
                self.response.write('''
                    Please Sign Up %s!<br>
                    <form method="post" action="/login">
                    <input type="text" name="first_name">
                    <input type="text" name="last_name">
                    <br>
                    <select name="college">
                    <option value="" disabled selected>Choose your college</option>
                    <option value="Georgia Tech">Georgia Tech</option>
                    <option value="Georgia State University">Georgia State University</option>
                    <option value="Emory University">Emory University</option>
                    <option value="Spelman College">Spelman College</option>
                    </select>
                    <br>
                    <input type="submit">
                    </form>
                    <br>%s''' % (email_address, signout_link_html))
    def post(self):
        user = users.get_current_user()
        self.response.write('You are now logged in!')
        self.response.write('''<a href="%s">Sign Out</a>'''% users.create_logout_url('/'))
        cssi_user = User(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            college=self.request.get('college'),
            id=user.user_id())
        cssi_user.put()
        self.response.write('Thanks for signing up, %s %s! You go to %s' % (cssi_user.first_name, cssi_user.last_name, cssi_user.college))
class BooksPage(webapp2.RequestHandler):
    def get(self):
        books_template = the_jinja_environment.get_template('templates/books.html')
        self.response.write(books_template.render())

class StressedPage(webapp2.RequestHandler):
    def get(self):
        stressed_template = the_jinja_environment.get_template('templates/stressed.html')
        self.response.write(stressed_template.render())

class MuseumsPage(webapp2.RequestHandler):
    def get(self):
        museums_template = the_jinja_environment.get_template('templates/museums.html')
        self.response.write(museums_template.render())

class TechnologyPage(webapp2.RequestHandler):
    def get(self):
        technology_template = the_jinja_environment.get_template('templates/technology.html')
        self.response.write(technology_template.render())

class ShoppingPage(webapp2.RequestHandler):
    def get(self):
        shopping_template = the_jinja_environment.get_template('templates/shopping.html')
        self.response.write(shopping_template.render())

class DormPage(webapp2.RequestHandler):
    def get(self):
        dorm_template = the_jinja_environment.get_template('templates/dorm.html')
        self.response.write(dorm_template.render())

class ClothesPage(webapp2.RequestHandler):
    def get(self):
        clothes_template = the_jinja_environment.get_template('templates/clothes.html')
        self.response.write(clothes_template.render())

class LaptopPage(webapp2.RequestHandler):
    def get(self):
        laptop_template = the_jinja_environment.get_template('templates/laptop.html')
        self.response.write(laptop_template.render())

class SpecificEventPage(webapp2.RequestHandler):
    def get(self):
        event_template = the_jinja_environment.get_template('templates/event.html')

class MusicPage(webapp2.RequestHandler):
    def get(self):
        music_template = the_jinja_environment.get_template('templates/music.html')
        self.response.write(music_template.render())

class MeditationPage(webapp2.RequestHandler):
    def get(self):
        meditation_template = the_jinja_environment.get_template('templates/meditation.html')
        self.response.write(meditation_template.render())

class SportPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        sport_template = the_jinja_environment.get_template('templates/sport.html')
        self.response.write(sport_template.render(temp_dict))

class ComedyPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        comedy_template = the_jinja_environment.get_template('templates/comedy.html')
        self.response.write(comedy_template.render(temp_dict))

class FoodPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        food_template = the_jinja_environment.get_template('templates/food.html')
        self.response.write(food_template.render(temp_dict))

class FestivalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        festival_template = the_jinja_environment.get_template('templates/festival.html')
        self.response.write(festival_template.render(temp_dict))

class ConcertPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        concert_template = the_jinja_environment.get_template('templates/concert.html')
        self.response.write(concert_template.render(temp_dict))

class TheaterPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        theater_template = the_jinja_environment.get_template('templates/theater.html')
        self.response.write(theater_template.render(temp_dict))

class AttractionsPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        attractions_template= the_jinja_environment.get_template('templates/attractions.html')
        self.response.write(attractions_template.render(temp_dict))

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/discounts', DiscountPage),
    ('/events', EventsPage),
    ('/login', LoginPage),
    ('/books', BooksPage),
    ('/stressed', StressedPage),
    ('/museums', MuseumsPage),
    ('/technology',TechnologyPage),
    ('/shopping', ShoppingPage),
    ('/dorm', DormPage),
    ('/clothes', ClothesPage),
    ('/laptop',LaptopPage),
    ('/music', MusicPage),
    ('/meditation', MeditationPage),
    ('/events/sport', SportPage),
    ('/events/comedy', ComedyPage),
    ('/events/food', FoodPage),
    ('/events/festival', FestivalPage),
    ('/events/music', ConcertPage),
    ('/events/theater', TheaterPage),
    ('/events/attractions', AttractionsPage)
], debug=True)
