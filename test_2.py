def check_access(card, pin, voice, alarm):
    if not alarm:
        if (card and pin) or (card and voice):
            return "доступ разрешен"
        else:
            return "доступ запрещен"
    else:
        if card and pin and voice:
            return "доступ разрешен"
        else:
            return "доступ запрещен"
