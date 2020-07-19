from backend import listing, volunteer, person

from json import dumps
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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
def volunteerCreate():
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
	return dumps(listing.getLocation(request.args.get('listing_id')))

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
	app.run()