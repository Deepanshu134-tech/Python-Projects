import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def scrape_books(base_url):
    # Create a session
    session = requests.Session()
    
    # Set headers to mimic a browser visit
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    current_page = base_url
    all_books = []
    
    while current_page:
        print(f"Scraping page: {current_page}")
        
        # Get the page content
        response = session.get(current_page, headers=headers)
        
        # Check if request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve page: {current_page}")
            break
            
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all book containers
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            # Extract book details
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text[1:]  # Remove £ symbol
            rating = book.p['class'][1]  # e.g., 'Three' for 3-star rating
            availability = book.find('p', class_='instock availability').text.strip()  # Availability status

            
            # Get the full URL for the book page
            book_url = urljoin(base_url, book.h3.a['href'])
            
            # Visit the book page to get more details
            book_response = session.get(book_url, headers=headers)
            if book_response.status_code == 200:
                book_soup = BeautifulSoup(book_response.text, 'html.parser')
                # Extract additional details
                description = book_soup.find('meta', attrs={'name': 'description'})['content'].strip()
                upc = book_soup.find('th', string='UPC').find_next_sibling('td').text
                product_type = book_soup.find('th', string='Product Type').find_next_sibling('td').text
                price_excl_tax = book_soup.find('th', string='Price (excl. tax)').find_next_sibling('td').text[1:]
                price_incl_tax = book_soup.find('th', string='Price (incl. tax)').find_next_sibling('td').text[1:]
                tax = book_soup.find('th', string='Tax').find_next_sibling('td').text[1:]
                num_reviews = book_soup.find('th', string='Number of reviews').find_next_sibling('td').text

            else:
                description = upc = product_type = price_excl_tax = price_incl_tax = tax = num_reviews = "N/A"
            
            # Add book data to list
            all_books.append({
                'title': title,
                'price': price,
                'rating': rating,
                'availability': availability,
                'url': book_url,
                'description': description,
                'upc': upc,
                'product_type': product_type,
                'price_excl_tax': price_excl_tax,
                'price_incl_tax': price_incl_tax,
                'tax': tax,
                'num_reviews': num_reviews
            })
        
        # Check for next page
        next_button = soup.find('li', class_='next')
        if next_button:
            next_page = next_button.a['href']
            current_page = urljoin(current_page, next_page)
        else:
            current_page = None
    
    return all_books

def save_to_csv(books, filename):
    if not books:
        print("No books to save.")
        return
        
    keys = books[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(books)
    
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    base_url = "http://books.toscrape.com/"
    print("Starting web scraping...")
    books_data = scrape_books(base_url)
    save_to_csv(books_data, 'books_data.csv')
    print(f"Scraping complete. {len(books_data)} books scraped.")
