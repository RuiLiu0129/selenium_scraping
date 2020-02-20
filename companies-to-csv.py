
from scrape_linkedin import CompanyScraper
import pandas as pd

# LIST YOUR COMPANIES HERE
my_company_list = ['sumitomo-mitsui-banking-corporation','facebook', 'linkedin','google']

company_data = []

with CompanyScraper(cookie='AQEDASgc_sYBUdX-AAABb2foSO0AAAFwfNSGnE4AVgMRkHBIlGE--Dsqwz4X-V4q_8YRMYCzXpOdVQqu6_LDEtnjvIuPauzu7JZ81QiPa5r2nCEWimHSJzLqaxt3uYBAuCQG6c2nNus2Lnt0GSsdh2iN') as scraper:
    # Get each company's overview, add to company_data list
    for name in my_company_list:
        overview = scraper.scrape(company=name).overview
        overview['company_name'] = name
        company_data.append(overview)

# Turn into dataframe for easy csv output
df = pd.DataFrame(company_data)
df.to_csv('out.csv', index=False)
