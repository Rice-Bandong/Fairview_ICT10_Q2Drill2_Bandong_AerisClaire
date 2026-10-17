from pyscript import document

# Grade level sets 
grade8 = {'Jordin San Juan', 'Elina Elysse Padre', 'Savanah Fugueroa'}
grade9 = {'Franshellyahna Pilao', 'Kyrie Cerise Funtanilla', 'Antoinette Caleigh Garcia', 'Julianna Omaking'}
grade10 = {'Aeris Bandong', 'Vyelle Mikayla Bunag', 'Gavin Ghonn Taguiga', 'Hans Arada'}
grade11 = {'Alexi Villanueva', 'Dannielle Luna Dimasuhid', 'Ebtisam A. Al Hazmi', 'Marley Summer Reyes Manese', 'Queeny Haraj Guilas Ramos'}
grade12 = {'Maia Isabelle Fabro', 'Erin Mandapat', 'Maria Elisha Padre', 'Nica Gabriela Crispino'}

def add_member(event):
    # Get input 
    first_name = document.getElementById('fname').value.strip()
    last_name = document.getElementById('lname').value.strip()
   
    # Create new member set
    new_member = {f"{first_name} {last_name}"}
    
    # Combine all sets using union
    all_members = grade8 | grade9 | grade10 | grade11 | grade12 | new_member
    
    # Sort and join with line breaks
    members_list = "<br>".join(sorted(all_members))
    
    # Get total count
    total_members = len(all_members)
    
    # Show results on the webpage
    document.getElementById('output1').innerHTML = f"ALL MEMBERS:<br>{members_list}<br><br>TOTAL MEMBERS: {total_members}"