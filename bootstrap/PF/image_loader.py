import json
import shutil
from bs4 import BeautifulSoup as bs
import requests
import bs4

list_page = requests.get("https://pathfinder.fandom.com/wiki/List_of_monsters").text
soup = bs(list_page, 'html.parser')
all_monsters_file = open(r'bootstrap/PF/json/pf_monsters.json', 'r')
all_monsters = json.load(all_monsters_file)

for link in soup.table.descendants:
    if type(link) is bs4.element.Tag:
        if link.name == 'a':
            for monster in all_monsters:
                if monster['fields'].get('name') is not None:
                    if link.text.capitalize() in monster['fields'].get('name'):
                        monster_page = requests.get(rf"https://pathfinder.fandom.com/wiki/{link.text.capitalize()}").text
                        monster_image = bs(monster_page, 'html.parser').table
                        try: img_file = requests.get(monster_image.img['src'], stream=True)
                        except:
                            img_file = requests.get('https://images.generation-msx.nl/company/0388910c.png', stream=True)
                        if img_file.status_code == 200:
                            with open(rf"media/images/monsters/PathFinder1e/{monster['fields'].get('name')}.jpg", 'wb') as img_target:
                                shutil.copyfileobj(img_file.raw, img_target)
                                print(f"{monster['fields'].get('name')} image has been loaded")
                        else: print('Imagem não foi encontrada')
                    else:
                        img_file = requests.get('https://images.generation-msx.nl/company/0388910c.png', stream=True)
                        if img_file.status_code == 200:
                            if '/' not in monster['fields'].get('name'):
                                with open(rf"media/images/monsters/PathFinder1e/{monster['fields'].get('name')}.jpg",
                                          'wb') as img_target:
                                    shutil.copyfileobj(img_file.raw, img_target)
                                    print(f"{monster['fields'].get('name')} image has been loaded")
                            else:
                                string_index = 0
                                for char in monster['fields'].get('name'):
                                    if char == '/':
                                        string_index = monster['fields'].get('name').index(char)
                                        break
                                monster_name = monster['fields'].get('name')[:string_index]
                                with open(rf"media/images/monsters/PathFinder1e/{monster_name}.jpg",
                                          'wb') as img_target:
                                    shutil.copyfileobj(img_file.raw, img_target)
                                    print(f"{monster['fields'].get('name')} image has been loaded")
                        else:
                            print('Imagem não foi encontrada')
