## Marks Mazeiko
from pyfiglet import Figlet  
import random

def generate_congratulation():
    
    print("🎉 Personīgais apsveikuma ģenerators 🎉")
    
   
    name = input("Vards: ").strip().title()
    date = input("Datums: ")
    color = input("Milaka krasa (sarkana/zila/zala): ").lower()
    
   
    holiday = random.choice([
        "Dzimsanas dienu", "Jauno gadu", "8 Martu", 
        "23 Februari", "Programesanas dienu"
    ])
    
    
    styles = {
        "sarkana": ("red", "❤️"), 
        "zila": ("blue", "💙"), 
        "zala": ("green", "💚")
    }
    
    color_code, emoji = styles.get(color, ("yellow", "✨"))
   
    f = Figlet(font='slant')
    ascii_art = f.renderText(f"Apsveicu, {name}!")
    
   
    filename = f"apsveicu.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"""
{ascii_art}
Ar {holiday}!
{emoji} {date} {emoji}

<3
""")
    
    print(f"\n Saglabats faila '{filename}'!")


if __name__ == "__main__":
    generate_congratulation()