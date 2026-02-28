from duckduckgo_search import DDGS

def search_editais_2(query, max_results=5):
    results_list = []
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        for r in results:
            results_list.append({
                "title": r["title"],
                "href": r["href"],
                "body": r["body"]
            })
    return results_list
