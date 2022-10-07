import json
import os
import random
import discord
#-------------------------------------------------------------------------------
from core.classes import Cog_Extension
from discord.ext import commands
import asyncio
import json
import datetime

class event(Cog_Extension):

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def 啟動 (self,ctx):
        with open('問答設置.json','r',encoding='utf8') as jfile:
            config = json.load(jfile)


        rang = int(len(config['問答集']))


        knowans = []
        playerpoint = {}
        回 = config['按鈕回覆內容']
        秒 = config['每題間隔秒數']
        秒 = int(秒)


        embed=discord.Embed(title=f"正在讀取題目...", color=discord.Colour.random())


        
        ba = discord.ui.Button(label='A',style=discord.ButtonStyle.blurple)
        bb = discord.ui.Button(label='B',style=discord.ButtonStyle.blurple)
        bc = discord.ui.Button(label='C',style=discord.ButtonStyle.blurple)
        bd = discord.ui.Button(label='D',style=discord.ButtonStyle.blurple)
        
        async def a_callback(inter):
            if inter.user.id not in knowans:
                if x1['答案'] == 'A':
                    await inter.response.send_message(f'{回}',ephemeral=True)
                    knowans.append(inter.user.id)
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = {}
                        playerpoint[str(inter.user.id)]['point'] = ["1"]
                    else:
                        playerpoint[str(inter.user.id)]['point'] += ["1"]
                else:
                    await inter.response.send_message(f'{回}',ephemeral=True)
                    knowans.append(inter.user.id)
            else:
                await inter.response.send_message(f'這題你已經回答過囉!',ephemeral=True)
        async def b_callback(inter):
            if inter.user.id not in knowans:
                if x1['答案'] == 'B':
                    await inter.response.send_message(f'{回}',ephemeral=True)
                    knowans.append(inter.user.id)
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = {}
                        playerpoint[str(inter.user.id)]['point'] = ["1"]
                    else:
                        playerpoint[str(inter.user.id)]['point'] += ["1"]
                else:
                    await inter.response.send_message(f'{回}',ephemeral=True)
                    knowans.append(inter.user.id)
            else:
                await inter.response.send_message(f'這題你已經回答過囉!',ephemeral=True)
        async def c_callback(inter):
            if inter.user.id not in knowans:
                if x1['答案'] == 'C':
                    await inter.response.send_message(f'{回}',ephemeral=True)
                    knowans.append(inter.user.id)
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = {}
                        playerpoint[str(inter.user.id)]['point'] = ["1"]
                    else:
                        playerpoint[str(inter.user.id)]['point'] += ["1"]
                else:
                    await inter.response.send_message(f'{回}',ephemeral=True)
                    knowans.append(inter.user.id)
            else:
                await inter.response.send_message(f'這題你已經回答過囉!',ephemeral=True)
        async def d_callback(inter):
            if inter.user.id not in knowans:
                if x1['答案'] == 'D':
                    await inter.response.send_message(f'{回}',ephemeral=True)
                    knowans.append(inter.user.id)
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = {}
                        playerpoint[str(inter.user.id)]['point'] = ["1"]
                    else:
                        playerpoint[str(inter.user.id)]['point'] += ["1"]
                else:
                    await inter.response.send_message(f'{回}',ephemeral=True)
                    knowans.append(inter.user.id)
            else:
                await inter.response.send_message(f'這題你已經回答過囉!',ephemeral=True)
        ba.callback = a_callback
        bb.callback = b_callback
        bc.callback = c_callback
        bd.callback = d_callback
        view = discord.ui.View()
        view.add_item(ba)
        view.add_item(bb)
        view.add_item(bc)
        view.add_item(bd)
        wmsg = await ctx.send(embed=embed)
        await asyncio.sleep(2)
        for x1 in config['問答集']:
            q1 = x1['題目']
            q2 = x1['A']
            q3 = x1['B']
            q4 = x1['C']
            q5 = x1['D']
            q6 = str(x1['圖片網址'])
            x1embed=discord.Embed(title=f"{config['嵌入標題']}", description=f"每{秒}秒會切換下一題\n{q1}\n\nA:{q2}\nB:{q3}\nC:{q4}\nD:{q5}", color=discord.Colour.random())
            x1embed.set_image(url=q6)
            await wmsg.edit(embed=x1embed,view=view)
            await asyncio.sleep(秒)
            knowans.clear()
        embed=discord.Embed(title=f"{config['嵌入標題']}", description=f"遊戲已經結束囉!", color=discord.Colour.random())
        ba.disabled = True
        bb.disabled = True
        bc.disabled = True
        bd.disabled = True
        await wmsg.edit(embed=embed,view=view)
        point = ''
        for ansersss in playerpoint:
            point = point+f"<@{ansersss}>:{len(playerpoint[ansersss]['point'])}"
        conchannel = config['遊戲統計訊息傳送頻道ID']
        dechannel = self.bot.get_channel(int(conchannel))
        embed=discord.Embed(title="遊戲結果統計", description=f"{point}", color=discord.Colour.random())
        await dechannel.send(embed=embed)
async def setup(bot):
    await bot.add_cog(event(bot))