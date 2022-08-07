from django import template

register = template.Library()


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

