import urllib.request
import re

base_url = "http://web.eecs.umich.edu/~radev/coursera-slides/"

html = urllib.request.urlopen(base_url)
html_contents = str(html.read().decode("utf8"))

url_list = re.findall(r"nlp[0-9a-zA-Z\_\.\]*\.pdf", html_contents)

for url in url_list:
    file_name = "".join(url)
    full_url = base_url + file_name
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url, file_name)
    print("End Download")
