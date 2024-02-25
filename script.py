
import os
import bs4
import requests
import re
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
            return folder_path
        except OSError as e:
            print(f"Error creating folder '{folder_path}': {e}")
    else:
        print(f"Folder '{folder_path}' already exists.")

def download(j,k):
    i = 1
    while i<int(k):
        with open(f"{i}.jpg", "wb") as f:
            try:
                f.write(requests.get(j[:j.rfind('.')-1] + f"{i}" + j[j.rfind('.'):]).content)
                i+=1
            except Exception as e:
                print(e)
                break
"109969"
ip = input("Enter 6-digitnumber")  

get_html = requests.get(f"https://www.nhentai.net/g/{ip}/1/")
soup = bs4.BeautifulSoup(get_html.text,'html.parser')
print(soup)
re_obj = re.compile(r"https?://\S+\.webp\b")

for i  in soup.section.find_all('a'):
    obj = i.attrs
    if obj['class'] == ['last']:
        ref = obj['href']
        print(os.getcwd())
        os.chdir(os.path.join('/home/arvind/Documents/Mangas'))
        p = create_folder(os.getcwd()+f"/{ip}")
        os.chdir(os.path.join(p))
        download(re_obj.findall(str(soup))[0],ref[10:ref.rfind('/')])

