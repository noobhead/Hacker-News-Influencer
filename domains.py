#########
# Script to find What domains were submitted most often to Hacker News?
# This could help in choosing domains for writing the article in order for it to get submitted on Hacker News
##########

import pandas as pd 
from read import load_data
hn_stories = load_data()
domains = hn_stories["url"]
domain_dict = domains.value_counts()

# printing the top 100 most submitted domains 
#with pd.option_context('display.max_rows', 100, 'display.max_columns', None):
#    print(domain_dict)


# Making it more robust by removing the subdomains
def remove_subdomain(domain):
    inner_list = str(domain).split(".")
    if len(inner_list) >= 3:
        if ((inner_list[-2] == "co") or (inner_list[-2] == "com")):
            new_list = inner_list[-3:]
            new_domain = ".".join(new_list)
            return new_domain
        else:
            new_list = inner_list[-2:]
            new_domain = ".".join(new_list)
            return new_domain
    
    else:
        return domain
    
no_subdomain_domains = domains.apply(remove_subdomain)
no_subdomain_domain_dict = no_subdomain_domains.value_counts() 

# printing the top 100 most submitted domains 
with pd.option_context('display.max_rows', 100, 'display.max_columns', None):
    print(no_subdomain_domain_dict) 