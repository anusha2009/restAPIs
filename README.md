# restAPIs

Activate the virtual environment:

source venv/bin/activate

Start the Flask server:

python3 app.py

Endpoints
GET /offers: Retrieve all offers from the stocklist.
GET /offers/<offer_id>: Delete the offer with the specified offer ID.
Parameters:
offer_id: Identifier of the offer to delete (barcode or articleEAN).
