import wikipedia
import re
from utils.logger import log_info, log_error


def get_wiki_pages(query: str, count: int=5, lang: str="de") -> list:
    if not query:
        return []
    try:
        wikipedia.set_lang(lang)
        results = wikipedia.search(query, results=count)
        log_info(f"Executed Wikipedia search, found {len(results)} pages for topic '{query}' and language '{lang}': {results}")
        return results
    except Exception as e:
        return [f"Error while searching the Wikipedia pages for topic '{query}' and language '{lang}': {e}"]

def get_content_for_wiki_page(title: str, lang: str="de") -> str:
    try:
        wikipedia.set_lang(lang)
        page = wikipedia.page(title, auto_suggest=False)
        text = page.content
        text = re.sub(r"==+.*?==+", "", text)
        text = re.sub(r"\n\s*\n+", "\n\n", text.strip())
        return text.strip()
    except Exception as e:
        return f"Error while loading the Wikipedia page '{title}' for language '{lang}': {e}"

def query_wikipedia(topic: str, language: str) -> str:
    try:
        pages = get_wiki_pages(topic, 1, language)
        if not pages:
            log_error(f"Page for topic '{topic}' not found")
            return f"Page for topic '{topic}' not found"

        return get_content_for_wiki_page(pages[0], language)

    except Exception as e:
        log_error(str(e))
        return f"Something went wrong: {e}"