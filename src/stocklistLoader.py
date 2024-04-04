import csv
import xml.etree.ElementTree as ET

# Function to load Stocklist data from a CSV file
def load_stocklist_csv(file_path):
    stocklist = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if 'Variant Barcode' in row and 'Variant Price' in row and 'Variant Inventory Quantity' in row:
                # Normalize CSV data
                product_title = row.get('Product Title', '')
                variant_price = float(row.get('Variant Price', 0))
                variant_sku = row.get('Variant Sku', '')
                variant_barcode = row.get('Variant Barcode', '')
                variant_quantity = int(row.get('Variant Inventory Quantity', 0))
                pack_size = row.get('Product.custom.pack_size', '')
                
                stocklist.append({
                    'product_title': product_title,
                    'variant_price': variant_price,
                    'variant_sku': variant_sku,
                    'variant_barcode': variant_barcode,
                    'variant_quantity': variant_quantity,
                    'pack_size': pack_size
                })
    return stocklist

# Function to load Stocklist data from an XML file
def load_stocklist_xml(file_path):
    stocklist = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    for article in root.findall('items/item'):
        # Normalize XML data
        article_ean = article.find('articleEAN').text
        article_id = article.find('articleId').text
        brand = article.find('brand').text
        portfolio = article.find('portfolio').text
        article_name = article_name = article.find('articleName').text
        volume = float(article.find('volume').text)
        price_without_vat = float(article.find('priceWithoutVat').text)
        currency = article.find('currency').text
        stock_quantity = int(article.find('stockQuantity').text)

        if article_ean is not None and price_without_vat is not None and stock_quantity is not None:
        
            stocklist.append({
                'article_ean': article_ean,
                'article_id': article_id,
                'brand': brand,
                'portfolio': portfolio,
                'article_name': article_name,
                'volume': volume,
                'price_without_vat': price_without_vat,
                'currency': currency,
                'stock_quantity': stock_quantity
            })
    return stocklist

# Function to load Stocklist data from either CSV or XML file based on file extension
def load_stocklist(file_path):
    if file_path.endswith('.csv'):
        return load_stocklist_csv(file_path)
    elif file_path.endswith('.xml'):
        return load_stocklist_xml(file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and XML files are supported.")

#General testing
if __name__ == "__main__":
    file_path_csv = '../data/sample_cosmetics_stocklist.csv'  
    file_path_xml = '../data/wholesale-feed.xml' 
    
    stocklist_data_csv = load_stocklist(file_path_csv)
    if stocklist_data_csv:
        print("Stocklist (CSV) loaded successfully:")
        ##print(stocklist_data_csv)
    else:
        print("Failed to load Stocklist (CSV).")
    
    stocklist_data_xml = load_stocklist(file_path_xml)
    if stocklist_data_xml:
        print("Stocklist (XML) loaded successfully:")
        ##print(stocklist_data_xml)
    else:
        print("Failed to load Stocklist (XML).")