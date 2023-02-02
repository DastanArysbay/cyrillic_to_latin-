import telebot as tg

bot = tg.TeleBot("API_TOKEN")
# I
def convert_kazakh_to_latin(text: str) -> str:
    # Define a dictionary to map Kazakh letters to latin letters
    kazakh_to_latin = {
        'ә': 'ä', 'Ә': 'Ä', 'і': 'ı', 'І': 'I',  'ң': 'ñ', 'Ң': 'Ñ', 'ғ': 'ğ', 'Ғ': 'Ğ', 'ү': 'ü', 'Ү': 'Ü', 'Ұ': 'Ū', 'ұ': 'ū', 'қ': 'q', 'Қ': 'Q', 'Ө': 'Ö', 'ө': 'ö', 'һ': 'h',
        'Һ': 'H',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',  'д': 'd', 'е': 'e', 'ё': 'ö', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'i',
        'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 's', 'ч': 'ch', 'Ш': 'Ş', 'Щ': 'Ş', 'ъ': '', 'ы': 'y',
        'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia',
        'А': 'A', 'Б': 'B', 'B': 'V', 'Г': 'G', 'Д': 'D',  'Е': 'E', 'Ё': 'Ö', 'Ж': 'J', 'З': 'Z', 'И': 'İ', 'Й': 'İ',
        'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'S', 'Ч': 'Ch', 'ш': 'ş', 'щ': 'ş', 'Ъ': '', 'Ы': 'Y',
        'Ь': '', 'Э': 'E', 'Ю': 'İu', 'Я': 'İa',
    }
    latin_text = ''
    for char in text:
        if char in kazakh_to_latin:
            latin_text += kazakh_to_latin[char]
        else:
            latin_text += char
    return latin_text

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Армысыз, мен қазақ әріптерін латын әліпбиіне айналдыра алатын ботпын. Маған қазақ тілінде хабарлама жіберіңіз  (max: 4096 әріп)')

@bot.message_handler(content_types=['text'])
def convert_text(message):
    latin_text = convert_kazakh_to_latin(message.text)
    bot.send_message(message.chat.id, latin_text)

bot.polling()
