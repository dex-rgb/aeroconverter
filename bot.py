import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté : {bot.user} est prêt !')

# --- 1. COMMANDE .convert (ZIP vers format Aerofly) ---
@bot.command()
async def convert(ctx):
    if not ctx.message.reference:
        await ctx.send("⚠️ Tu dois faire cette commande en **réponse** à ton fichier ZIP !")
        return
    
    ref_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    if not ref_msg.attachments:
        await ctx.send("⚠️ Le message auquel tu réponds ne contient aucun fichier.")
        return
    
    attachment = ref_msg.attachments[0]
    file_path = f"./{attachment.filename}"
    await attachment.save(file_path)
    
    await ctx.send(f"📥 Fichier `{attachment.filename}` reçu. Traitement et conversion en cours...")
    
    # ICI : Insérer le script de traitement de l'archive ZIP
    
    if os.path.exists(file_path):
        os.remove(file_path)

# --- 2. COMMANDE .convert2 (Encodage PNG -> TTX / TME) ---
@bot.command()
async def convert2(ctx):
    if not ctx.message.reference:
        await ctx.send("⚠️ Réponds à l'image PNG ou au fichier à encoder avec `.convert2`.")
        return
    
    ref_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    if ref_msg.attachments:
        att = ref_msg.attachments[0]
        await ctx.send(f"🔄 Encodage de `{att.filename}` en `.ttx` / `.tme` en cours...")
    else:
        await ctx.send("⚠️ Aucun fichier trouvé dans le message ciblé.")

# --- 3. COMMANDE .convert3 (Décodage TTX -> PNG) ---
@bot.command()
async def convert3(ctx):
    if not ctx.message.reference:
        await ctx.send("⚠️ Réponds au fichier `.ttx` avec `.convert3` pour décoder.")
        return
    
    ref_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    if ref_msg.attachments:
        att = ref_msg.attachments[0]
        await ctx.send(f"🔓 Décodage de `{att.filename}` vers PNG en cours...")

# --- 4. COMMANDE .fs4toglobal / .globaltofs4 (Cross-Platform) ---
@bot.command(name="fs4toglobal")
async def fs4toglobal(ctx, aircraft_name: str = None):
    if not aircraft_name:
        await ctx.send("⚠️ Précise le nom de l'avion (Ex: `a350_1000`).")
        return
    if not ctx.message.reference:
        await ctx.send("⚠️ Réponds au fichier ZIP de la livrée avec la commande.")
        return
    
    await ctx.send(f"✈️ Conversion FS4 vers FS Global pour l'appareil `{aircraft_name}` en cours...")

@bot.command(name="globaltofs4")
async def globaltofs4(ctx, aircraft_name: str = None):
    if not aircraft_name:
        await ctx.send("⚠️ Précise le nom de l'avion (Ex: `a350_1000`).")
        return
    if not ctx.message.reference:
        await ctx.send("⚠️ Réponds au fichier ZIP de la livrée avec la commande.")
        return
    
    await ctx.send(f"✈️ Conversion FS Global vers FS4 pour l'appareil `{aircraft_name}` en cours...")

# Remplace par ton token secret
bot.run("MTU2NDI1MTE0MjgwMjc3MTk4OA.GL-xd-.lT-xXKsIkIp0x5fcRTrH42jXMIvA-nIJUs-BtE")
