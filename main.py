import discord
from discord.ext import commands

# Botun için gerekli izinleri ayarlıyoruz
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Bot hazır olduğunda mesaj atacak
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Geri dönüşüm ile ilgili bilgi veren komut
@bot.command()
async def geri_donustur(ctx, item: str):
    # Eşyaların geri dönüşüm kategorilerini belirleyelim
    recycling_info = {
        "kağıt": "Kağıt, geri dönüştürülebilir. Biriktirip geri dönüşüm kutusuna atabilirsiniz.",
        "cam": "Cam da geri dönüştürülebilir. Cam şişeleri ve kavanozları geri dönüşüm kutusuna atabilirsiniz.",
        "plastik": "Plastik, geri dönüşüm yapılabilir. Plastik ambalajları geri dönüşüm kutusuna atmalısınız.",
        "metal": "Metaller geri dönüştürülebilir. Metal kutuları geri dönüşüm kutusuna atabilirsiniz.",
    }

    # Kullanıcının verdiği eşya ismine göre geri dönüşüm bilgisini gönderiyoruz
    item = item.lower()
    if item in recycling_info:
        await ctx.send(recycling_info[item])
    else:
        await ctx.send("Bu eşya hakkında geri dönüşüm bilgisi bulunmamaktadır. Lütfen başka bir eşya girin.")

# Ayrışma süresi ile ilgili komut
@bot.command()
async def ayrisma_suresi(ctx, item: str):
    # Eşyaların ayrışma sürelerini belirleyelim
    decomposition_info = {
        "kağıt": "Kağıt, doğada yaklaşık 2-6 hafta içinde ayrışır.",
        "cam": "Cam, doğada ayrışmaz. Yüzyıllar sürebilir.",
        "plastik": "Plastik, doğada yaklaşık 450 yıl süresince ayrışmaz.",
        "metal": "Metal, türüne bağlı olarak 50-100 yıl arasında ayrışabilir.",
    }

    # Kullanıcının verdiği eşya ismine göre ayrışma süresini gönderiyoruz
    item = item.lower()
    if item in decomposition_info:
        await ctx.send(decomposition_info[item])
    else:
        await ctx.send("Bu eşya hakkında ayrışma süresi bilgisi bulunmamaktadır. Lütfen başka bir eşya girin.")

# Botu çalıştırıyoruz
bot.run("TOKEN")  # Buraya kendi bot tokenınızı yazın
