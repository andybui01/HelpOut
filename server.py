from backend import listing
from flask import Flask, request
app = Flask(__name__)


@app.route('/listing/title', methods=["GET"])
def listingTitle():
	return dumps(listing.getTitle(request.form.get('listing_id')))
	
@app.route('/listing/desc', methods=["GET"])
def listingDesc():
	return dumps(listing.getDesc(request.form.get('listing_id')))

@app.route('listing/create', methods=["POST"])
def listingCreate():
	return dumps(listing.createListing(
		request.form.get('title'),
		request.form.get('desc'),
		request.form.get('commitment'),
		request.form.get('location')
		))

if __name__ == '__main__':
	app.run()