"""
Rubika Asynchronous/Synchronous Client Library 

Github: https://github.com/Rubier-Project/RubiXgram
Rubika Channel: @RubixGram1
Dev: @StreamX
Supporters: @Off_coder - @StreamX
"""

from .network import XNetwork
from .updater import XUpdater
from .DataParse import Parse
from mutagen import mp3, File
from tempfile import NamedTemporaryFile
from aiortc.contrib.media import MediaPlayer
import re
import time
import random
import httpx
import aiortc
import io
import os
import base64

class ReactionsIds(object):
    RED_HEART = 1
    LIKE = 2
    UN_LIKE = 3
    FIRE = 4
    SMILING_FACE_WITH_HEARTS = 5
    CLAPPING_HANDS = 6
    IRAN = 7
    BEAMING_FACE = 8
    THINKING_FACE = 9
    EXPLODING_HEAD = 10
    SCREAMING_FACE = 11
    FACE_WITH_SYMBOLS_ON_MOUTH = 12
    CRYING_FACE = 13
    CELEBRATION = 14
    PARTY_POPPER = 15
    STAR_STRUCK = 16
    FACE_VOMITING = 17
    PILE_OF_POO = 18
    FOLDED_HANDS = 19
    OKAY = 20
    DOVE_OF_PEACE = 21
    CLOWN_FACE = 22
    YAWNING_FACE = 23
    WOOZY_FACE = 24
    SMILING_FACE_WITH_HEART_EYES = 25
    WHALE = 26
    HEART_ON_FIRE = 27
    NEW_MOON_FACE = 28
    HOT_DOG = 29
    HUNDRED_POINTS = 30
    ROLLING_ON_THE_FLOOR_LAUGHING = 31
    HIGH_VOLTAGE = 32
    BANANA = 33
    TROPHY = 34
    BROKEN_HEART = 35
    FACE_WITH_RAISED_EYEBROW = 36
    NEUTRAL_FACE = 37
    STRAWBERRY = 38
    KISS_MARK = 39
    SMILING_FACE_WITH_HORNS = 40
    SLEEPING = 41
    LOUDLY_CRYING_FACE = 42
    NERD_FACE = 43
    GHOST = 44
    MAN_TECHNOLOGIST = 45
    EYES = 46
    JACK_O_LANTERN = 47
    SEE_NO_EVIL_MONKEY = 48
    SMILING_FACE_WITH_HALO = 49
    FEARFUL_FACE = 50
    HANDSHAKE = 51
    WRITING_HANDS = 52
    HUGGING_FACE = 53
    SANTA_CLAUS = 54
    CHRISTMAS_TREE = 55
    SNOWMAN = 56
    NAIL_POLISH = 57
    ZANY_FACE = 58
    MOAI = 59
    COOL_BUTTON = 60
    HEART_WITH_ARROW = 61
    HEAR_NO_EVIL_MONKEY = 62
    UNICORN = 63
    FACE_BLOWING_A_KISS = 64
    PILL = 65
    SPEAK_NO_EVIL_MONKEY = 66
    SMILING_FACE_WITH_SUNGLASSES = 67
    ALIEN_MONSTER = 68
    SHRUGGING_MAN = 69
    SHRUGGING_PERSON = 70
    SHRUGGING_WOMAN = 71
    RAGE = 72

    def __init__(self) -> None:
        self.dictionary_option = {
            "RED_HEART": 1,
            "LIKE": 2,
            "UN_LIKE": 3,
            "FIRE": 4,
            "SMILING_FACE_WITH_HEARTS": 5,
            "CLAPPING_HANDS": 6,
            "IRAN": 7,
            "BEAMING_FACE": 8,
            "THINKING_FACE": 9,
            "EXPLODING_HEAD": 10,
            "SCREAMING_FACE": 11,
            "FACE_WITH_SYMBOLS_ON_MOUTH": 12,
            "CRYING_FACE": 13,
            "CELEBRATION": 14,
            "PARTY_POPPER": 15,
            "STAR_STRUCK": 16,
            "FACE_VOMITING": 17,
            "PILE_OF_POO": 18,
            "FOLDED_HANDS": 19,
            "OKAY": 20,
            "DOVE_OF_PEACE": 21,
            "CLOWN_FACE": 22,
            "YAWNING_FACE": 23,
            "WOOZY_FACE": 24,
            "SMILING_FACE_WITH_HEART_EYES": 25,
            "WHALE": 26,
            "HEART_ON_FIRE": 27,
            "NEW_MOON_FACE": 28,
            "HOT_DOG": 29,
            "HUNDRED_POINTS": 30,
            "ROLLING_ON_THE_FLOOR_LAUGHING": 31,
            "HIGH_VOLTAGE": 32,
            "BANANA": 33,
            "TROPHY": 34,
            "BROKEN_HEART": 35,
            "FACE_WITH_RAISED_EYEBROW": 36,
            "NEUTRAL_FACE": 37,
            "STRAWBERRY": 38,
            "KISS_MARK": 39,
            "SMILING_FACE_WITH_HORNS": 40,
            "SLEEPING": 41,
            "LOUDLY_CRYING_FACE": 42,
            "NERD_FACE": 43,
            "GHOST": 44,
            "MAN_TECHNOLOGIST": 45,
            "EYES": 46,
            "JACK_O_LANTERN": 47,
            "SEE_NO_EVIL_MONKEY": 48,
            "SMILING_FACE_WITH_HALO": 49,
            "FEARFUL_FACE": 50,
            "HANDSHAKE": 51,
            "WRITING_HANDS": 52,
            "HUGGING_FACE": 53,
            "SANTA_CLAUS": 54,
            "CHRISTMAS_TREE": 55,
            "SNOWMAN": 56,
            "NAIL_POLISH": 57,
            "ZANY_FACE": 58,
            "MOAI": 59,
            "COOL_BUTTON": 60,
            "HEART_WITH_ARROW": 61,
            "HEAR_NO_EVIL_MONKEY": 62,
            "UNICORN": 63,
            "FACE_BLOWING_A_KISS": 64,
            "PILL": 65,
            "SPEAK_NO_EVIL_MONKEY": 66,
            "SMILING_FACE_WITH_SUNGLASSES": 67,
            "ALIEN_MONSTER": 68,
            "SHRUGGING_MAN": 69,
            "SHRUGGING_PERSON": 70,
            "SHRUGGING_WOMAN": 71,
            "RAGE": 72
        }

    def get(self, name: str) -> int:
        if name.upper() in self.dictionary_option.keys():
            return self.dictionary_option[name.upper()]
        else:
            return 0x063 # 99

class FormattingOptions(object):
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return "Formatting Options class is a HELPER class to use them singly in texts"

    @property
    def underline(self) -> str:
        return f"--{self.text}--"
    
    @property
    def bold(self) -> str:
        return f"**{self.bold}**"
    
    @property
    def mono(self) -> str:
        return f"``{self.text}``"
    
    @property
    def italic(self) -> str:
        return f"__{self.text}__"
    
    @property
    def strike(self) -> str:
        return f"~~{self.text}~~"
    
    @property
    def spoil(self) -> str:
        return f"||{self.spoil}||"
    
    def linkify(self, text: str, link: str) -> str:
        return f"[{text}]({link})"

# Thanks to Rubpy for this Class

class Markdown(object):
    def __init__(self, text: str) -> None:
        self.mark = ( r'\*\*(.*?)\*\*|``(.*?)``|__(.*?)__|--(.*?)--|~~(.*?)~~|\|\|(.*?)\|\||\[(.*?)\]\((\S+)\)' )
        self.pattern = re.compile(self.mark)
        self.text = text
    
    @property
    def metadata(self) -> dict:
        meta_data_parts = []

        while True:
            for markdown in self.pattern.finditer(self.text):
                string = markdown.group(0)
                span = markdown.span()
                from_index = span[0]

                if string.startswith('**'):
                    self.text = self.pattern.sub(r'\1', self.text, count=1)
                    meta_data_parts.append({
                        'type': 'Bold',
                        'from_index': from_index,
                        'length': len(string) - 4,
                    })
                    break
                elif string.startswith('``'):
                    self.text = self.pattern.sub(r'\2', self.text, count=1)
                    meta_data_parts.append({
                        'type': 'Mono',
                        'from_index': from_index,
                        'length': len(string) - 4,
                    })
                    break
                elif string.startswith('__'):
                    self.text = self.pattern.sub(r'\3', self.text, count=1)
                    meta_data_parts.append({
                        'type': 'Italic',
                        'from_index': from_index,
                        'length': len(string) - 4,
                    })
                    break
                elif string.startswith('--'):
                    self.text = self.pattern.sub(r'\4', self.text, count=1)
                    meta_data_parts.append({
                        'type': 'Underline',
                        'from_index': from_index,
                        'length': len(string) - 4,
                    })
                    break
                elif string.startswith('~~'):
                    self.text = self.pattern.sub(r'\5', self.text, count=1)
                    meta_data_parts.append({
                        'type': 'Strike',
                        'from_index': from_index,
                        'length': len(string) - 4,
                    })
                    break
                elif string.startswith('||'):
                    self.text = self.pattern.sub(r'\6', self.text, count=1)
                    meta_data_parts.append({
                        'type': 'Spoiler',
                        'from_index': from_index,
                        'length': len(string) - 4,
                    })
                    break

                else:
                    self.text = self.pattern.sub(r'\7', self.text, count=1)
                    mention_text_object_type = 'hyperlink'
                    mention_type = 'MentionText'
                    mention_text_object_guid = markdown.group(8)
                    length = len(markdown.group(7))

                    if mention_text_object_guid.startswith('u'):
                        mention_text_object_type = 'User'
                    elif mention_text_object_guid.startswith('g'):
                        mention_text_object_type = 'Group'
                    elif mention_text_object_guid.startswith('c'):
                        mention_text_object_type = 'Channel'
                    else:
                        mention_type = 'Link'

                    if mention_type == 'MentionText':
                        meta_data_parts.append({
                            'type': mention_type,
                            'from_index': from_index,
                            'length': length,
                            'mention_text_object_guid': mention_text_object_guid,
                            'mention_text_object_type': mention_text_object_type
                        })
                        break

                    else:
                        meta_data_parts.append({
                            'from_index': from_index,
                            'length': length,
                            'link': {
                                'hyperlink_data': {
                                    'url': mention_text_object_guid,
                                },
                                'type': mention_text_object_type,
                            },
                            'type': mention_type,
                        })
                        break

            else:
                break

        result = {'text': self.text.strip()}

        if meta_data_parts:
            result['metadata'] = {'meta_data_parts': meta_data_parts}

        return result

class ClientMessenger(object):

    __version__ = "1.0.0"
    __github__ = "https://github.com/Rubier-Project/RubiXgram"

    def __init__(self, AuthToken: str, PrivateKey: str, UseFakeUserAgent: bool = True, Proxy = None):
        self.authtoken = AuthToken
        self.privatekey = PrivateKey.replace("-----BEGIN PRIVATE KEY-----\n", "").replace("\n-----END PRIVATE KEY-----", "")

        self.ufa = UseFakeUserAgent
        self.proxy = Proxy
        
        self.network = XNetwork(self.authtoken, self.privatekey, Proxy)
        self.handlers = []
    
    def __str__(self):
        return f"<RubiXgram {self.__github__} - {self.__version__}>"
    
    @property
    def accountInfo(self) -> dict:
        return self.network.option({}, "getUserInfo", self.ufa)

    def handlePhoneNumber(self, phone: str):
        p = ""
        if phone.startswith("0"):
            p = phone[1:]
        elif phone.startswith("98"):
            p = phone[2:]
        elif phone.startswith("+98"):
            p = phone[3:]
        else:
            p = phone
        
        return f"98{p}"
    
    def guessGuid(self, guid: str):
        if guid.startswith("c0"):
            return "Channel"
        elif guid.startswith("g0"):
            return "Group"
        elif guid.startswith("u0"):
            return "User"
        elif guid.startswith("b0"):
            return "Bot"
        elif guid.startswith("s0"):
            return "Service"
        
    def guessLink(self, link: str):
        if "rubika.ir/joing" in link: return "Group"
        elif "rubika.ir/joinc" in link: return "Channel"
        
    def endpointHash(self, link: str):
        if "/" in link:
            return link.split("/")[-1]
        else:
            return link
        
    def getDefaultTumbInline(self) -> str:
        return "iVBORw0KGgoAAAANSUhEUgAAACgAAAARCAIAAAAg6XlfAAAEwUlEQVR4nK1VXWwUVRQ+587s7HZ3u+x0u/3bav8WgQqkP1RpKdW0adXgSxFjCg9gxJhomvCIz/pgNE0gjfHBv6ARjVFDNCUagkkLTbS0Sw00BYoUuuy23dLZ7ezs7szszD0+jMEXoj70PJ2cLznfPSfnfh8SEWxiEAFxYAIALCsX/1z9fDpxt6asb2DHW8GSCgDgRAwRAHAzibntUGazN+cefPZAuSShcE3hSW2j0lvW1fT60/VDLkEkIAAUN42VCJhgq2v58x+ZG2O+KFflLZbEGGa2SO5lvXQkNr/N+O1Q7RN7AhVAgETkDI2Ij+r2/yDigFiY+lb/aRTWkuLuSnelN8v1ZKh4rijPqi1c2AkolDbIJAjtZZVDkR3iI/sSkVN8JKUTDkRECADICrEZ7fS7UoR4QOaIuqW4WWhn9ZtSuDd7/XpsecEtipIQZmUlV+4s6T/eEQFAVVVVVYPBoN/vN01TkiRELBQKAKAoCgBEIhEAcCDbtonItu1UKuX3+2VZLuo6c7nshUVzqYajxxtICIxj00vSjtfAV70N4P1nq369W3/2xlUyLd+5eOj8/eyGKebz+ZGRkYaGhkwm09HRMTU1deLEidnZ2cXFxXw+n8vlfD6fYRj79++fnp4+fPjwzMxMJpNZWVkxTdMwjM7OTm1DFeQtnX6/CoYn659PNHl6X9m15yACAHEOiIi99VtbKmreGf5CurYmlLqgVGK6rgeDwWPHjkWj0Xg83tPTc+rUqYmJiYGBAU3T9u7de+DAgVQqlU6nDcMgItM0dV03TbOjoyMSiSiKYtmWbhYZ43mSxij6lb4rUaxWMqmMkuYEDNEqWllNE00rm7LmCbKARRuZ2+1OJpOjo6OJRKK3t7e9vX19fb21tdXv9xcKhcnJyZMnT/b39zvbRkSPxwMAjLHZ2dmVlRUism3uFeCWJX9stv1hVQvAXWAS4EY2u7q6qmlaPp8jzjmQ4IKsAddVECxVLBQKVVVVw8PDD8+qsbExHA4713706NF0On3mzJnjx4/H4/GlpaVYLNbc3JxIJPr6+mzbvnDhQn1dQ8A2bxrBqQ2hRTYFBBciASBjlmWZpimKIoIN6MraUpVkDMlLT7kV0efzdXd3ExHnHBEZYy0tLaFQCBG7u7t1Xa+tre3q6mKMDQ4Ojo2NRSKRffv22bY9Pj4uSdKRI0eU9bTX7165vWwTLW4UmcETRG2InKFBgEAAAJLMteShwM223N2Qp5hD138r18Ov9e/xzacTn7z3c0lTeVz2hp+L9rZEng946ktczB9GLMK9MXb7rOvKvdx9WVfK0AIRADjnjLGHLZzREdGpOwni31LjbIVz7rzYyRljW5+sWW4so2i5wEkkmlK12Lr5THngZW08eOvLYuYaCd684GbVGY+Y5HLP5mg1EQHi15dvnP5+JrmqNvdvL9/+OMvN+4zv+kvnWvNiZdYjcNSvrnG1ILb1eQ++vWkm4SxjNaON/hCbgQd1j12uMieRCtsqQkGvq0Qr1C9r8r06qecNT9sLsLnuZHMSGALAkrJwaeGDudXfOYhtlf6AqDN3dTQ8VF8+yAQJHJHfXD8mAk5cYAwA5pIXf7nxYcSr7I682Fj5qlsKAfxjnX8BoH+PlgeA47wAAAAASUVORK5CYII="
    
    def getImageThumbnail(self, bytes:bytes) -> str:
        try:
            from PIL import Image
        except ImportError:
            os.system("pip install pillow")
            from PIL import Image
            
        image = Image.open(io.BytesIO(bytes))
        width, height = image.size
        if height > width:
            new_height = 40
            new_width  = round(new_height * width / height)
        else:
            new_width = 40
            new_height = round(new_width * height / width)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        changed_image = io.BytesIO()
        image.save(changed_image, format="PNG")
        return base64.b64encode(changed_image.getvalue()).decode("UTF-8")
    
    def getImageSize(self, bytes:bytes) -> str:
        try:
            from PIL import Image
        except ImportError:
            os.system("pip install pillow")
            from PIL import Image

        width, height = Image.open(io.BytesIO(bytes)).size
        return width , height
    
    def getVideoData(self, bytes:bytes) -> list:
        try:
            from moviepy.editor import VideoFileClip

            with NamedTemporaryFile(delete=False, dir=".") as temp_video:
                temp_video.write(bytes)
                temp_path = temp_video.name

            os.chmod(temp_path, 0o777)

            try:
                from PIL import Image
            except ImportError:
                os.system("pip install pillow")
                from PIL import Image

            with VideoFileClip(temp_path) as clip:
                duration = clip.duration
                resolution = clip.size
                thumbnail = clip.get_frame(0)
                thumbnail_image = Image.fromarray(thumbnail)
                thumbnail_buffer = io.BytesIO()
                thumbnail_image.save(thumbnail_buffer, format="JPEG")
                thumbnail_b64 = base64.b64encode(thumbnail_buffer.getvalue()).decode("UTF-8")
                clip.close()

            os.remove(temp_path)

            return thumbnail_b64, resolution, duration
        except ImportError:
            print("Can't get video data! Please install the moviepy library by following command:\npip install moviepy" + "\033[00m")
            return self.getDefaultTumbInline(), [900, 720], 1
        except:
            return self.getDefaultTumbInline(), [900, 720], 1
        
    def getVoiceDuration(self, bytes:bytes) -> int:
        file = io.BytesIO()
        file.write(bytes)
        file.seek(0)
        return mp3.MP3(file).info.length
    
    def getMusicArtist(self, bytes:bytes) -> str:
        try:
            audio = File(io.BytesIO(bytes), easy=True)

            if audio and "artist" in audio:
                return audio["artist"][0]
            
            return "rubix"
        except Exception:
            return "rubix"
        
    def getFileName(self, fname: str):
        if "/" in fname:
            return fname.split("/")[-1]
        elif "\\" in fname:
            return fname.split("\\")[-1]
        else:
            return fname

    def getMe(self) -> dict:
        return self.network.option({}, "getUserInfo", self.ufa)

    def getChatsUpdates(self) -> dict:
        return self.network.option({"state": time.time() - 150}, "getChatsUpdates", self.ufa)
    
    def getChats(self) -> dict:
        return self.network.option({"start_id": None}, "getChats", self.ufa)

    def onMessage(self):
        yield XUpdater(self.authtoken, self.privatekey, self.getChatsUpdates(), self.ufa, self.proxy)

    def onPlusMessage(self):
        def decorator(func):
            self.handlers.append(func)
            return func
        return decorator
    
    def polling(self):
        msgd = []
        while 1:
            for handler in self.handlers:
                data = XUpdater(self.authtoken, self.privatekey, self.getChatsUpdates(), self.ufa, self.proxy)
                if not data.messageId in msgd:
                    msgd.append(data.messageId)
                    handler(data)
                else:msgd.append(data.messageId)

    def onChatMessage(self, chat_object_guid: str) -> dict:
        try:
            datas = self.getChatsUpdates()
            if datas['data']['chats'][0]['object_guid'] == chat_object_guid:
                return datas['data']['chats'][0]
            else:
                return {}
        except Exception as ERROR:
            return {"error": True, "base": str(ERROR)}
    
    @property
    def send_code_types(self) -> tuple:
        return ("SMS", "Internal")

    def sendCode(self, phone_number: str, pass_key: str, send_type: str = "SMS", parsePhoneNumber: bool = True) -> dict:
        if not send_type in self.send_code_types:
            raise ValueError(f"Send type does not available, use send_code_types property to see more of that")
        return self.network.option({"phone_number": self.handlePhoneNumber(phone_number), "pass_key": pass_key,
                                    "send_type": send_type}, "sendCode", self.ufa) if parsePhoneNumber else self.network.option({"phone_number": phone_number, "pass_key": pass_key,
                                    "send_type": send_type}, "sendCode", self.ufa)
    
    def signIn(self, phone_number: str, phone_code: str, phone_code_hash: str, public_key: str, parsePhoneNumber: bool = True) -> dict:
        return self.network.option({"phone_number": phone_number, "phone_code": phone_code,
                                    "phone_code_hash": phone_code_hash, "public_key": public_key}, "signIn", self.ufa) if parsePhoneNumber else self.network.option({"phone_number": self.handlePhoneNumber(phone_number), "phone_code": phone_code,
                                    "phone_code_hash": phone_code_hash, "public_key": public_key}, "signIn", self.ufa)

    def addChannel(self, title: str, description: str = None, member_guids: list = None) -> dict:
        return self.network.option({"title": title, "description": description,
                                    "member_guids": member_guids}, "addChannel", self.ufa) if type(member_guids) == list else self.network.option({"title": title, "description": description,
                                    "member_guids": [member_guids]}, "addChannel", self.ufa)
    
    def addChannelMembers(self, object_guid: str, member_guids: list = None) -> dict:
        return self.network.option({"channel_guid": object_guid, "member_guids": member_guids}, "addChannelMembers", self.ufa) if type(member_guids) == list else \
               self.network.option({"channel_guid": object_guid, "member_guids": [member_guids]}, "addChannelMembers", self.ufa)
    
    @property
    def ban_channel_member_actions(self) -> tuple:
        return ("Set", "Unset")

    def banChannelMember(self, object_guid: str, member_guid: str) -> dict:
        return self.network.option({"channel_guid": object_guid, "member_guid": member_guid,
                                    "action": "Set"}, "banChannelMember", self.ufa)
    
    def banChannelMembers(self, object_guid: str, member_guids: list) -> dict:

        if type(member_guids) != list and type(member_guids) == str:
            member_guids = [member_guids]

        dbs = {}

        for _ in member_guids:
            dbs[_] = self.banChannelMember(object_guid=object_guid, member_guid=_)
        
        return dbs

    def channelPreviewByJoinLink(self, link: str, use_endpoint_hash: bool = True) -> dict:
        return self.network.option({"hash_link": self.endpointHash(link)},
                                   "channelPreviewByJoinLink", self.ufa) if use_endpoint_hash else self.network.option({"hash_link": link},
                                   "channelPreviewByJoinLink", self.ufa)
    
    def checkChannelUsername(self, username: str, replace_tag: bool = True) -> dict:
        return self.network.option({"username": username.replace("@", "")},
                                   "checkChannelUsername", self.ufa) if replace_tag else self.network.option({"username": username},
                                   "checkChannelUsername", self.ufa)
    
    def checkChannelUsernames(self, usernames: list, replace_tag: bool = True) -> dict:
        if not type(usernames) == list:
            raise ValueError("`usernames` parameter in checkChannelUsernames is not list")
        
        dbs = {}

        for username in usernames:
            dbs[username] = self.checkChannelUsername(username=username, replace_tag=replace_tag)

        return dbs
    
    def createChannelVoiceChat(self, channel_guid: str) -> dict:
        return self.network.option({"channel_guid": channel_guid},
                                   "createChannelVoiceChat", self.ufa)
    
    def deleteNoAccessGroupChat(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid},
                                   "deleteNoAccessGroupChat", self.ufa)
    
    def discardChannelVoiceChat(self, channel_guid: str, voice_chat_id: str) -> dict:
        return self.network.option({"channel_guid": channel_guid, 
                                    "voice_chat_id": voice_chat_id}, "discardChannelVoiceChat", self.ufa)
    
    @property
    def chat_history_for_new_members_list(self) -> tuple:
        return ('Hidden', 'Visible')

    def editChannelInfo(self,
                channel_guid: str,
                title: str = None,
                description: str = None,
                channel_type: str = None,
                sign_messages: str = None,
                chat_reaction_setting: dict = None,
                chat_history_for_new_members: str = "Hidden") -> dict:
        
        updatedParameters = []
        inp = {
            "channel_guid": channel_guid
        }

        if title is not None:
            inp['title'] = title
            updatedParameters.append('title')

        if description is not None:
            inp['description'] = description
            updatedParameters.append('description')

        if channel_type is not None:
            inp['channel_type'] = channel_type
            updatedParameters.append('channel_type')

        if sign_messages is not None:
            inp['sign_messages'] = sign_messages
            updatedParameters.append('sign_messages')

        if chat_reaction_setting is not None:
            inp['chat_reaction_setting'] = chat_reaction_setting
            updatedParameters.append('chat_reaction_setting')

        if chat_history_for_new_members is not None:
            if chat_history_for_new_members not in self.chat_history_for_new_members_list:
                raise ValueError('`chat_history_for_new_members` parameter in editChannelInfo is not available, to see more options use `chat_history_for_new_members_list` property.')

            inp['chat_history_for_new_members'] = chat_history_for_new_members
            updatedParameters.append('chat_history_for_new_members')

        inp['updated_parameters'] = updatedParameters

        return self.network.option(inp, "editChannelInfo", self.ufa)
    
    def getBannedGroupMembers(self, group_guid: str, start_id: str = None) -> dict:
        return self.network.option({
            "group_guid": group_guid,
            "start_id": start_id
        }, "getBannedGroupMembers", self.ufa)
    
    def getChannelAdminAccessList(self, channel_guid: str, admin_user_guid: str) -> dict:
        return self.network.option({
            "channel_guid": channel_guid,
            "member_guid": admin_user_guid
        }, "getChannelAdminAccessList", self.ufa)
    
    def getChannelAdminsAccessList(self, channel_guid: str, admins_user_guids: list) -> dict:
        if not type(admins_user_guids) == list:
            raise ValueError("`admins_user_guids` parameter in getChannelAdminsAccessList is not list")
        
        dbs = {}

        for guid in admins_user_guids:
            dbs[guid] = self.getChannelAdminAccessList(channel_guid=channel_guid, admin_user_guid=guid)

        return dbs
    
    def getChannelAdminMembers(self, channel_guid: str, start_id: str = None) -> dict:
        return self.network.option({
            "channel_guid": channel_guid,
            "start_id": start_id
        }, "getChannelAdminMembers", self.ufa)
    
    def getChannelAllMembers(self, channel_guid: str, search_text: str = '', start_id: str = None) -> dict:
        return self.network.option({
            "channel_guid": channel_guid,
            "start_id": start_id
        }, "getChannelAllMembers", self.ufa)
    
    def getChannelInfo(self, channel_guid: str) -> dict:
        return self.network.option({"channel_guid": channel_guid}, "getChannelInfo", self.ufa)
    
    def getChannelLink(self, channel_guid: str) -> dict:
        return self.network.option({"channel_guid": channel_guid}, "getChannelLink", self.ufa)
    
    def getGroupDefaultAccess(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "getGroupDefaultAccess", self.ufa)
    
    def getGroupMentionList(self, group_guid: str, search_mention: str = None) -> dict:
        return self.network.option({"group_guid": group_guid, "search_mention": search_mention}, "getGroupMentionList", self.ufa)
    
    def getGroupVoiceChatUpdates(self, group_guid: str, voice_chat_id: str  ) -> dict:
        return self.network.option({"group_guid": group_guid, "voice_chat_id": voice_chat_id, "state": round(time.time()) - 150}, "getGroupVoiceChatUpdates", self.ufa)
    
    @property
    def join_channel_actions(self) -> tuple:
        return (
            "Join",
            "Remove",
            "Archive"
        )
    
    def joinChannelAction(self, channel_guid: str, action: str) -> dict:
        if not action in self.join_channel_actions:
            raise ValueError("`action` parameter in joinChannelAction does not available, to see more actions print `join_channel_actions` property")
        
        return self.network.option({"channel_guid": channel_guid, "action": action}, "joinChannelAction", self.ufa)
    
    def joinChannelByLink(self, link: str, use_endpoint_hash: bool = True) -> dict:
        return self.network.option({"hash_link": self.endpointHash(link)},
                                   "joinChannelByLink", self.ufa) if use_endpoint_hash else self.network.option({"hash_link": self.endpointHash(link)},
                                   "joinChannelByLink", self.ufa)
    
    def joinGroup(self, link: str, use_endpoint_hash: bool = True) -> dict:
        return self.network.option({"hash_link": self.endpointHash(link)},
                                   "joinGroup", self.ufa) if use_endpoint_hash else self.network.option({"hash_link": self.endpointHash(link)},
                                   "joinGroup", self.ufa)
    
    def leaveGroup(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "leaveGroup", self.ufa)
    
    def leaveGroupVoiceChat(self, group_guid: str, voice_chat_id: str) -> dict:
        return self.network.option({"group_guid": group_guid, "voice_chat_id": voice_chat_id}, "leaveGroupVoiceChat", self.ufa)
    
    def removeChannel(self, channel_guid: str) -> dict:
        return self.network.option({"channel_guid": channel_guid}, "removeChannel", self.ufa)
    
    def seenChannelMessages(self, channel_guid: str, min_id: int, max_id: int) -> dict:
        return self.network.option({"channel_guid": channel_guid, "min_id": min_id, "max_id": max_id}, "seenChannelMessages", self.ufa)
    
    def setChannelLink(self, channel_guid: str) -> dict:
        return self.network.option({"channel_guid": channel_guid}, "setChannelLink", self.ufa)
    
    def changeChannelLink(self, channel_guid: str) -> dict:
        return self.setChannelLink(channel_guid=channel_guid)
    
    def setChannelVoiceChatSetting(self, channel_guid: str, voice_chat_id: str, title: str = None) -> dict:
        inp = {
            "channel_guid": channel_guid,
            "voice_chat_id": voice_chat_id
        }

        updatedParameters = []

        if title is not None:
            inp['title'] = title
            updatedParameters.append("title")

        inp['updated_parameters'] = updatedParameters

        return self.network.option(inp, "setChannelVoiceChatSetting", self.ufa)
    
    def changeChannelVoiceChatSetting(self, channel_guid: str, voice_chat_id: str, title: str = None) -> dict:
        return self.setChannelVoiceChatSetting(channel_guid=channel_guid, voice_chat_id=voice_chat_id, title=title)
    
    @property
    def group_admins_actions(self) -> tuple:
        return (
            "SetAdmin",
            "UnsetAdmin"
        )
    
    def setGroupAdmin(self, group_guid: str, member_guid: str, action: str = "SetAdmin", access_list: list = []) -> dict:
        if not action in self.group_admins_actions:
            raise ValueError("`action` parameter in ( setGroupAdmin / addGroupAdmin ) functions, is not available, to see more actions print `group_admins_actions` property")
        
        if type(access_list) != list and type(access_list) == str:
            access_list = [access_list]

        return self.network.option({"group_guid": group_guid, "member_guid": member_guid,
                                    "action": action, "access_list": access_list}, "setGroupAdmin", self.ufa)
    
    def addGroupAdmin(self, channel_guid: str, member_guid: str, action: str = "SetAdmin", access_list: list = []) -> dict:
        return self.setGroupAdmin(channel_guid=channel_guid, member_guid=member_guid,
                                  action=action, access_list=access_list)
    
    def updateChannelUsername(self, channel_guid: str, username: str, replace_tag: bool = True) -> dict:
        return self.network.option({"channel_guid": channel_guid,
                                    "username": username.replace("@", "")}, "updateChannelUsername", self.ufa) if replace_tag else self.network.option({"channel_guid": channel_guid,
                                    "username": username}, "updateChannelUsername", self.ufa)
    
    def sendMessage(self, chat_object_guid: str, text_message: str, reply_to_message_id: str = None) -> dict:
        metadata = Markdown(text_message).metadata

        metadata['object_guid'] = chat_object_guid
        metadata['reply_to_message_id'] = reply_to_message_id
        metadata['rnd'] = random.random() * 1e6 + 1

        return self.network.option(metadata, "sendMessage", self.ufa)

    def requestSendFile(self, file_name: str, mime: str, size: str) -> dict:
        return self.network.option({"file_name": file_name, "mime": mime, "size": size}, "requestSendFile", self.ufa)
    
    def __sendFileInline(
            self,
            objectGuid:str,
            file:str,
            messageId:str,
            fileName:str,
            type:dict,
            text:str="",
            isSpoil:bool=False,
            customThumbInline:str=None,
            time:int=None,
            performer:str=None
    ) -> dict:
        uploadData:dict = self.network.upload(file=file, fileName=fileName)
        if not uploadData: return

        input = Markdown(text).metadata
        input['file_inline'] = {}
        input['file_inline']['dc_id'] = uploadData["dc_id"]
        input['file_inline']['file_id'] = uploadData["id"]
        input['file_inline']['file_name'] = uploadData['file_name']
        input['file_inline']['size'] = uploadData['size']
        input['file_inline']['mime'] = uploadData['mime']
        input['file_inline']['access_hash_rec'] = uploadData['access_hash_rec']
        input['file_inline']['type'] = type
        input['file_inline']['is_spoil'] = isSpoil
        input['object_guid'] = objectGuid
        input['rnd'] = random.random() * 1e6 + 1
        input['reply_to_message_id'] = messageId


        if type in ["Image", "Video", "Gif", "VideoMessage"]:
            customThumbInline = self.getImageThumbnail(
                customThumbInline
                if isinstance(customThumbInline, bytes)
                else httpx.get(customThumbInline).text
                if self.guessLink(customThumbInline)
                else open(customThumbInline, "rb").read()
            ) if customThumbInline else None

            if not type == "Image":
                videoData:list = self.getVideoData(uploadData["file"])
                input["file_inline"]["time"] = videoData[2] * 1000

            fileSize:list = self.getImageSize(uploadData["file"]) if type == "Image" else videoData[1]
            input["file_inline"]["width"] = fileSize[0]
            input["file_inline"]["height"] = fileSize[1]

            if type == "VideoMessage":
                input["file_inline"]["type"] = "Video"
                input["file_inline"]["is_round"] = True

            input["file_inline"]["thumb_inline"] = customThumbInline or (self.getImageThumbnail(uploadData["file"]) if type == "Image" else videoData[0])

        if type in ["Music", "Voice"]:
            input["file_inline"]["time"] = (time or self.getVoiceDuration(uploadData["file"])) * (1000 if type == "Voice" else 1)

            if type == "Music":
                input["file_inline"]["music_performer"] = performer or self.getMusicArtist(uploadData["file"])


        return self.network.option(
            method="sendMessage",
            input_data=input,
            use_fake_useragent=self.ufa
        )
    
    def downloadSomething(self, accessHashRec:str, fileId:str, dcId:str, size:int, writeFileName: str = None, attempt:int=0, maxAttempts:int=2) -> dict:
        """
        Download Something and Save in Memory
        """
        try:
            downloaded = self.network.download(accessHashRec, fileId, dcId, size)
            fn = self.getFileName(writeFileName) if writeFileName is not None else self.network.generateFileName(self.network.getMimeFromByte(downloaded))

            with open(fn, 'w') as First:
                pass 

            with open(fn, 'wb') as FN:
                FN.write(downloaded)

            return {
                "status": "OK",
                "status_det": "OK",
                "data": {
                    "download_info": {
                        "access_hash_rec": accessHashRec,
                        "file_id": fileId,
                        "dc_id": dcId,
                        "size": size
                    },
                    "local_info": {
                        "writed_file_name": fn,
                        "date_time": time.ctime(time.time())
                    }
                }
            }
        
        except Exception as ERROR:
            return {
                "status": "OK",
                "status_det": "ERROR",
                "description": str(ERROR)
            }
    
    def sendFile(self, objectGuid:str, file:str, messageId:str, text:str, fileName:str) -> dict:
        return self.__sendFileInline(
            objectGuid=objectGuid,
            file=file,
            text=text,
            messageId=messageId,
            fileName=fileName,
            type="File"
        )
    
    def sendImage(self, objectGuid:str, file:str, fileName:str, text:str = None, messageId:str = None, isSpoil:bool = False, thumbInline:str = None) -> dict:
        return self.__sendFileInline(
            objectGuid=objectGuid,
            file=file,
            text=text,
            messageId=messageId,
            fileName=fileName,
            type="Image",
            isSpoil=isSpoil,
            customThumbInline=thumbInline
        )
    
    def sendVideo(self, objectGuid:str, file:str, fileName:str, text:str, messageId:str = None, isSpoil:bool = False, thumbInline:str = None) -> dict:
        return self.__sendFileInline(
            objectGuid=objectGuid,
            file=file,
            text=text,
            messageId=messageId,
            fileName=fileName,
            type="Video",
            isSpoil=isSpoil,
            customThumbInline=thumbInline
        )
    
    def sendVideoMessage(self, objectGuid:str, file:str, fileName:str, text:str, messageId:str = None, thumbInline:str = None) -> dict:
        return self.__sendFileInline(
            objectGuid=objectGuid,
            file=file,
            text=text,
            messageId=messageId,
            fileName=fileName,
            type="VideoMessage",
            customThumbInline=thumbInline
        )
    
    def sendGif(self, objectGuid:str, file:str, fileName:str, text:str, messageId:str = None, thumbInline:str = None) -> dict:
        return self.__sendFileInline(
            objectGuid=objectGuid,
            file=file,
            text=text,
            messageId=messageId,
            fileName=fileName,
            type="Gif",
            customThumbInline=thumbInline
        )
    
    def sendMusic(self, objectGuid:str, file:str, fileName:str, text:str, messageId:str = None, performer = None, thumbInline:str = None) -> dict:
        return self.__sendFileInline(
            objectGuid=objectGuid,
            file=file,
            text=text,
            messageId=messageId,
            fileName=fileName,
            type="Music",
            performer=performer
        )
    
    def sendVoice(self, objectGuid:str, file:str, fileName:str, text:str, messageId:str = None) -> dict:
        return self.__sendFileInline(
            objectGuid=objectGuid,
            file=file,
            text=text,
            messageId=messageId,
            fileName=fileName,
            type="Voice",
            time=self.getVoiceDuration(open(file, 'rb').read())
        )
    
    def sendLocation(self, objectGuid:str, latitude:int, longitude:int, messageId:str = None) -> dict:
        return self.network.option(
            method="sendMessage",
            input={
                "location": {
                    "latitude": latitude,
                    "longitude": longitude
                },
                "object_guid":objectGuid,
                "rnd": random.randint(-99999999, 99999999),
                "reply_to_message_id": messageId
            }
        )
    
    def sendMessageAPICall(self, objectGuid:str, text:str, messageId:str, buttonId:str) ->  dict:
        return self.network.option(
            method="sendMessageAPICall",
            input={
                "text": text,
                "object_guid": objectGuid,
                "message_id": messageId,
                "aux_data": {"button_id": buttonId}
            },
            use_fake_useragent=self.ufa
        )
    
    def editMessage(self, objectGuid, text, messageId) -> dict:
        metadata = self.checkMetadata(text)
        data = {
            "object_guid": objectGuid,
            "text": metadata[1],
            "message_id": messageId,
        }
        if metadata[0] != []:
            data["metadata"] = {"meta_data_parts": metadata[0]}
        return self.network.option(data, "editMessage", self.ufa)
    
    def deleteAvatar(self, object_guid: str, avatar_id: str) -> dict:
        return self.network.option({"object_guid": object_guid, "avatar_id": avatar_id}, "deleteAvatar", self.ufa)
    
    def deleteChatHistory(self, object_guid: str, last_message_id: str) -> dict:
        return self.network.option({"object_guid": object_guid, "last_message_id": last_message_id}, "deleteChatHistory", self.ufa)
    
    def getAbsObjects(self, object_guids: list) -> dict:
        if type(object_guids) == str:
            object_guids = [object_guids]

        return self.network.option({"object_guid": object_guids}, "getAbsObjects", self.ufa)
        
    def abstractionObjects(self, object_guids: list) -> dict:
        return self.getAbsObjects(object_guids=object_guids)
    
    def getAvatars(self, object_guid: str) -> dict:
        return self.network.option({'object_guid': object_guid}, "getAvatars", self.ufa)
    
    def getAvatarsArray(self, object_guids: list) -> dict:
        if not type(object_guids) == list:
            raise ValueError("`object_guids` parameter of method getAvatarsArray is not list")
        
        dbs = {}

        for guid in object_guids:
            dbs[guid] = self.getAvatars(guid)

        return dbs
    
    def getChats(self, start_id: str = None) -> dict:
        return self.network.option({"start_id": start_id}, "getChats", self.ufa)
    
    def getLinkFromAppUrl(self, app_url: str) -> dict:
        return self.network.option({"app_url": app_url}, "getLinkFromAppUrl", self.ufa)
    
    @property
    def search_chat_messages_types(self) -> tuple:
        return (
            "Text",
            "Hashtag"
        )

    def searchTextMessages(self, object_guid: str, text: str) -> dict:
        return self.network.option({"object_guid": object_guid, "search_text": text, "type": "Text"}, "searchChatMessages", self.ufa)
    
    def searchHashtagMessages(self, object_guid: str, hashtag: str) -> dict:
        return self.network.option({"object_guid": object_guid, "search_text": hashtag, "type": "Hashtag"}, "searchChatMessages", self.ufa)
    
    def seenChats(self, seen_dictionary: dict) -> dict:
        return self.network.option({"seen_list": seen_dictionary}, "seenChats", self.ufa)
    
    @property
    def chat_activities(self) -> tuple:
        return (
            "Typing",
            "Uploading",
            "Recording"
        )

    def sendChatActivity(self, object_guid: str, activity: str = "Typing") -> dict:
        if not activity in self.chat_activities:
            raise ValueError("`activity` parameter does not available in sendChatActivity, to see more options print `chat_activities` property")
        
        return self.network.option({
            "object_guid": object_guid,
            "activity": activity
        }, "sendChatActivity", self.ufa)
    
    @property
    def chat_actions(self) -> tuple:
        return ('Mute', 'Unmute')

    def setActionChat(self, object_guid: str, action: str = "Mute") -> dict:
        if not action in self.chat_actions:
            raise ValueError("`action` parameter does not available in setActionChat, to see more options print `chat_actions` property")
        
        return self.network.option({"object_guid": object_guid, "action": action}, "setActionChat", self.ufa)
    
    def uploadAvatar(self, object_guid: str, image: str) -> dict:
        if not os.path.exists(image):
            raise ValueError("`image` parameter, get an unexist path")
        
        database = {}

        if type(image) == str:
            database['file_name'] = image.split("/")[-1]
        
        else:
            database['file_name'] = "rubixImage.jpg"

        uploaded = self.network.upload(image, database["file_name"], os.path.getsize(image))

        return self.network.option({
            "object_guid": object_guid,
            "thumnail_file_id": uploaded['id'],
            "main_file_id": uploaded['id']
        }, "uploadAvatar", self.ufa)
    
    def addAddressBook(self, phone: str, first_name: str, last_name: str = '') -> dict:
        return self.network.option({"phone": phone, "first_name": first_name, "last_name": last_name}, "addAddressBook", self.ufa)
    
    def deleteContact(self, user_guid: str) -> dict:
        return self.network.option({"user_guid": user_guid}, "deleteContact", self.ufa)
    
    def getContacts(self, start_id: str = None) -> dict:
        return self.network.option({"start_id": start_id}, "getContacts", self.ufa)
    
    def getContactsUpdates(self) -> dict:
        return self.network.option({"state": round(time.time()) - 150}, "getContactsUpdates", self.ufa)
    
    def getObjectByUsername(self, username: str, replace_tag: bool = True) -> dict:
        return self.network.option({"username": username.replace("@", "")}, "getObjectByUsername", self.ufa) if replace_tag else \
               self.network.option({"username": username}, "getObjectByUsername", self.ufa)
    
    def getProfileLinkItems(self, object_guid: str) -> dict:
        return self.network.option({"object_guid": object_guid}, "getProfileLinkItems", self.ufa)
    
    def getRelatedObjects(self, object_guid: str) -> dict:
        return self.network.option({"object_guid": object_guid}, "getRelatedObjects", self.ufa)
    
    def getTranscription(self, message_id: str, transcription_id: str) -> dict:
        return self.network.option({"message_id": message_id, "transcription_id": transcription_id}, "getTranscription", self.ufa)
    
    def searchGlobalObjects(self, search_text: str) -> dict:
        return self.network.option({"search_text": search_text}, "searchGlobalObjects", self.ufa)
    
    def addToMyGifSet(self, object_guid: str, message_id: str) -> dict:
        return self.network.option({"object_guid": object_guid, "message_id": message_id}, "addToMyGifSet", self.ufa)
    
    def getMyGifSet(self) -> dict:
        return self.network.option({}, "getMyGifSet", self.ufa)
    
    def removeFromMyGifSet(self, file_id: str) -> dict:
        return self.network.option({"file_id": file_id}, "removeFromMyGifSet", self.ufa)
    
    def addGroup(self, title: str, member_guids: list) -> dict:
        if type(member_guids) == str:
            member_guids = [member_guids]

        return self.network.option({"title": title, "member_guids": member_guids}, "addGroup", self.ufa)
    
    def addGroupMembers(self, group_guid: str, member_guids: list) -> dict:
        if type(member_guids) == str:
            member_guids = [member_guids]
        
        return self.network.option({"group_guid": group_guid, "member_guids": member_guids}, "addGroupMembers", self.ufa)
    
    @property
    def ban_group_member_actions(self) -> tuple:
        return (
            "Set",
            "Unset"
        )

    def banGroupMember(self, group_guid: str, member_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid, "member_guid": member_guid,
                                    "action": "Set"}, "banGroupMember", self.ufa)
    
    def createGroupVoiceChat(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "createGroupVoiceChat", self.ufa)
    
    def deleteNoAccessGroupChat(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "deleteNoAccessGroupChat", self.ufa)
    
    def editGroupInfo(self,
                group_guid: str,
                title: str = None,
                description: str = None,
                slow_mode: str = None,
                event_messages: bool = None,
                sign_messages: str = None,
                chat_reaction_setting: dict = None,
                chat_history_for_new_members: str = "Hidden") -> dict:
        
        updatedParameters = []
        inp = {
            "group_guid": group_guid
        }

        if title is not None:
            inp['title'] = title
            updatedParameters.append('title')

        if description is not None:
            inp['description'] = description
            updatedParameters.append('description')

        if slow_mode is not None:
            inp['slow_mode'] = slow_mode
            updatedParameters.append("slow_mode")

        if event_messages is not None:
            inp['event_messages'] = event_messages
            updatedParameters.append("event_messages")

        if sign_messages is not None:
            inp['sign_messages'] = sign_messages
            updatedParameters.append('sign_messages')

        if chat_reaction_setting is not None:
            inp['chat_reaction_setting'] = chat_reaction_setting
            updatedParameters.append('chat_reaction_setting')

        if chat_history_for_new_members is not None:
            if chat_history_for_new_members not in self.chat_history_for_new_members_list:
                raise ValueError('`chat_history_for_new_members` parameter in editChannelInfo is not available, to see more options use `chat_history_for_new_members_list` property.')

            inp['chat_history_for_new_members'] = chat_history_for_new_members
            updatedParameters.append('chat_history_for_new_members')

        inp['updated_parameters'] = updatedParameters

        return self.network.option(inp, "editChannelInfo", self.ufa)
    
    def getBannedGroupMembers(self, group_guid: str, start_id: str = None) -> dict:
        return self.network.option({"group_guid": group_guid, "start_id": start_id}, "getBannedGroupMembers", self.ufa)
    
    def getGroupAdminAccessList(self, group_guid: str, member_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid, "member_guid": group_guid}, "getGroupAdminAccessList", self.ufa)
    
    def getGroupAdminMembers(self, group_guid: str, start_id: str = None) -> dict:
        return self.network.option({"group_guid": group_guid, "start_id": start_id}, "getGroupAdminMembers", self.ufa)
    
    def getGroupAllMembers(self, group_guid: str, search_text: str = None, start_id: str = None) -> dict:
        return self.network.option({"group_guid": group_guid, "search_text": search_text, "start_id": start_id}, "getGroupAllMembers", self.ufa)
    
    def getGroupDefaultAccess(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "getGroupDefaultAccess", self.ufa)
    
    def getGroupInfo(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "getGroupInfo", self.ufa)
    
    def getGroupLink(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "getGroupInfo", self.ufa)
    
    def getGroupMentionList(self, group_guid: str, search_mention: str = None) -> dict:
        return self.network.option({"group_guid": group_guid, "search_mention": search_mention}, "getGroupMentionList", self.ufa)
    
    def getGroupVoiceChatUpdates(self, group_guid: str, voice_chat_id: str) -> dict:
        return self.network.option({"group_guid": group_guid, "voice_chat_id": voice_chat_id, "state": round(time.time()) - 150}, "getGroupVoiceChatUpdates", self.ufa)
    
    def groupPreviewByJoinLink(self, link: str, use_endpoint_hash: bool = True) -> dict:
        return self.network.option({"hash_link": self.endpointHash(link)}, "groupPreviewByJoinLink", self.ufa) if use_endpoint_hash else \
               self.network.option({"hash_link": link}, "groupPreviewByJoinLink", self.ufa)
    
    def leaveGroupVoiceChat(self, group_guid: str, voice_chat_id: str) -> dict:
        return self.network.option({"group_guid": group_guid, "voice_chat_id": voice_chat_id}, "leaveGroupVoiceChat", self.ufa)
    
    def removeGroup(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "removeGroup", self.ufa)
    
    def setGroupDefaultAccess(self, group_guid: str, access_list: list = []) -> dict:
        if type(access_list) == str:
            access_list = [access_list]

        return self.network.option({"group_guid": group_guid, "access_list": access_list}, "setGroupDefaultAccess", self.ufa)
    
    def setGroupLink(self, group_guid: str) -> dict:
        return self.network.option({"group_guid": group_guid}, "setGroupLink", self.ufa)
    
    def changeGroupLink(self, group_guid: str) -> dict:
        return self.setGroupLink(group_guid=group_guid)
    
    def setGroupVoiceChatSetting(self, group_guid: str, voice_chat_id: str, title: str = None) -> dict:
        inp = {
            "group_guid": group_guid,
            "voice_chat_id": voice_chat_id
        }

        updatedParameters = []

        if title is not None:
            inp['title'] = title
            updatedParameters.append("title")

        inp['updated_parameters'] = updatedParameters

        return self.network.option(inp, "setGroupVoiceChatSetting", self.ufa)
    
    def checkUserUsername(self, username: str, replace_tag: bool = True) -> dict:
        return self.network.option({"username": username.replace("@", "")}, "checkUserUsername", self.ufa) if replace_tag else \
               self.network.option({"username": username}, "checkUserUsername", self.ufa)
    
    def deleteUserChat(self, user_guid: str, last_deleted_message_id: str) -> dict:
        return self.network.option({"user_guid": user_guid, "last_deleted_message_id": last_deleted_message_id}, "deleteUserChat", self.ufa)
    
    @property
    def block_user_actions(self) -> tuple:
        return (
            "Block",
            "Unblock"
        )

    def blockUser(self, user_guid: str) -> dict:
        return self.network.option({"user_guid": user_guid, "action": "Block"}, "setBlockUser", self.ufa)
    
    def getChatInfo(self, guid: str) -> dict:
        type = self.guessGuid(guid=guid)
        return self.network.option({f"{type.lower()}_guid": guid}, f"get{type}Info", self.ufa)
    
    def getMessagesInfo(self, object_guid: str, message_ids: list) -> dict:
        if not type(message_ids) == list and type(message_ids) == str:
            message_ids = [message_ids]

        return self.network.option({"object_guid": object_guid, "message_ids": [message_ids]}, "getMessagesByID")
    
    def getMessagesInfoByArray(self, object_guids: list, message_ids: list) -> dict:
        if not type(object_guids) == list and type(object_guids) == str:
            object_guids = [object_guids]

        if not type(message_ids) == list and type(message_ids) == str:
            message_ids = [message_ids]

        if not len(object_guids) == message_ids:
            raise ValueError("The Length of `object_guids` and `message_ids` are not equal,\
                              Please Set them together")
        
        dbs = {}

        for guid in object_guids:
            for message in message_ids:
                dbs[guid] = self.getMessagesInfo(message)
        
        return dbs
    
    @property
    def on_message_reaction_actions(self) -> tuple:
        return (
            "Add",
            "Remove"
        )

    def actionOnMessageReaction(self, object_guid: str, message_id: str, reaction_id: int = None, action: str = "Add") -> dict:
        if not action in self.on_message_reaction_actions:
            raise ValueError(f"The action '{action}' of method `actionOnMessageReaction` is not allow to use, \
                             for see More actions, print `on_message_reaction_actions` property")
        
        return self.network.option({
            "object_guid": object_guid,
            "message_id": message_id,
            "reaction_id": reaction_id,
            "action": action
        }, "actionOnMessageReaction", self.ufa)
    
    @property
    def question_types(self) -> tuple:
        return (
            "Regular",
            "Quiz"
        )
    
    def createPoll(
            self,
            object_guid: str,
            question: str,
            options: list,
            type: str = 'Regular',
            is_anonymous: bool = True,
            allows_multiple_answers: bool = True,
            correct_option_index: int = 0,
            explanation: str = None,
            reply_to_message_id: str = None,
    ) -> dict:
        if len(options) <= 1:
            raise ValueError('The `options` argument must have more than two string values.')

        if not type in ('Quiz', 'Regular'):
            raise ValueError('The `type` of question is not allowed, print `question_types` property to see types')
        

        input = {
            'object_guid': object_guid,
            'question': question,
            'options': options,
            'allows_multiple_answers': allows_multiple_answers,
            'is_anonymous': is_anonymous,
            'reply_to_message_id': reply_to_message_id,
            'type': type,
            'rnd': int(random() * 1e6 + 1),
        }

        if type == 'Quiz':
            input['correct_option_index'] = correct_option_index
            input['explanation'] =  explanation

        return self.network.option(input, "createPoll", self.ufa)
    
    @property
    def delete_message_types(self) -> tuple:
        return (
            "Global",
            "Local"
        )

    def deleteMessage(self, object_guid: str, message_id: str, is_globaly: bool = True) -> dict:
        return self.network.option({
            "object_guid": object_guid,
            "message_ids": [message_id],
            "type": "Global" if is_globaly else "Local"
        }, "deleteMessages", self.ufa)
    
    def deleteMessages(self, object_guid: str, message_ids: list, is_globaly: bool = True) -> dict:
        return self.network.option({
            "object_guid": object_guid,
            "message_ids": message_ids,
            "type": "Global" if is_globaly else "Local"
        }, "deleteMessages", self.ufa)
    
    def forwardMessage(self, from_object_guid: str, to_object_guid: str, message_id: str) -> dict:
        return self.network.option({
            "from_object_guid": from_object_guid,
            "to_object_guid": to_object_guid,
            "message_ids": [message_id]
        }, "forwardMessages", self.ufa)
    
    def forwardMessage(self, from_object_guid: str, to_object_guid: str, message_ids: list) -> dict:
        return self.network.option({
            "from_object_guid": from_object_guid,
            "to_object_guid": to_object_guid,
            "message_ids": message_ids
        }, "forwardMessages", self.ufa)
    
    def getMessageLink(self, object_guid: str, message_id: str) -> dict:
        return self.network.option({
            "object_guid": object_guid,
            "message_id": message_id
        }, "getMessageShareUrl", self.ufa)
    
    def getMessagesInterval(self, object_guid: str, middle_message_id: str) -> dict:
        return self.network.option({
            "object_guid": object_guid,
            "middle_message_id": middle_message_id
        }, "getMessagesInterval", self.ufa)
    
    def getPollOptionsVoters(self, poll_id: str, selection_index: int, start_id: str = None) -> dict:
        return self.network.option({
            "poll_id": poll_id,
            "selection_index": selection_index,
            "start_id": start_id
        }, "getPollOptionsVoters", self.ufa)
    
    def getPollStatus(self, poll_id: str) -> dict:
        return self.network.option({
            "poll_id": poll_id
        }, "getPollStatus", self.ufa)
    
    def reaction(self, object_guid: str, message_id: str, reaction_id: int) -> dict:
        return self.actionOnMessageReaction(object_guid=object_guid, message_id=message_id, \
                                            reaction_id=reaction_id)
    
    def remove_reaction(self, object_guid: str, message_id: str, reaction_id: int) -> dict:
        return self.actionOnMessageReaction(object_guid=object_guid, message_id=message_id, \
                                            reaction_id=reaction_id, action="Remove")
    
    @property
    def messages_pup(self) -> tuple:
        return (
            "Pin",
            "Unpin"
        )

    def pin(self, object_guid: str, message_id: str) -> dict:
        return self.network.option({
            "object_guid": object_guid,
            "message_id": message_id,
            "action": "Pin"
        }, "setPinMessage", self.ufa)
    
    def unpin(self, object_guid: str, message_id: str) -> dict:
        return self.network.option({
            "object_guid": object_guid,
            "message_id": message_id,
            "action": "Unpin"
        }, "setPinMessage", self.ufa)
    
    def votePoll(self, poll_id: str, selection_index: int) -> dict:
        return self.network.option({
            "poll_id": poll_id,
            "selection_index": selection_index
        }, "votePoll", self.ufa)
    
    def sendVote(self, poll_id: str, selection_index: int) -> dict:
        return self.votePoll(poll_id=poll_id, \
                             selection_index=selection_index)
    
    def deleteFolder(self, folder_id: int) -> dict:
        return self.network.option({
            "folder_id": folder_id
        }, "deleteFolder", self.ufa)
    
    def getBlockedUsers(self) -> dict:
        return self.network.option({}, "getBlockedUsers", self.ufa)
    
    def getFolders(self) -> dict:
        return self.network.option({
            "last_state": time.time() - 150
        }, "getFolders", self.ufa)
    
    def getSessions(self) -> dict:
        return self.network.option({}, "getMySessions", self.ufa)
    
    def getPrivacySetting(self) -> dict:
        return self.network.option({}, "getPrivacySetting", self.ufa)
    
    def getSuggestedFolders(self) -> dict:
        return self.network.option({}, "getSuggestedFolders", self.ufa)
    
    def getTwoPasscodeStatus(self) -> dict:
        return self.network.option({}, "getTwoPasscodeStatus", self.ufa)
    
    @property
    def last_online_params(self) -> tuple:
        return (
            'Nobody',
            'Everybody',
            'MyContacts'
        )
    
    # Thanks to Rubpy for this Method

    def setSetting(
            self,
            show_my_last_online: str = None,
            show_my_phone_number: str = None,
            show_my_profile_photo: str = None,
            link_forward_message: str = None,
            can_join_chat_by: str = None,
    ) -> dict:
        input = {}
        updated_parameters = []

        if isinstance(show_my_last_online, str):
            if show_my_last_online not in ('Nobody', 'Everybody', 'MyContacts'):
                raise ValueError('The `show_my_last_online` can only be in `["Nobody", "Everybody", "MyContacts"]`.')

            input['show_my_last_online'] = show_my_last_online
            updated_parameters.append('show_my_last_online')

        if isinstance(show_my_phone_number, str):
            if show_my_phone_number not in ('Nobody', 'Everybody', 'MyContacts'):
                raise ValueError('The `show_my_phone_number` can only be in `["Nobody", "Everybody", "MyContacts"]`.')

            input['show_my_phone_number'] = show_my_phone_number
            updated_parameters.append('show_my_phone_number')

        if isinstance(show_my_profile_photo, str):
            if show_my_profile_photo not in ('Everybody', 'MyContacts'):
                raise ValueError('The `show_my_profile_photo` can only be in `["Everybody", "MyContacts"]`.')

            input['show_my_profile_photo'] = show_my_profile_photo
            updated_parameters.append('show_my_profile_photo')

        if isinstance(link_forward_message, str):
            if link_forward_message not in ('Nobody', 'Everybody', 'MyContacts'):
                raise ValueError('The `link_forward_message` can only be in `["Nobody", "Everybody", "MyContacts"]`.')

            input['link_forward_message'] = link_forward_message
            updated_parameters.append('link_forward_message')

        if isinstance(can_join_chat_by, str):
            if can_join_chat_by not in ('Everybody', 'MyContacts'):
                raise ValueError('The `can_join_chat_by` can only be in `["Everybody", "MyContacts"]`.')

            input['can_join_chat_by'] = can_join_chat_by
            updated_parameters.append('can_join_chat_by')

        input['updated_parameters'] = updated_parameters

        return self.network.option(input, 'SetSetting', self.ufa)
    
    def setupTwoStepVerification(self, password: str, hint: str, recovery_email: str = None) -> dict:
        return self.network.option({
            "password": password,
            "hint": hint,
            "recovery_email": recovery_email
        }, "setupTwoStepVerification", self.ufa)
    
    def terminateSession(self, session_key: str) -> dict:
        return self.network.option({
            "session_key": session_key
        }, "terminateSession", self.ufa)
    
    def update_profile(
            self,
            first_name: str= None,
            last_name: str = None,
            bio: str = None,
    ) -> dict:
        if first_name and last_name and bio is None:
            raise ValueError('All parameters are None.')

        input = {'updated_parameters': []}

        if first_name is not None:
            input['updated_parameters'].append('first_name')
            input['first_name'] = first_name

        if last_name is not None:
            input['updated_parameters'].append('last_name')
            input['last_name'] = last_name

        if bio is not None:
            input['updated_parameters'].append('bio')
            input['bio'] = bio

        return self.network.option(input, "updateProfile", self.ufa)
    
    def updateUsername(self, username: str) -> dict:
        return self.network.option({
            "username": username.replace("@", "")
        }, "updateUsername", self.ufa)
    
    def addSticker(self, sticker_set_id: str) -> dict:
        return self.network.option({
            "sticker_set_id": sticker_set_id,
            "actoin": "Add"
        }, "actionOnStickerSet", self.ufa)
    
    def removeSticker(self, sticker_set_id: str) -> dict:
        return self.network.option({
            "sticker_set_id": sticker_set_id,
            "actoin": "Remove"
        }, "actionOnStickerSet", self.ufa)
    
    def getMyStickerSets(self) -> dict:
        return self.network.option({}, "getMyStickerSets", self.ufa)
    
    def getStickerSetById(self, sticker_set_id: int) -> dict:
        return self.network.option({
            "sticker_set_id": sticker_set_id
        }, "getStickerSetById", self.ufa)
    
    def getStickersByEmoji(
            self,
            emoji: str,
    ) -> dict:
        return self.network.option(
            {'emoji': emoji, 'suggest_by': "Add"},
            "getStickersByEmoji",
            self.ufa
        )
    
    def getStickersBySetIds(self, sticker_set_ids: list) -> dict:
        return self.network.option({
            "sticker_set_ids": sticker_set_ids
        }, "GetStickersBySetIDs", self.ufa)
    
    def getTrendStickerSets(self, start_id: str = None):
        return self.network.option({
            "start_id": start_id
        }, "getTrendStickerSets", self.ufa)
    
    def searchStickers(
            self,
            search_text: str = '',
            start_id: str = None,
    ) -> dict:
        return self.network.option({
            "search_text": search_text,
            "start_id": start_id
        }, "searchStickers", self.ufa)
    
    # Thanks to Rubpy for Below Methods

    def heartbeater(self, chat_guid: str, voice_chat_id: str):
        while True:
            try:
                self.getGroupVoiceChatUpdates(chat_guid, voice_chat_id)
                time.sleep(10)

            except Exception:
                continue

    def speaking(self, chat_guid: str, voice_chat_id):
        while True:
            try:
                self.send_group_voice_chat_activity(chat_guid, voice_chat_id)
                time.sleep(1)

            except Exception:
                continue

    def playOnVoiceChat(self, chat_guid: str, music_path: str, loop: bool = False):
        if aiortc is None:
            return False

        class AudioFileTrack(aiortc.MediaStreamTrack):
            kind: str = 'audio'

            def __init__(self, player):
                super().__init__() 
                self.player = player

            async def recv(self):
                frame = self.player.audio.recv()
                return frame

        chat_info = self.getChatInfo(chat_guid)
        voice_chat_id = chat_info['data']['chat']['group_voice_chat_id'] if chat_guid.startswith("g0") else chat_info['data']['chat']['channel_voice_chat_id']

        if voice_chat_id is None:
            voice_chat = (self.createGroupVoiceChat(chat_guid) if chat_guid.startswith('g0') else
                          self.createChannelVoiceChat(chat_guid))
            voice_chat_id = voice_chat['data']['chat']['voice_chat_id']
            if voice_chat_id is None:
                voice_chat_id = (voice_chat['data']['group']['voice_chat_id'] if chat_guid.startswith('g0') else
                                voice_chat['data']['channel']['voice_chat_id'])

        print(f'Voice chat created and started on chat guid: {chat_guid} and voice id: {voice_chat_id}...')

        pc = aiortc.RTCPeerConnection()
        track = AudioFileTrack(MediaPlayer(music_path, music_path.split('.')[-1], loop=loop, decode=True))
        pc.addTrack(track)

        sdp_offer_local = pc.createOffer()
        pc.setLocalDescription(sdp_offer_local)

        connect = self.createGroupVoiceChat(chat_guid)
        sdp_offer = connect['data']['sdp_answer_data']

        self.set_voice_chat_state(chat_guid, voice_chat_id)
        self.speaking(chat_guid, voice_chat_id)
        remote_description = aiortc.RTCSessionDescription(sdp_offer, 'answer')
        self.heartbeat(chat_guid, voice_chat_id)
        pc.setRemoteDescription(remote_description)

        @pc.on('iceconnectionstatechange')
        def on_iceconnectionstatechange():
            print(f'ICE connection state is: {pc.iceConnectionState}')

        @pc.on('connectionstatechange')
        def on_connectionstatechange():
            print(f'Connection state is: {pc.connectionState}')

        @pc.on('track')
        def on_track(event):
            print(f'Track {event}')

        return True
    
# Hello to you who read source until here :D
