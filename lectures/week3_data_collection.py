import requests
import pandas as pd
from joblib import Parallel, delayed
from tqdm import tqdm
import time

#############################################
# UTILITY FUNCTIONS
#############################################

def batch_list(lst, batch_size):
    """Yield successive chunks of size batch_size from lst."""
    for i in range(0, len(lst), batch_size):
        yield lst[i:i+batch_size]

#############################################
# API FETCH FUNCTIONS
#############################################

def fetch_works_for_batch(author_ids, filter_params="", per_page=200, sleep_time=0.2):
    """
    Fetch works from OpenAlex for a batch of author IDs.
    
    Parameters:
      - author_ids: list of author OpenAlex IDs (e.g. "https://openalex.org/A123456789")
      - filter_params: additional filter string (e.g. "cited_by_count:>10,authorship_count:<10")
      - per_page: number of works per page (max 200)
      - sleep_time: pause between pages (to respect rate limits)
      
    Returns:
      - List of work dictionaries.
    """
    works_endpoint = "https://api.openalex.org/works"
    all_works = []
    # Build filter for author IDs (using the OR operator "|")
    author_filter = "authorships.author.id:" + "|".join(author_ids)
    full_filter = author_filter + ("," + filter_params if filter_params else "")
    
    cursor = "*"
    while True:
        params = {
            "filter": full_filter,
            "per_page": per_page,
            "cursor": cursor,
            "select": "id,publication_year,cited_by_count,authorships,abstract_inverted_index,title,concepts"
        }
        response = requests.get(works_endpoint, params=params)
        if response.status_code != 200:
            print(f"Error fetching works for authors {author_ids}: {response.status_code}")
            break
        data = response.json()
        results = data.get("results", [])
        all_works.extend(results)
        meta = data.get("meta", {})
        next_cursor = meta.get("next_cursor")
        if not next_cursor:
            break
        cursor = next_cursor
        time.sleep(sleep_time)
    return all_works

def fetch_works_for_authors(author_ids, filter_params="", batch_size=25, n_jobs=5):
    """
    Given a list of author IDs, split them into batches and fetch works in parallel.
    
    Returns:
      - List of work dictionaries.
    """
    batches = list(batch_list(author_ids, batch_size))
    results = Parallel(n_jobs=n_jobs)(
        delayed(fetch_works_for_batch)(batch, filter_params) for batch in tqdm(batches, desc="Fetching works for authors")
    )
    # Flatten list of lists
    all_works = [work for sublist in results for work in sublist]
    return all_works

ic2s2_authors_df = pd.read_csv("files/researchers_data_2024.csv")
    
# Filter authors with works_count between 5 and 5000
ic2s2_authors_df = ic2s2_authors_df[(ic2s2_authors_df["Works Count"] >= 5) & (ic2s2_authors_df["Works Count"] <= 5000)]
ic2s2_author_ids = ic2s2_authors_df["ID"].tolist()
ic2s2_author_ids = [author_id.split("org/")[1] for author_id in ic2s2_author_ids]

all_works = fetch_works_for_authors(ic2s2_author_ids, filter_params="cited_by_count:>10", batch_size=25, n_jobs=5)
print(f"Total works fetched for IC2S2 authors: {len(all_works)}")

all_works_filtered = [work for work in all_works if len(work["authorships"]) > 10]
print(f"Total works fetched for IC2S2 authors: {len(all_works_filtered)}")

def filter_works_by_concepts(works, css_concepts, quantitative_concepts):
    """
    Filter works to include only those that have at least one level-0 concept 
    from each of the following groups:
      - Computational Social Science: e.g. Sociology, Psychology, Economics, Political Science
      - Quantitative disciplines: e.g. Mathematics, Physics, Computer Science
    """
    filtered = []
    # Pre-lowercase the concept names for easier comparison
    css_concepts_lower = [c.lower() for c in css_concepts]
    quantitative_concepts_lower = [q.lower() for q in quantitative_concepts]
    
    for work in works:
        concepts = work.get("concepts", [])
        css_found = False
        quantitative_found = False
        for concept in concepts:
            if concept.get("level") == 0:
                name = concept.get("display_name", "").lower()
                if name in css_concepts_lower:
                    css_found = True
                if name in quantitative_concepts_lower:
                    quantitative_found = True
        if css_found and quantitative_found:
            filtered.append(work)
    return filtered

css_concepts = ["Sociology", "Psychology", "Economics", "Political Science"]
quantitative_concepts = ["Mathematics", "Physics", "Computer Science"]
filtered_works = filter_works_by_concepts(all_works_filtered, css_concepts, quantitative_concepts)
print(f"Total works after concept filtering: {len(filtered_works)}")

ic2s2_papers = []
ic2s2_abstracts = []

for work in filtered_works:
    # Extract author IDs from the "authorships" field
    authors = [auth.get("author", {}).get("id") for auth in work.get("authorships", []) if auth.get("author", {}).get("id")]
    ic2s2_papers.append({
        "id": work.get("id"),
        "publication_year": work.get("publication_year"),
        "cited_by_count": work.get("cited_by_count"),
        "author_ids": authors
    })
    ic2s2_abstracts.append({
        "id": work.get("id"),
        "title": work.get("title"),
        "abstract_inverted_index": work.get("abstract_inverted_index")
    })

ic2s2_papers_df = pd.DataFrame(ic2s2_papers)
ic2s2_abstracts_df = pd.DataFrame(ic2s2_abstracts)

ic2s2_papers_df.to_csv("ic2s2_papers.csv", index=False)
ic2s2_abstracts_df.to_csv("ic2s2_abstracts.csv", index=False)

import ast
ic2s2_authors_df = ic2s2_authors_df[(ic2s2_authors_df["Works Count"] >= 5) & (ic2s2_authors_df["Works Count"] <= 5000)]
ic2s2_author_ids = ic2s2_authors_df["ID"].tolist()

ic2s2_papers_df = pd.read_csv("files/ic2s2_papers.csv")
ic2s2_papers = ic2s2_papers_df.to_dict(orient='records')
for paper in ic2s2_papers:
    if isinstance(paper['author_ids'], str):
        paper['author_ids'] = ast.literal_eval(paper['author_ids'])
len(ic2s2_author_ids)

all_author_ids_in_works = set()
for paper in ic2s2_papers:
    for aid in paper["author_ids"]:
        all_author_ids_in_works.add(aid)

# Identify co-author IDs by removing the IC2S2 authors
ic2s2_author_ids_set = set(ic2s2_author_ids)
coauthor_ids = list(all_author_ids_in_works - ic2s2_author_ids_set)
coauthor_ids = [author_id.split("org/")[1] for author_id in coauthor_ids]
print(f"Total unique co-author IDs: {len(coauthor_ids)}")

ic2s2_authors_df = ic2s2_authors_df[(ic2s2_authors_df["Works Count"] >= 5) & (ic2s2_authors_df["Works Count"] <= 5000)]
len(ic2s2_author_ids)

URL = "https://api.openalex.org/authors"
coauthors_data = []

# Use a session to reuse connections
with requests.Session() as session:
    for id in coauthor_ids:
        params = {
            "select": "id,display_name,works_api_url,summary_stats,works_count,last_known_institutions"
        }
        
        response = session.get(URL + f"/{id}", params=params)
        
        if response.status_code == 200:
            results = response.json()
            if results:
                result = results
                author_id = result.get('id', '')
                display_name = result.get('display_name', '')
                works_api_url = result.get('works_api_url', '')
                works_count = result.get('works_count', 0)
                h_index = result.get('summary_stats', 0).get('h_index', 0)
                country_code = result.get('last_known_institutions', '')
                if country_code:
                    country_code = country_code[0].get('country_code', '')

                # Append to list
                coauthors_data.append({
                    "ID": author_id,
                    "Name": display_name,
                    "Works API URL": works_api_url,
                    "Works Count": works_count,
                    "H-Index": h_index,
                    "Country Code": country_code
                })
            else:
                print(f"Error fetching data for {id}")
        else:
            print(f"Error fetching data for {id}: {response.status_code}")

# -------------------------------
# STEP 4: Store the Data
# -------------------------------
coauthors_df = pd.DataFrame(coauthors_data)
coauthors_df.to_csv("files/ic2s2_coauthors.csv", index=False)
print(f"Fetched data for {len(coauthors_data)} co-authors.")

ic2s2_coauthors_df = pd.read_csv("files/ic2s2_coauthors.csv")
print(len(ic2s2_coauthors_df))
ic2s2_coauthors_df = ic2s2_coauthors_df[(ic2s2_coauthors_df["Works Count"] >= 5) & (ic2s2_coauthors_df["Works Count"] <= 5000)]
ic2s2_coauthor_ids = ic2s2_coauthors_df["ID"].tolist()
ic2s2_coauthor_ids = [author_id.split("org/")[1] for author_id in ic2s2_coauthor_ids]
len(ic2s2_coauthor_ids)

coauthor_ids_set = set(ic2s2_coauthor_ids)
author_ids_set = set([author_id.split("org/")[1] for author_id in ic2s2_author_ids])
allowed_authors = author_ids_set.union(coauthor_ids_set)
len(coauthor_ids_set), len(author_ids_set), len(allowed_authors)

coauthor_ids_1 = ic2s2_coauthor_ids[:3100]
coauthor_ids_2 = ic2s2_coauthor_ids[3100:6200]
coauthor_ids_3 = ic2s2_coauthor_ids[6200:]

all_coauthor_works_1 = fetch_works_for_authors(coauthor_ids_1, filter_params="cited_by_count:>10", batch_size=25, n_jobs=5)
print(f"Total works fetched for IC2S2 authors: {len(all_coauthor_works_1)}")

all_coauthor_works_2 = fetch_works_for_authors(coauthor_ids_2, filter_params="cited_by_count:>10", batch_size=25, n_jobs=5)
print(f"Total works fetched for IC2S2 authors: {len(all_coauthor_works_2)}")

all_coauthor_works_3 = fetch_works_for_authors(coauthor_ids_3, filter_params="cited_by_count:>10", batch_size=25, n_jobs=5)
print(f"Total works fetched for IC2S2 authors: {len(all_coauthor_works_3)}")

all_coauthor_works = []
all_coauthor_works.extend(all_coauthor_works_1)
all_coauthor_works.extend(all_coauthor_works_2)
all_coauthor_works.extend(all_coauthor_works_3)

# filter out works with more than 10 authors
all_coauthor_works_filtered = [work for work in all_coauthor_works if len(work["authorships"]) > 10]
print(f"Total works fetched for IC2S2 authors: {len(all_coauthor_works_filtered)}")

# filter by concept
css_concepts = ["Sociology", "Psychology", "Economics", "Political Science"]
quantitative_concepts = ["Mathematics", "Physics", "Computer Science"]
filtered_coauthor_works = filter_works_by_concepts(all_coauthor_works_filtered, css_concepts, quantitative_concepts)
print(f"Total works after concept filtering: {len(filtered_coauthor_works)}")

ic2s2_coauthors_papers = []
ic2s2_coauthors_abstracts = []

for work in filtered_coauthor_works:
    # Extract author IDs from the "authorships" field
    authors = [auth.get("author", {}).get("id") for auth in work.get("authorships", []) if auth.get("author", {}).get("id")]
    ic2s2_coauthors_papers.append({
        "id": work.get("id"),
        "publication_year": work.get("publication_year"),
        "cited_by_count": work.get("cited_by_count"),
        "author_ids": authors
    })
    ic2s2_coauthors_abstracts.append({
        "id": work.get("id"),
        "title": work.get("title"),
        "abstract_inverted_index": work.get("abstract_inverted_index")
    })