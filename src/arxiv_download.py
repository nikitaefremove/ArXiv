import arxiv


paper_name = "GenEx: Generating an Explorable World"

paper = next(arxiv.Client().results(arxiv.Search(query=paper_name)))

paper.download_pdf(dirpath="Papers", filename=f"{paper_name}.pdf")
