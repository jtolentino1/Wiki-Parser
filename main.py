import sys
import requests

def get_full_page(title):
    ENDPOINT = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True, 
        "exsectionformat": "plain"  
    }
    response = requests.get(ENDPOINT, params=params)
    pages = response.json().get('query', {}).get('pages', {})
    if pages:
        page = next(iter(pages.values()))  # Get the first page in the response
        if 'extract' in page:
            return page['extract']
    return "Content not found or unable to retrieve full content."

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 main.py -s <searchTerm> -o <textFileName>")
        sys.exit(1)

    # Initialize variables
    search_term = ""
    text_file_name = ""

    # Parse command line arguments
    for i in range(1, len(sys.argv)-1):
        if sys.argv[i] == "-s":
            search_term = sys.argv[i+1]
        elif sys.argv[i] == "-o":
            text_file_name = sys.argv[i+1]

    if search_term == "" or text_file_name == "":
        print("Missing required arguments. Usage: python3 main.py -s <searchTerm> -o <textFileName>")
        sys.exit(1)

    # Retrieve the full page content based on the search term
    full_content = get_full_page(search_term)

    # Save the content to the specified file
    with open(text_file_name, "w", encoding="utf-8") as file:
        file.write(full_content)

    print(f"Full page content saved to {text_file_name}")
