import time
from datetime import datetime

alarm_active = False

def main():
    print(show_time())
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
        if alarm_active:
            raise_alarm(alarm_time)

def show_time():
    moment = datetime.now().time().isoformat(timespec='minutes')
    return moment

def setting_alarm():
    # demander aux users d'entrer l'heure et la minute
    try:
        alarm_hours = int(input('Entrez l\'heure du reveille: '))
        alarm_minute = int(input('Entrez la minute du reveille: '))
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
            break
        time.sleep(10)

def alarm_status():
    global alarm_active
    if alarm_active:
        print("Alarm desactivee")
        alarm_active = False 
    else:
        print("alarm activee")
        alarm_active = True


if __name__ == "__main__":
    main()