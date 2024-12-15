import arxiv
from deep_translator import GoogleTranslator


client = arxiv.Client()
translator = GoogleTranslator(source="auto", target="ru")

# topic = "Artificial Intelligence"
topic = "Crypto"
top_k = 10

# Lates
search = arxiv.Search(
    query=topic, max_results=top_k, sort_by=arxiv.SortCriterion.SubmittedDate
)

# # Relevance
# search = arxiv.Search(
#     query=topic, max_results=top_k, sort_by=arxiv.SortCriterion.Relevance
# )

results = client.results(search)

for result in results:
    print(f"Title: {result.title}")
    print(f"Authors: {', '.join([author.name for author in result.authors])}")
    print(f"Date of publication: {result.published}")
    summary_translated = translator.translate(result.summary)
    print(f"Symmary: {summary_translated}")
    print(f"PDF: {result.pdf_url}")
    print("-" * 80)
