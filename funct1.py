def search_by_keyword(data):
    keyword = input("Enter the keyword to search: ")
    results = []
    for item in data:
        if keyword.lower() in item.lower():
            results.append(item)
    return results

# Example usage
data = ["hilton", "hotel kyiv", "hotel holosiivskiy", "Radisson Blu Hotel", "Favor Park Hotel "]
search_results = search_by_keyword(data)
print(search_results)