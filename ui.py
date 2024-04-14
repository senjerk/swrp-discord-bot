import disnake
from functions import get_ip
from datetime import datetime
import a2s


map_img_dict = {
    "rp_anaxes_ngg": "https://cdn.discordapp.com/attachments/1216277741238751322/1228989950448500756/rp_anaxes_ngg.jpg?ex=662e0d15&is=661b9815&hm=dbf04b28b9d9025bf9a68e74ae629e434db79d369dc00ea50b7958b2834b6c8a&",
    "ngg_sw_m3": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985724733231195/ngg_sw_m3.jpg?ex=662e0926&is=661b9426&hm=24a9c34f47340a8d1eb5c6ac1ced54a3b498c753c9b934ab5a5253c84730012e&",
    "ngg_sw_m4": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985724976758877/ngg_sw_m4.jpg?ex=662e0926&is=661b9426&hm=8ae8da9e1fb837e07b8a70a1fd070c14cb146b62959196df88961160ad3f5132&",
    "ngg_sw_m5": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985725169438781/ngg_sw_m5.jpg?ex=662e0926&is=661b9426&hm=a09fc2a0c6a19fc34a80fbb74a9999d82a3a3faf205186d77ed61660a12a8508&",
    "ngg_sw_m6": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985725349789827/ngg_sw_m6.jpg?ex=662e0926&is=661b9426&hm=9e2e8470789f5afc02f06e6bade7b8ba90b69981591dcbdef8ccb47213f1d7c8&",
    "ngg_sw_m7": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985725601710091/ngg_sw_m7.jpg?ex=662e0926&is=661b9426&hm=38ed24e80bdede79dae61f5a0928d30f154f767da6e4f7a517e13df615b94e35&",
    "ngg_sw_m9": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985725836333148/ngg_sw_m9.jpg?ex=662e0926&is=661b9426&hm=08bf924376a07912ca5129171678780f5648f9691aac72a8b9bcbe7a5c44c38a&",
    "ngg_sw_m10": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985726117347378/ngg_sw_m10.jpg?ex=662e0926&is=661b9426&hm=56d44ec2bc2d942909c720e9d9b3f1152e81ce2fdde7c4437cc0bb7c9702762f&",
    "ngg_sw_m11": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985726352490597/ngg_sw_m11.jpg?ex=662e0926&is=661b9426&hm=b54149a11e4b72cd8d45267784cde8041a32946f55e8351b5875fc55c98b0450&",
    "ngg_sw_m12": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985726574530581/ngg_sw_m12.jpg?ex=662e0926&is=661b9426&hm=5b55cf011217b327e7e2a063099f2b4e80398646ba71d05e75993406d2058276&",
    "ngg_sw_m13": "https://cdn.discordapp.com/attachments/1216277741238751322/1228985726809407558/ngg_sw_m13.jpg?ex=662e0926&is=661b9426&hm=4ef01cd22e3068378731a2eed8ed546f9049c502f308a42a03787ef692b097da&"
}


def create_embed(data: dict) -> disnake.Embed:
    ip = get_ip()
    embed = disnake.Embed(title="Началась спец. операция.", color=0xad0000)
    embed.set_author(name="SWRP Phase 1",
                     icon_url="https://m.media-amazon.com/images/I/51dq-a7FiqL._AC_UF894,1000_QL80_.jpg")
    embed.add_field(name=f"{data['event']} на планете {data['location']}",
                    value=f"На сервере {len(a2s.players(ip))}/{a2s.info(ip).max_players}", inline=False)
    embed.set_thumbnail(map_img_dict[a2s.info(ip).map_name])
    embed.set_footer(text=datetime.now().strftime("%H:%M %d.%m.%Y"))
    return embed