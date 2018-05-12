import re

class SearchDict():
    def __init__(self):
        pass

    def get(self):
        search_fields = dict({
            # Eyec colours
            'eyes': re.compile('עיניים'),
            'green_eyes': re.compile('ירוקות|ירוק'),
            'blue_eyes': re.compile('כחולות|כחול'),
            'brown_eyes': re.compile('חומות|עיניים חומות'),
            
            # Hair types
            'hair': re.compile('שיער'),
            'brown_hair': re.compile('שיער חום|בצבע חום|ברונטית|ברונטי'),
            'black_hair': re.compile('שיער שחור|בצבע שחור|שחורדינית|שחור'),
            'blonde_hair': re.compile('בלונדיני|בלונדינית'),
            'ginger_hair': re.compile("ג'ינג'י|ג'ינג'ית|גינגי|גינגית"),
            'beard': re.compile('זקן|מזוקן|זיפים'),

            # Friday evenings
            'going_out': re.compile("לצאת|יציאות"),
            'parties': re.compile("מסיבות|מועדונים|מסיבה|מועדון"),
            'bars_pubs': re.compile(" בר | לבר |פאב|לפאב"),
            'bed': re.compile("מיטה|שמיכה|להתכרבל"),

            # TV & books
            'series': re.compile('סדרות|טלוויזיה|לראות סדרות'),
            'movies': re.compile('סרטים|סרט|קולנוע'),
            'books': re.compile('ספר'),

            # Army
            'bashal': re.compile('בש"לית|שירות לאומי'),
            'shinshin': re.compile('שנת שירות|ש"ש|שינשין'),
            'mechina': re.compile('מכינה|מכיניסט'),
            'malshab': re.compile('מלשב|מלש"ב|מלשבית|מלש"בית|לפני גיוס|מתייגס|מתגייסת|גיוס'),
            'soldier': re.compile('חייל|חיילת|משתחרר|משתחררת'),
            'combat': re.compile('קרבי|קרבית|לוחם|לוחמת'),
            'dailies': re.compile('יומיות'),
            'jobnics': re.compile("ג'ובניק|ג'ובניקית| גוב |גובניקית"),
            'officer': re.compile('קצין|קצינה'),
            'commander': re.compile('מפקד|מפקדת'),
            'secret': re.compile('סודי|מסווג'),

            # Foods and drinks
            'hamburger': re.compile('המבורגר'),
            'pizza': re.compile('פיצה'),
            'ice_cream': re.compile('גלידה'),
            'hummus': re.compile('חומוס'),
            'beer': re.compile('בירה'),
            'wine': re.compile(' יין '),

            # Geography
            'north': re.compile('צפון'),
            'center': re.compile('מרכז'),
            'sharon': re.compile('שרון'),
            'south': re.compile('דרום'),

            # Religion
            'religious': re.compile('דתי|דתייה'),
            'traditional': re.compile('מסורתי|מסורתית'),
            'hiloni': re.compile('חילוני|חילונית'),
            'atheist': re.compile('אתאיסט|אתאיסטית'),
            'sabbath': re.compile('שומר שבת|שומרת שבת'),
            'kosher': re.compile('כשר'),

            # Animals and diets
            'dogs': re.compile('כלב|כלבים'),
            'cats': re.compile('חתול|חתולים'),
            'horses': re.compile('סוס|סוסים|רכיבה'),
            'carnibore': re.compile('קרניבור|קרניבורית|בשר'),
            'vegiterian': re.compile('צמחוני|צמחונית'),
            'vegan': re.compile('טבעוני|טבעונית'),

            ## Nature, Pakal and coffee
            'coffee': re.compile('קפה'),
            'tea': re.compile(' תה '),
            'pakal': re.compile('פק"ל|פקל'),
            'picnic': re.compile('פיקניק'),
            'trip': re.compile('טיולים|לטייל'),
            'nature': re.compile('טבע'),
            'desert': re.compile('מדבר|נגב|ערבה'),
            'sea': re.compile(' ים |חוף'),
            'sunrise': re.compile('זריחה|זריחות'),
            'sunset': re.compile('שקיעה|שקיעות'),

            # Body types
            'short(F)': re.compile('נמוכה'),
            'short(M)': re.compile('נמוך'),
            'tall': re.compile('גבוה'),
            'skinny': re.compile('רזה'),
            'plus_size': re.compile('מלאה|מבנה גוף מלא'),
            'fat(F)': re.compile('שמנה'),
            'fat(M)': re.compile('שמן'),
            'mascular(M)': re.compile('שרירי|אתלט'),
            'mascular(F)': re.compile('שרירית|אתלטית'),

            # Hobbies
            'cooking': re.compile('לבשל|בישול'),
            'sports': re.compile('ספורט|להתאמן'),
            'piano': re.compile('פסנתר'),
            'guitar': re.compile('גיטרה'),
            'ukulele': re.compile('יוקילילי'),
            'singing': re.compile(' שר | שרה |לשיר'),
            'dancing': re.compile(' שר | שרה |לשיר'),

            # Ages
            '17': re.compile(' 17 '),
            '18': re.compile(' 18' ),
            '19': re.compile(' 19 '),
            '20': re.compile(' 20 '),
            '21': re.compile(' 21 '),
            '22': re.compile(' 18 '),

            # Most imporant thing in a person
            'eitan': re.compile('איתן|אית"ן')

            })

        return search_fields