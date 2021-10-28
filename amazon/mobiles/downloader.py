
import urllib.request    

links_file = open('links' , 'r')
links = links_file.readlines()
print(links)
i = 0
for link in links:
    try:
        urllib.request.urlretrieve(link, f"htmls/data{i}.html")
        print("saved done")
    except:
        try:
            urllib.request.urlretrieve(link, f"htmls/data{i}.html")
            print("saved done")
        except:
            print("something went wrong")
        
    i += 1