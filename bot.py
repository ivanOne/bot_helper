import telebot
from dataprovider import SentryMember, get_connection
from settings import BOT_ID


bot = telebot.TeleBot(BOT_ID)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Принимать сообщения от Sentry /sentry_subscribe \n"
                          "Отписаться от рассылки Sentry /sentry_unsubscribe")


@bot.message_handler(commands=['sentry_subscribe'])
def subscribe_sentry(message):
    session = get_connection()
    result = session.query(SentryMember).filter(SentryMember.t_id == message.from_user.id).first()
    if result:
        bot.reply_to(message, "Вы уже подписаны!")
    else:
        sentry_member = SentryMember(t_id=message.from_user.id)
        session.add(sentry_member)
        session.commit()
    bot.reply_to(message, "Подписка принята!")


@bot.message_handler(commands=['sentry_unsubscribe'])
def subscribe_sentry(message):
    session = get_connection()
    session.query(SentryMember).filter(SentryMember.t_id == message.from_user.id).delete()
    session.commit()
    bot.reply_to(message, "Подписка отменена!")


def send_alert_message():
    session = get_connection()
    result = session.query(SentryMember).all()
    for user in result:
        if user.t_id:
            bot.send_message(user.t_id, "Тревога!")
    return 
