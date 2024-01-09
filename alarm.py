import time
import pygame
import tkinter as tk
from datetime import datetime

alarm_active = False

# Initialisation de Pygame pour la lecture audio
pygame.init()

# charger le son pour l'alarme
son_alarme = pygame.mixer.Sound("Fowuro sise.mp3")

def main():
    # utiliser l'interface utilisateur tkinter 
    # print(show_time())
    alarm_time = setting_alarm()
    if alarm_time:
        while True:
            action = input("Tapez 'a' pour activer ou desactiver l'alarm ou 'q' pour quitter: ")
            if action.lower() == 'a':
                alarm_status()
            elif action.lower() == 'q':
                break
            else:
                print("Commande invalide. Veuillez taper 'a' pour activer/desactiver l'alarme ou 'q' pour quitter")
            print(alarm_active)
        if alarm_active:
            raise_alarm(alarm_time)

def setting_alarm():
    # demander aux users d'entrer l'heure et la minute
    try:
        alarm_hours = int(input('Entrez l\'heure du reveille: '))
        alarm_minute = int(input('Entrez la minute du reveille: '))
        # alarm_hours = int(hours)
        # alarm_minute = int(minute)
    # verifier si l'heure et la minute sont valides
        if 0 <= alarm_hours <= 24 and 0 <= alarm_minute <= 60:
            # obtenir la date et l'heure du moment
            moment = datetime.now()
            # definir l'alarm pour le jour suivant si l'alarm est passe deja pour
            if moment.hour > alarm_hours or (moment.hour == alarm_hours and moment.minute >= alarm_minute):
                alarm = moment.replace(day=moment.day + 1, hour=alarm_hours, minute=alarm_minute, second=0, microsecond=0)
            else:
                alarm = moment.replace(hour=alarm_hours, minute=alarm_minute)
    # la difference entre l'alarme et maintenant
            difference = alarm - moment
    # afficher un message rappelant aux user le temps definir
            print(f'Alarme reglee pour {alarm_hours:02}:{alarm_minute:02}.\nElle sonnera dans {difference.seconds // 3600} heures et {(difference.seconds // 60) % 60} minutes')

            # label_info.config(text=f'Alarme reglee pour {alarm_hours:02}:{alarm_minute:02}.\nElle sonnera dans {difference.seconds // 3600} heures et {(difference.seconds // 60) % 60} minutes')

            return alarm
        else:
            print('heure ou minute invalide')
    except ValueError:
        print("Valeurs Invalides")


def raise_alarm(alarm_time):
    while True:
        moment = datetime.now()
        # veifier si l'heure actuelle correspond a l'heure de l'alarm
        if moment.hour == alarm_time.hour and moment.minute == alarm_time.minute:
            print('Alarm!')
            
            try:
                son_alarme.play()
                pygame.time.wait(int(son_alarme.get_length() * 1000))
                pygame.quit()
            except pygame.error as e:
                print(f"Erreur lors de la lecture du son: {e}")
            
            break
        time.sleep(10)

def alarm_status():
    global alarm_active
    alarm_active = not alarm_active
    if alarm_active:
        print("Alarm activee")
    else:
        print("Alarm desactivee")

def show_time():
    moment = datetime.now().time().isoformat(timespec='minutes')
    return moment



# definir l'interface utilisateur
# root = tk.Tk()
# root.title('Alarm Clock')

# label_time = tk.Label(root, text=show_time())
# label_time.pack()

# moment = {}

# creer une fonction pour definir l'etat de l'alarme
# def choose_status():
#     # i use setting alarm without argument
#     # if setting_alarm():
#         while True:
#             action = variable.get()
#             if action.lower() == 'a':
#                 alarm_status()
#             elif action.lower() == 'q':
#                 break
#             else:
#                 # print("Commande invalide. Veuillez taper 'a' pour activer/desactiver l'alarme ou 'q' pour quitter")
#                 label_info.config(text="Commande invalide. Veuillez taper 'a' pour activer/desactiver l'alarme ou 'q' pour quitter")
#         if alarm_active:
#             raise_alarm(setting_alarm(moment['heure_alarm'].get(),moment['minute_alarm'].get() ))



# def show_moment():
#     heure = moment['heure_alarm'].get()
#     minute = moment['minute_alarm'].get()

#     setting_alarm(heure, minute)

#     print(f"Heure: {heure}, Minute: {minute}")
    




# def show_fields():
#     # champ hours
#     label_hours = tk.Label(root, text='Hours: ')
#     label_hours.pack()

#     moment['heure_alarm'] = tk.Entry(root)
#     moment['heure_alarm'].pack()

#     # champ minute
#     label_minute = tk.Label(root, text='Minute: ')
#     label_minute.pack()

#     moment['minute_alarm'] = tk.Entry(root)
#     moment['minute_alarm'].pack()

#     button_moment = tk.Button(root, text="show alarm time", command=show_moment)
#     button_moment.pack()

# label_info = tk.Label(text='')
# label_info.pack()





# try the radio button with tkinter
# variable = tk.StringVar()
# radio_button1 = tk.Radiobutton(root, text="a", variable=variable, value="1")
# radio_button2 = tk.Radiobutton(root, text="q", variable=variable, value="2")
# radio_button1.pack()
# radio_button2.pack()

# button_active = tk.Button(root, text='Activer/Quitter', command=choose_status)
# button_active.pack()

# bouton_afficher = tk.Button(root, text='Regler', command=show_fields)
# bouton_afficher.pack()

# root.mainloop()
  


if __name__ == "__main__":
    main()
