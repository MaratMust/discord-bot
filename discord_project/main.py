import discord
from discord.ext import commands
from data import db_session
from data.man import Man
from datetime import datetime
import config

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            await bot.get_channel(channel.id).send("Im in.")
            await bot.get_channel(channel.id).send('https://tenor.com/view/cool-pog-rainbow-epic-gif-18198472')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hello, {member.name}!')
    await member.dm_channel.send('Im bot 👎👎👎.')
    await member.dm_channel.send('https://tenor.com/view/brawl-stars-dislike-gif-25745609')
    await member.dm_channel.send('All commands start with dot(.)')
    await member.dm_channel.send('Write date like \'%d.%m.%y\'')
    await member.dm_channel.send('Please write \'.reg\'')


@bot.event
async def on_member_remove(member):
    await member.dm_channel.send('Goodbye!')


@bot.command(name='reg')
async def reg(ctx, name=None, email=None, phone_number=None, birthday=None, address=None):
    try:
        if '@' not in email:
            await ctx.send('Something wrong with your email.')
            return
        if len(phone_number) <= 11 or len(phone_number) >= 18:
            await ctx.send('Something wrong with your phone.')
            return
        try:
            if datetime.strptime(birthday, '%d.%m.%y') > datetime.now():
                await ctx.send('Something wrong with your date')
                return
        except:
            await ctx.send('Please FORMAT date to \'%d.%m.%y\'!')
            return
        db_sess = db_session.create_session()
        man = Man()
        man.name = name
        if not list(db_sess.query(Man).filter(Man.email == email)):
            man.email = email
        else:
            await ctx.send('This email is already here')
            return
        if not list(db_sess.query(Man).filter(Man.phone_number == phone_number)):
            man.phone_number = phone_number
        else:
            await ctx.send('This phone is already here')
            return
        man.birthday = datetime.strptime(birthday, '%d.%m.%y')
        man.address = address
        db_sess.add(man)
        db_sess.commit()
    except:
        await ctx.send('Hm... It broke down. Okay... May be I can fix it.')
    else:
        await ctx.send('I think... It works!!!')


@bot.command(name='time')
async def time_now(ctx):
    await ctx.send(datetime.now().strftime('%d.%m.%y - %H:%M'))


@bot.command(name='show_all')
async def show_all(ctx):
    db_sess = db_session.create_session()
    for man in db_sess.query(Man).all():
        await ctx.send(man)


@bot.command(name='show_name')
async def show_name(ctx, name):
    db_sess = db_session.create_session()
    if list(db_sess.query(Man).filter(Man.name == name)):
        for man in db_sess.query(Man).filter(Man.name == name):
            await ctx.send(man)
    else:
        await ctx.send('There is no this name')


@bot.command(name='show_phone')
async def show_phone(ctx, phone):
    db_sess = db_session.create_session()
    if list(db_sess.query(Man).filter(Man.phone_number == phone)):
        for man in db_sess.query(Man).filter(Man.phone_number == phone):
            await ctx.send(man)
    else:
        await ctx.send('There is no this phone')


@bot.command(name='show_email')
async def show_email(ctx, email):
    db_sess = db_session.create_session()
    if list(db_sess.query(Man).filter(Man.email == email)):
        for man in db_sess.query(Man).filter(Man.email == email):
            await ctx.send(man)
    else:
        await ctx.send('There is no this email')


@bot.command(name='show_address')
async def show_address(ctx, address):
    db_sess = db_session.create_session()
    if list(db_sess.query(Man).filter(Man.email == address)):
        for man in db_sess.query(Man).filter(Man.address == address):
            await ctx.send(man)
    else:
        await ctx.send('There is no this address')


@bot.command(name='show_id')
async def show_id(ctx, id):
    db_sess = db_session.create_session()
    if list(db_sess.query(Man).filter(Man.id == id)):
        for man in db_sess.query(Man).filter(Man.id == id):
            await ctx.send(man)
    else:
        await ctx.send('There is no this id')


db_session.global_init("db/people.db")

bot.run(config.TOKEN)
