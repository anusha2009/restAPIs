from flask import Flask, jsonify, request
from stocklistLoader import load_stocklist

app = Flask(__name__)

#Combine the data from CSV and XML files
def combine_offers():
    file_path_csv = '../data/sample_cosmetics_stocklist.csv'  
    file_path_xml = '../data/wholesale-feed.xml' 
    
    stocklist_data_csv = load_stocklist(file_path_csv)
    if stocklist_data_csv:
        print("Stocklist (CSV) loaded successfully:")
    else:
        print("Failed to load Stocklist (CSV).")
    
    stocklist_data_xml = load_stocklist(file_path_xml)
    if stocklist_data_xml:
        print("Stocklist (XML) loaded successfully:")
    else:
        print("Failed to load Stocklist (XML).")
    
    # Combine CSV and XML data
    combined_stocklist_data = {'sample_cosmetics': stocklist_data_csv, 'wholesale_feed': stocklist_data_xml}
    
    return combined_stocklist_data

combined_stocklist_data = combine_offers()

#Return the combines data
@app.route('/offers', methods=['GET'])
def get_offers():
    
    return jsonify(combined_stocklist_data)

#Delete offer from the combined data
@app.route('/offers/<offer_id>', methods=['GET'])
def delete_offer(offer_id):

    # Check if identifier is barcode or articleEAN and delete corresponding offer
    for offer in combined_stocklist_data['sample_cosmetics']:
        if offer.get('variant_barcode') == offer_id:
            combined_stocklist_data['sample_cosmetics'].remove(offer)
            return jsonify({'message': f'Offer with {offer_id} deleted successfully'}), 200
    
    for offer in combined_stocklist_data['wholesale_feed']:
        if offer.get('article_ean') == offer_id:
            combined_stocklist_data['wholesale_feed'].remove(offer)
            return jsonify({'message': f'Offer with {offer_id} deleted successfully'}), 200
    
    return jsonify({'error': f'Offer with {offer_id} not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
