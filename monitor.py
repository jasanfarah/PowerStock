import requests
from discord.ext import commands

bot = commands.Bot(command_prefix='-power ')
@bot.command()
async def PID(ctx, productID):
    product = await getProductStock(productID)
    await ctx.send(f' {product} ')

async def getProductStock(product_id):
    url="https://www.power.dk/umbraco/api/product/getproductsbyids?ids=%s"%(product_id) # Generates correct URL for product based on product ID
    response = requests.get(url)
    data =response.json()[0]['StockCount']
    return "Stock Count :  %s "% (data)
bot.run({TOKEN})

