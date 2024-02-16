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

# Example usage
page_title = "Entrepreneurship"
full_content = get_full_page(page_title)
filename = f"{page_title}_Wikipedia_Page.txt"

# Save the content to a file
with open(filename, "w", encoding="utf-8") as file:
    file.write(full_content)

print(f"Full page content saved to {filename}")
