import webapp2

form="""
<form method="post">
	When is your birthday?
	<br>
	<label> Month
		<input type="text" name="month">
	</label>
	<label> Day
		<input type="text" name="day">
	</label>
	<label> Year
		<input type="text" name="year">
	</label>
	<br>
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)