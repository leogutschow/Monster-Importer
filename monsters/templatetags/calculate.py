from django import template

register = template.Library()


@register.filter
def calculate_pf_xp(value: str):
    match value:
        case "1/8":
            return 50
        case "1/6":
            return 65
        case "1/4":
            return 100
        case "1/3":
            return 135
        case "1/2":
            return 200
        case "1":
            return 400
        case "2":
            return 600
        case "3":
            return 800
        case "4":
            return 1200
        case "5":
            return 1600
        case "6":
            return 2400
        case "7":
            return 3200
        case "8":
            return 4800
        case "9":
            return 6400
        case "10":
            return 9600
        case "11":
            return 12800
        case "12":
            return 19200
        case "13":
            return 25600
        case "14":
            return 38400
        case "15":
            return 51200
        case "16":
            return 76800
        case "17":
            return 102400
        case "18":
            return 153600
        case "19":
            return 204800
        case "20":
            return 307200
        case "21":
            return 409600
        case "22":
            return 614400
        case "23":
            return 819200
        case "24":
            return 1228800
        case "25":
            return 1638400



@register.filter
def calculate_mod(value: int):
    match value:
        case 1:
            return '-5'
        case 2 | 3:
            return '-4'
        case 4 | 5:
            return '-3'
        case 6 | 7:
            return '-2'
        case 8 | 9:
            return '-1'
        case 10 | 11:
            return '+0'
        case 12 | 13:
            return '+1'
        case 14 | 15:
            return '+2'
        case 16 | 17:
            return '+3'
        case 18 | 19:
            return '+4'
        case 20 | 21:
            return '+5'
        case 22 | 23:
            return '+6'
        case 24 | 25:
            return '+7'
        case 26 | 27:
            return '+8'
        case 28 | 29:
            return '+9'
        case 30:
            return '+10'


@register.filter
def calculate_challenge(value: str):
    match value:
        case "0":
            return 10
        case "1/8":
            return 25
        case "1/4":
            return 50
        case "1/2":
            return 100
        case "1":
            return 200
        case "2":
            return 450
        case "3":
            return 700
        case "4":
            return 1100
        case "5":
            return 1800
        case "6":
            return 2300
        case "7":
            return 2900
        case "8":
            return 3900
        case "9":
            return 5000
        case "10":
            return 5900
        case "11":
            return 7200
        case "12":
            return 8400
        case "13":
            return 10000
        case "14":
            return 11500
        case "15":
            return 13000
        case "16":
            return 15000
        case "17":
            return 18000
        case "18":
            return 20000
        case "19":
            return 22000
        case "20":
            return 25000

