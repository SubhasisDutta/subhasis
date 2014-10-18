import webapp2
from src.controller.HomeContoller import HomePage
from src.controller.SliderController import SliderWS

application = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/sliderdata',SliderWS)    
], debug=True)

"""def main():
    run_wsgi_app(subhasisapp)
    
if __name__== "__main__":
    main()"""