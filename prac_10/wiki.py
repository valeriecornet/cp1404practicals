"""Wiki summary"""

import wikipedia
from wikipedia import DisambiguationError, PageError

wiki_prompt = input("Enter page title or search phrase: ")
while wiki_prompt != "":
    # Search wikipedia
    wikipedia.search(wiki_prompt)
    # Print summary of the page
    try:
        wiki_summary = wikipedia.summary(wiki_prompt)
        wiki_page = wikipedia.page(wiki_prompt, auto_suggest = False)
        print("Title: {}".format(wiki_page.title))
        print("Summary: {}".format(wiki_summary))
        print("URL: {}".format(wiki_page.url))
    except DisambiguationError:
        print("Disambiguation Error")
        print(DisambiguationError.options)
    except PageError:
        print("Page Error")
    wiki_prompt = input("Enter page title or search phrase: ")
