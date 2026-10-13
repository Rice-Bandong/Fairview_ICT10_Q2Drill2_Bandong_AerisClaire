from pyscript import document, display

grade8 = {'Jordin San Juan', 'Elina Elysse Padre', 'Savanah Fugueroa'}
grade9 = {'Franshellyahna Pilao', 'Kyrie Cerise Funtanilla', 'Antoinette Caleigh Garcia', 'Julianna Omaking'}
grade10 = {'Aeris Bandong', 'Vyelle Mikayla Bunag', 'Gavin Ghonn Taguiga', 'Hans Arada'}
grade11 = {'Alexi Villanueva', 'Dannielle Luna Dimasuhid', 'Ebtisam A. Al Hazmi', 'Marley Summer Reyes Manese', 'Queeny Haraj Guilas Ramos'}
grade12 = {'Maia Isabelle Fabro', 'Erin Mandapat', 'Maria Elisha Padre', 'Nica Gabriela Crispino'}

def add_member(event):
    
    first_name = document.getElementById('fname').value.strip().upper()
    last_name = document.getElementById('lname').value.strip().upper()
   
    new_member_set = {f"{first_name} {last_name}"}
    
    all_members_set = grade8 | grade9 | grade10 | grade11 | grade12 | new_member_set
    
    members_text = "\n".join(sorted(all_members_set))
    total_count = len(all_members_set)
    
    display(f"ALL MEMBERS:\n{members_text}\n\nTOTAL MEMBERS: {total_count}", target="output1", append=False)