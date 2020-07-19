from backend import listing, volunteer, person

from json import dumps
import sys
from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

'''Pages'''
@app.route("/")
def start():
	return redirect(url_for('homePage'))

@app.route("/homePage", methods=["GET", "POST"])
def homePage():
	return render_template('home.html')

@app.route("/volunteerPage", methods=["GET", "POST"])
def volunteerPage():
	allListings = listing.sortListing("5", "Kensington")
	return render_template('volunteer.html', test = allListings)

@app.route("/reviewPage", methods=["GET", "POST"])
def reviewPage():
	volunteerDetails = {
	"name" : "James",
	"contact" : "0401010101",
	"number" : "10",
	"badges" : "Fast"}
	return render_template('review.html', **volunteerDetails)

""" Person """
@app.route('/person/name', methods=["GET"])
def personName():
	return dumps(person.getName(request.args.get('person_id')))

@app.route('/person/contact', methods=["GET"])
def personContact():
	return dumps(person.getContact(request.args.get('person_id')))

@app.route('/person/create', methods=["POST"])
def personCreate():
	return dumps(person.createPerson(
		request.form.get('person_id'),
		request.form.get('name'),
		request.form.get('contact')
		))

""" Volunteer """
@app.route('/volunteer/name', methods=["GET"])
def volunteerName():
	return dumps(volunteer.getName(request.args.get('volunteer_id')))

@app.route('/volunteer/contact', methods=["GET"])
def volunteerContact():
	return dumps(volunteer.getContact(request.args.get('volunteer_id')))

@app.route('/volunteer/completed', methods=["GET"])
def volunteerCompleted():
	return dumps(volunteer.getNumberCompleted(request.args.get('volunteer_id')))

@app.route('/volunteer/badges', methods=["GET"])
def volunteerBadges():
	return dumps(volunteer.getBadges(request.args.get('volunteer_id')))

@app.route('/volunteer/create', methods=["POST"])
def listingCreate2():
	return dumps(volunteer.createVolunteering(
		request.form.get('volunteer_id'),
		request.form.get('name'),
		request.form.get('contact')
		))

""" Listings """
@app.route('/listing/title', methods=["GET"])
def listingTitle():
	return dumps(listing.getTitle(request.args.get('listing_id')))
	
@app.route('/listing/desc', methods=["GET"])
def listingDesc():
	return dumps(listing.getDesc(request.args.get('listing_id')))

@app.route('/listing/commitment', methods=["GET"])
def listingCommitment():
	return dumps(listing.getCommitment(request.args.get('listing_id')))

@app.route('/listing/location', methods=["GET"])
def listingLocation():
	return dumps(listing.getLocation(request.args.get('listing_location')))

@app.route('/listings', methods=["GET"])
def listings():
	return dumps(listing.sortListing(request.args.get('num'), request.args.get('suburb')))

@app.route('/listing/create', methods=["POST"])
def listingCreate():
	return dumps(listing.createListing(
		request.form.get('personID'),
		request.form.get('title'),
		request.form.get('desc'),
		request.form.get('commitment'),
		request.form.get('location')
		))

if __name__ == '__main__':
	app.run(debug=True, port = 8000)