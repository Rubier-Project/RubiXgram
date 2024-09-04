from .network import XNetwork
import random
import json
import re
from typing import Union, Dict

class UNKNOWN(object):
    def __str__(self) -> str:
        return "UNKNOWN"

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
    
class ForwardedFrom(object):
    def __init__(self, forward_result: dict = {}):
        self.forward_result = forward_result
        self.keys: list = list(self.forward_result.keys())
        self.type_from: Union[str, UNKNOWN] = self.forward_result['type_from'] if "type_from" in self.keys else UNKNOWN
        self.message_id: Union[str, UNKNOWN] = self.forward_result['message_id'] if "message_id" in self.keys else UNKNOWN
        self.object_guid: Union[str, UNKNOWN] = self.forward_result['object_guid'] if "object_guid" in self.keys else UNKNOWN

    def __str__(self) -> dict:
        return json.dumps(self.forward_result, indent=2)

class FileInlineTypes(object):
    def __init__(self) -> None:
        self.IMAGE = "Image"
        self.MUSIC = "Music"
        self.VIDEO = "Video"
        self.VIDEO_MESSAGE = "Video",
        self.VOICE = "Voice"
        self.GIF = "Gif"
        self.FILE = "File"

    def __str__(self) -> str:
        return json.dumps({
            "IMAGE": self.IMAGE,
            "MUSIC": self.MUSIC,
            "GIF": self.GIF,
            "FILE": self.FILE,
            "VOICE": self.VOICE,
            "VIDEO": self.VIDEO,
            "VIDEO_MESSAGE": self.VIDEO_MESSAGE
        }, indent=2)

class FileInline(object):
    def __init__(self, file_inline_result: dict = {}):
        self.file = file_inline_result
        self.keys: list = list(self.file.keys())
        self.id: Union[int, UNKNOWN] = self.file['file_id'] if "file_id" in self.keys else UNKNOWN
        self.mime: Union[str, UNKNOWN] = self.file['mime'] if "mime" in self.keys else UNKNOWN
        self.dc_id: Union[int, UNKNOWN] = self.file['dc_id'] if "dc_id" in self.keys else UNKNOWN
        self.access_hash_rec: Union[str, UNKNOWN] = self.file['access_hash_rec'] if "access_hash_rec" in self.keys else UNKNOWN
        self.name: Union[str, UNKNOWN] = self.file['file_name'] if "file_name" in self.keys else UNKNOWN
        self.thumb_inline: Union[str, UNKNOWN] = self.file['thumb_inline'] if "thumb_inline" in self.keys else UNKNOWN
        self.width: Union[int, UNKNOWN] = self.file['width'] if "width" in self.keys else UNKNOWN
        self.height: Union[int, UNKNOWN] = self.file['height'] if "height" in self.keys else UNKNOWN
        self.time: Union[int, UNKNOWN] = self.file['time'] if "time" in self.keys else UNKNOWN
        self.size: Union[int, UNKNOWN] = self.file['size'] if "size" in self.keys else UNKNOWN
        self.type: Union[str, UNKNOWN] = self.file['type'] if "type" in self.keys else UNKNOWN
        self.is_round: Union[bool, UNKNOWN] = self.file['is_round'] if "is_round" in self.keys else UNKNOWN
        self.is_spoil: Union[bool, UNKNOWN] = self.file['is_spoil'] if "is_spoil" in self.keys else UNKNOWN

    def __str__(self) -> str:
        return json.dumps(self.file, indent=2)
    
class FileInlineMusic(FileInline):
    def __init__(self, file_inline_result: Dict = {}):
        super().__init__(file_inline_result)
        self.music_performer: Union[str, UNKNOWN] = self.file['music_performer'] if "music_performer" in self.keys else UNKNOWN
        del self.thumb_inline

class FileInlineVoice(FileInline):
    def __init__(self, file_inline_result: Dict = {}):
        super().__init__(file_inline_result)
        del self.thumb_inline

class FileInlineFile(FileInline):
    def __init__(self, file_inline_result: Dict = {}):
        super().__init__(file_inline_result)
        del self.thumb_inline

class FileInlineGif(FileInline):
    def __init__(self, file_inline_result: Dict = {}):
        super().__init__(file_inline_result)

class FileInlineImage(FileInline):
    def __init__(self, file_inline_result: Dict = {}):
        super().__init__(file_inline_result)

class FileInlineVideo(FileInline):
    def __init__(self, file_inline_result: Dict = {}):
        super().__init__(file_inline_result)

class FileInlineVideoMessage(FileInline):
    def __init__(self, file_inline_result: Dict = {}):
        super().__init__(file_inline_result)

class MapView(object):
    def __init__(self, map_view: dict):
        self.map = map_view
        self.keys: list = list(self.map.keys())
        self.tile_side_count: Union[int, UNKNOWN] = self.map['tile_side_count'] if "tile_side_count" in self.keys else UNKNOWN
        self.tile_urls: Union[list, UNKNOWN] = self.map['tile_urls'] if "tile_urls" in self.keys else UNKNOWN
        self.x_loc: Union[float, UNKNOWN] = self.map['x_loc'] if "x_loc" in self.keys else UNKNOWN
        self.y_loc: Union[float, UNKNOWN] = self.map['y_loc'] if "y_loc" in self.keys else UNKNOWN

    def __str__(self) -> str:
        return json.dumps(self.map, indent=2)

class Location(object):
    def __init__(self, location_result: dict):
        self.location = location_result
        self.keys: list = list(self.location.keys())
        self.longitude: Union[float, UNKNOWN] = self.location['longitude'] if "longitude" in self.keys else UNKNOWN
        self.latitude: Union[float, UNKNOWN] = self.location['latitude'] if "latitude" in self.keys else UNKNOWN
        self.map_view: Union[MapView, UNKNOWN] = MapView(self.location['map_view']) if "map_view" in self.keys else UNKNOWN

    def __str__(self) -> str:
        return json.dumps(self.location, indent=2)

class Contact(object):
    def __init__(self, contact_result: dict) -> None:
        self.contact = contact_result
        self.keys: list = list(self.contact.keys())
        self.phone_number: Union[str] = self.contact['phone_number']
        self.first_name: Union[str] = self.contact['first_name']
        self.last_name: Union[str] = self.contact['last_name']
        self.user_guid: Union[str] = self.contact['user_guid']
        self.vcard: Union[str] = self.contact['vcard']

    def __str__(self) -> str:
        return json.dumps(self.contact, indent=2)

class ReplyObjects(object):
    def __init__(self, jsres: dict = {}):
        self.jsres = jsres
        self.keys: list = list(self.jsres.keys())
        self.file_types = FileInlineTypes()
        self.message_id: Union[str] = self.jsres['message_id'] if 'message_id' in self.keys else ""
        self.text: Union[str] = self.jsres['text'] if "text" in self.keys else ""
        self.reply_to_message_id: Union[str] = self.jsres['reply_to_message_id'] if "reply_to_message_id" in self.keys else ""
        self.message_time: Union[str, UNKNOWN] = self.jsres['time'] if "time" in self.keys else UNKNOWN
        self.type: Union[str, UNKNOWN] = self.jsres['file_inline']['type'] if "file_inline" in self.jsres.keys() and "type" in self.jsres['file_inline'].keys() else UNKNOWN
        self.author_type: Union[str, UNKNOWN] = self.jsres['author_type'] if "author_type" in self.keys else UNKNOWN
        self.is_allow_transcription: Union[bool, UNKNOWN] = self.jsres['allow_transcription'] if "allow_transcription" in self.keys else UNKNOWN
        self.is_edited: Union[bool, UNKNOWN] = self.jsres['is_edited'] if "is_edited" in self.keys else UNKNOWN
        self.is_reply: Union[bool] = self.jsres['is_reply'] if "is_reply" in self.keys else ""
        self.location: Union[Location, UNKNOWN] = Location(self.chat_result['location']) if "location" in self.keys else UNKNOWN
        self.file_inline: Union[
            FileInlineImage, FileInlineGif,
            FileInlineFile, FileInlineMusic,
            FileInlineVoice, FileInlineVideo,
            FileInlineVideoMessage, UNKNOWN
        ] = UNKNOWN if not "file_inline" in self.keys else FileInlineImage(self.jsres['file_inline']) if self.type == self.file_types.IMAGE else FileInlineGif(self.jsres['file_inline']) if self.type == self.file_types.GIF else \
            FileInlineFile(self.jsres['file_inline']) if self.type == self.file_types.FILE else FileInlineMusic(self.jsres['file_inline']) if self.type == self.file_types.MUSIC else FileInlineVoice(self.jsres['file_inline']) if self.type == self.file_types.VOICE \
            else FileInlineVideo(self.jsres['file_inline']) if self.type in ( self.file_types.VIDEO, self.file_types.VIDEO_MESSAGE ) else UNKNOWN

    def __str__(self) -> str:
        return json.dumps(self.jsres, indent=2)

class Avatar(object):
    def __init__(self, avatar_result: dict = {}):
        self.data: Dict = avatar_result
        self.keys = self.data.keys()
        self.id: Union[str, UNKNOWN] = self.data['file_id'] if "file_id" in self.keys else UNKNOWN
        self.mime: Union[str, UNKNOWN] = self.data['mime'] if "mime" in self.keys else UNKNOWN
        self.dc_id: Union[str, UNKNOWN] = self.data['dc_id'] if "dc_id" in self.keys else UNKNOWN
        self.access_hash_rec: Union[str, UNKNOWN] = self.data['access_hash_rec'] if "access_hash_rec" in self.keys else UNKNOWN

    def __str__(self) -> str:
        return json.dumps(self.data, indent=2)


class ChatType(object):
    def __init__(self, chat_result) -> None:
        self.chat_result: dict = chat_result
        self.keys: list = list(self.chat_result.keys())
        self.id: str = self.chat_result['object_guid']
        self.access: list = self.chat_result['access'] if "access" in self.keys else []
        self.count_unseen: int = self.chat_result['count_unseen'] if "count_unseen" in self.keys else UNKNOWN
        self.is_mute: Union[bool, UNKNOWN] = self.chat_result['is_mute'] if "is_mute" in self.keys else UNKNOWN
        self.is_pinned: Union[bool, UNKNOWN] = self.chat_result['is_pinned'] if "is_pinned" in self.keys else UNKNOWN
        self.status: Union[str, UNKNOWN] = self.chat_result['status'] if "status" in self.keys else UNKNOWN
        self.avatar: Union[Avatar, UNKNOWN] = Avatar(self.chat_result['abs_object']['avatar_thumbnail']) if "abs_object" in self.keys and "avatar_thumbnail" in self.chat_result['abs_object'].keys() else UNKNOWN
        self.is_verified: Union[bool, UNKNOWN] = self.chat_result['abs_object']['is_verified'] if "abs_object" in self.keys and "is_verified" in self.chat_result['abs_object'].keys() else UNKNOWN
        self.is_verified: Union[bool, UNKNOWN] = self.chat_result['abs_object']['is_deleted'] if "abs_object" in self.keys and "is_deleted" in self.chat_result['abs_object'].keys() else UNKNOWN
        self.is_verified: Union[bool, UNKNOWN] = self.chat_result['is_blocked'] if "is_blocked" in self.keys else UNKNOWN

    def __str__(self):
        return json.dumps(self.chat_result, indent=2)
    
class LastMessageType(object):
    def __init__(self, message_result) -> None:
        self.messagex: Dict = message_result
        self.message: Union[Dict] = self.messagex['last_message'] if "last_message" in self.messagex.keys() else {}
        self.message_keys: list = list(self.message.keys())
        self.message_id: Union[str] = self.message['message_id'] if "message_id" in self.message_keys else ""
        self.text: Union[str] = self.message['text'] if "text" in self.message_keys else ""
        self.type: Union[str] = self.message['type'] if "type" in self.message_keys else ""
        self.author_object_guid: Union[str, UNKNOWN] = self.message['author_object_guid'] if "author_object_guid" in self.message_keys else UNKNOWN
        self.author_title: Union[str, UNKNOWN] = self.message['author_title'] if "author_title" in self.message_keys else UNKNOWN
        self.author_type: Union[str, UNKNOWN] = self.message['author_type'] if "author_type" in self.message_keys else UNKNOWN
        self.is_mine: Union[bool, UNKNOWN] = self.message['is_mine'] if "is_mine" in self.message_keys else UNKNOWN

    def __str__(self):
        return json.dumps(self.message, indent=2)
    
class AbsObject(object):
    def __init__(self, abs_result: dict) -> None:
        self.abs = abs_result
        self.keys: list = list(self.abs.keys())
        self.object_guid: Union[str, UNKNOWN] = self.abs['object_guid'] if "object_guid" in self.keys else UNKNOWN
        self.type: Union[str, UNKNOWN] = self.abs['type'] if "type" in self.keys else UNKNOWN
        self.first_name: Union[str, UNKNOWN] = self.abs['first_name'] if "first_name" in self.keys else UNKNOWN
        self.avatar_thumbnail: Union[Avatar, UNKNOWN] = Avatar(self.abs['avatar_thumbnail']) if "avatar_thumbnail" in self.keys else UNKNOWN
        self.is_verified: Union[bool, UNKNOWN] = self.abs['is_verified'] if "is_verified" in self.keys else UNKNOWN
        self.is_deleted: Union[bool, UNKNOWN] = self.abs['is_deleted'] if "is_deleted" in self.keys else UNKNOWN
    
class XUpdater(object):
    def __init__(self, Auth, Key, UpdateResult, UseFakeUserAgent: bool = True, Proxy = None) -> None:
        self.auth = str(Auth)
        self.key = str(Key)
        self.UpResult: Dict = UpdateResult
        self.ufa = UseFakeUserAgent
        self.proxy = Proxy
        self.networkClient = XNetwork(self.auth, self.key, self.proxy)

        self.data: Dict = self.UpResult['data'] if "data" in self.UpResult.keys() else {}
        self.on_chat: Union[list] = self.data['chats'] if "chats" in list(self.data.keys()) else {}
        self.last_chat: Union[Dict] = self.on_chat[0] if len(self.on_chat) != 0 else []
        self.chat: Union[ChatType, Dict] = ChatType(self.last_chat) if len(list(self.last_chat.keys())) != 0 else {}
        self.last_message: Union[LastMessageType, Dict] = LastMessageType(self.last_chat) if len(self.last_chat.keys()) != 0 and "last_message" in self.last_chat else {}
        self.abs_object: Union[AbsObject, UNKNOWN] = AbsObject(self.last_chat['abs_object']) if len(self.last_chat.keys()) != 0 and "abs_object" in self.last_chat else UNKNOWN
        self.message_id: Union[str] = self.last_message.message_id if not self.last_message == {} else ""
        self.text: Union[str] = self.last_message.text if not self.last_message == {} else ""
        self.is_mine: Union[bool, UNKNOWN] = self.last_message.is_mine
        self.author_object_guid: Union[str, UNKNOWN] = self.last_message.author_object_guid
        self.author_title: Union[str, UNKNOWN] = self.last_message.author_title
        self.author_type: Union[str, UNKNOWN] = self.last_message.author_type

    @property
    def reply_info(self) -> ReplyObjects:
        replx = self.networkClient.option({"object_guid": self.chat.id, "message_ids": [self.message_id]}, "getMessagesByID")['data']['messages'][0]
        if not 'reply_to_message_id' in replx.keys():
            return ReplyObjects({"is_reply": False})
        else:
            data = self.networkClient.option({"object_guid": self.chat.id, "message_ids": [replx['reply_to_message_id']]}, "getMessagesByID")['data']['messages'][0]
            data['is_reply'] = True
            return ReplyObjects(data)
        
    @property
    async def reply_info_asyncly(self) -> ReplyObjects:
        replx = await self.networkClient.asyncOption({"object_guid": self.chat.id, "message_ids": [self.message_id]}, "getMessagesByID")
        replx = replx['data']['messages'][0]
        if not 'reply_to_message_id' in replx.keys():
            return ReplyObjects({"is_reply": False})
        else:
            data = await self.networkClient.asyncOption({"object_guid": self.chat.id, "message_ids": [replx['reply_to_message_id']]}, "getMessagesByID")
            data = data['data']['messages'][0]
            data['is_reply'] = True
            return ReplyObjects(data)
    
    def reply(self, text: str, markdown: bool = True):
        if markdown:
            metadata = Markdown(text=text).metadata

            metadata['object_guid'] = self.chat.id
            metadata['reply_to_message_id'] = self.message_id
            metadata['rnd'] = random.random() * 1e6 + 1

            return self.networkClient.option(metadata, "sendMessage", self.ufa)
        
        else:
            return self.networkClient.option({"object_guid": self.chat.id,
                                        "text": text,
                                        "reply_to_message_id": self.message_id,
                                        "rnd": random.random() * 1e6 + 1})
        
    async def replyAsyncly(self, text: str, markdown: bool = True):
        if markdown:
            metadata = Markdown(text=text).metadata

            metadata['object_guid'] = self.chat.id
            metadata['reply_to_message_id'] = self.message_id
            metadata['rnd'] = random.random() * 1e6 + 1

            return await self.networkClient.asyncOption(metadata, "sendMessage", self.ufa)
        
        else:
            return await self.networkClient.asyncOption({"object_guid": self.chat.id,
                                        "text": text,
                                        "reply_to_message_id": self.message_id,
                                        "rnd": random.random() * 1e6 + 1})

    def __str__(self):
        return json.dumps(self.UpResult['data'] if "data" in list(self.UpResult.keys()) else self.UpResult, indent=2)

class OldUpdater(object):
    def __init__(self, Auth, Key, UpdateResult, UseFakeUserAgent: bool = True, Proxy = None) -> None:
        self.auth = str(Auth)
        self.key = str(Key)
        self.UpResult = UpdateResult
        self.ufa = UseFakeUserAgent
        self.proxy = Proxy
        self.networkClient = XNetwork(self.auth, self.key, self.proxy)

    def __str__(self):
        return json.dumps(self.UpResult, indent=2)
    
    @property
    def status(self) -> str:
        return self.UpResult['status'] if "status" in self.UpResult.keys() else "Null"

    @property
    def status_det(self) -> str:
        return self.UpResult['status_det']if "status_det" in self.UpResult.keys() else "Null"
    
    @property
    def data(self) -> dict:
        return self.UpResult['data'] if "data" in self.UpResult.keys() else "Null"
    
    @property
    def chats(self) -> list:
        return self.data['chats'] if type(self.data) == dict and "chats" in self.data.keys() else "Null"
    
    @property
    def getLastChat(self) -> dict:
        return self.chats[0] if type(self.data) == dict and "chats" in self.data.keys() and not len(self.chats) == 0 else ""
    
    @property
    def lastChat(self) -> dict:
        return self.chats[0] if type(self.data) == dict and "chats" in self.data.keys() and not len(self.chats) == 0 else ""

    @property
    def newState(self) -> int:
        return self.data['new_state'] if type(self.data) == dict and 'new_state' in self.data.keys() else "Null"
    
    @property
    def timeStamp(self) -> str:
        return self.data['time_stamp'] if type(self.data) == dict and 'time_stamp' in self.data.keys() else "Null"
    
    @property
    def objectGuid(self) -> str:
        return self.getLastChat['object_guid'] if type(self.getLastChat) == dict and 'object_guid' in self.getLastChat.keys() else "Null"
    
    @property
    def chatId(self) -> str:
        return self.getLastChat['object_guid'] if type(self.getLastChat) == dict and 'object_guid' in self.getLastChat.keys() else "Null"
    
    @property
    def access(self) -> list:
        return self.getLastChat['access'] if type(self.getLastChat) == dict and 'access' in self.getLastChat.keys() else "Null"
    
    @property
    def countUnseen(self) -> int:
        return self.getLastChat['count_unseen'] if type(self.getLastChat) == dict and 'count_unseen' in self.getLastChat.keys() else "Null"
    
    @property
    def isMute(self) -> bool:
        return self.getLastChat['is_mute'] if type(self.getLastChat) == dict and 'is_mute' in self.getLastChat.keys() else "Null"
    
    @property
    def isPinned(self) -> bool:
        return self.getLastChat['is_pinned'] if type(self.getLastChat) == dict and 'is_pinned' in self.getLastChat.keys() else "Null"
    
    @property
    def getLastMessage(self) -> dict:
        return self.getLastChat['last_message'] if type(self.getLastChat) == dict and 'last_message' in self.getLastChat.keys() else "Null"
    
    @property
    def lastMessage(self) -> dict:
        return self.getLastChat['last_message'] if type(self.getLastChat) == dict and 'last_message' in self.getLastChat.keys() else "Null"
    
    @property
    def lastMessageId(self) -> str:
        return self.getLastMessage['message_id'] if type(self.getLastMessage) == dict and 'message_id' in self.getLastMessage.keys() else "Null"
    
    @property
    def messageId(self) -> str:
        return self.getLastMessage['message_id'] if type(self.getLastMessage) == dict and 'message_id' in self.getLastMessage.keys() else "Null"
    
    @property
    def lastMessageType(self) -> str:
        return self.getLastMessage['message_id'] if type(self.getLastMessage) == dict and 'message_id' in self.getLastMessage.keys() else "Null"
    
    @property
    def text(self) -> str:
        return self.getLastMessage['text'] if type(self.getLastMessage) == dict and 'text' in self.getLastMessage.keys() else "Null"
    
    @property
    def authorObjectGuid(self) -> str:
        return self.getLastMessage['author_object_guid'] if type(self.getLastMessage) == dict and 'author_object_guid' in self.getLastMessage.keys() else "Null"
    
    @property
    def isMine(self) -> str:
        return self.getLastMessage['is_mine'] if type(self.getLastMessage) == dict and 'is_mine' in self.getLastMessage.keys() else "Null"
    
    @property
    def authorTitle(self) -> str:
        return self.getLastMessage['author_title'] if type(self.getLastMessage) == dict and 'author_title' in self.getLastMessage.keys() else "Null"
    
    @property
    def authorType(self) -> str:
        return self.getLastMessage['author_type'] if type(self.getLastMessage) == dict and 'author_type' in self.getLastMessage.keys() else "Null"
    
    @property
    def lastSeenMyMid(self) -> str:
        return self.getLastChat['last_seen_my_mid'] if type(self.getLastChat) == dict and 'last_seen_my_mid' in self.getLastChat.keys() else "Null"
    
    @property
    def lastSeenPeerMid(self) -> str:
        return self.getLastChat['last_seen_peer_mid'] if type(self.getLastChat) == dict and 'last_seen_peer_mid' in self.getLastChat.keys() else "Null"
    
    @property
    def lastChatStatus(self) -> str:
        return self.getLastChat['status'] if type(self.getLastChat) == dict and 'status' in self.getLastChat.keys() else "Null"
    
    @property
    def time(self) -> str:
        return self.getLastChat['time'] if type(self.getLastChat) == dict and 'time' in self.getLastChat.keys() else "Null"
    
    @property
    def pinnedMessageId(self) -> str:
        return self.getLastChat['pinned_message_id'] if type(self.getLastChat) == dict and 'pinned_message_id' in self.getLastChat.keys() else "Null"
    
    @property
    def absObjects(self) -> dict:
        return self.getLastChat['abs_object'] if type(self.getLastChat) == dict and 'abs_object' in self.getLastChat.keys() else "Null"
    
    @property
    def absObjectGuid(self) -> str:
        return self.absObjects['object_guid'] if type(self.absObjects) == dict and 'object_guid' in self.absObjects.keys() else "Null"
    
    @property
    def absType(self) -> str:
        return self.absObjects['type'] if type(self.absObjects) == dict and 'type' in self.absObjects.keys() else "Null"
    
    @property
    def absTitle(self) -> str:
        return self.absObjects['title'] if type(self.absObjects) == dict and 'title' in self.absObjects.keys() else "Null"
    
    @property
    def absAvatarThumbnail(self) -> dict:
        return self.absObjects['avatar_thumbnail'] if type(self.absObjects) == dict and 'avatar_thumbnail' in self.absObjects.keys() else "Null"
    
    @property
    def absAvatarFileId(self) -> str:
        return self.absAvatarThumbnail['file_id'] if type(self.absAvatarThumbnail) == dict and 'file_id' in self.absAvatarThumbnail.keys() else "Null"
    
    @property
    def absAvatarMime(self) -> str:
        return self.absAvatarThumbnail['mime'] if type(self.absAvatarThumbnail) == dict and 'mime' in self.absAvatarThumbnail.keys() else "Null"
    
    @property
    def absAvatarDcId(self) -> str:
        return self.absAvatarThumbnail['dc_id'] if type(self.absAvatarThumbnail) == dict and 'dc_id' in self.absAvatarThumbnail.keys() else "Null"
    
    @property
    def absAvatarAccessHashRec(self) -> str:
        return self.absAvatarThumbnail['access_hash_rec'] if type(self.absAvatarThumbnail) == dict and 'access_hash_rec' in self.absAvatarThumbnail.keys() else "Null"
    
    @property
    def isVerified(self) -> bool:
        return self.absObjects['is_verified'] if type(self.absObjects) == dict and 'is_verified' in self.absObjects.keys() else "Null"
    
    @property
    def isDeleted(self) -> bool:
        return self.absObjects['is_deleted'] if type(self.absObjects) == dict and 'is_deleted' in self.absObjects.keys() else "Null"
    
    @property
    def isBlocked(self) -> bool:
        return self.getLastChat['is_blocked'] if type(self.getLastChat) == dict and 'is_blocked' in self.getLastChat.keys() else "Null"
    
    @property
    def lastDeletedMid(self) -> str:
        return self.getLastChat['last_deleted_mid'] if type(self.getLastChat) == dict and 'last_deleted_mid' in self.getLastChat.keys() else "Null"
    
    @property
    def groupMyLastSendTime(self) -> int:
        return self.getLastChat['group_my_last_send_time'] if type(self.getLastChat) == dict and 'group_my_last_send_time' in self.getLastChat.keys() else "Null"
    
    @property
    def pinnedMessageIds(self) -> list:
        return self.getLastChat['pinned_last_message_ids'] if type(self.getLastChat) == dict and 'pinned_last_message_ids' in self.getLastChat.keys() else "Null"
    
    @property
    def replyMessageInfo(self) -> ReplyObjects:
        replx = self.networkClient.option({"object_guid": self.chatId, "message_ids": [self.lastMessageId]}, "getMessagesByID")['data']['messages'][0]
        if not 'reply_to_message_id' in replx.keys():
            return ReplyObjects({"is_reply": False})
        else:
            data = self.networkClient.option({"object_guid": self.chatId, "message_ids": [replx['reply_to_message_id']]}, "getMessagesByID")['data']['messages'][0]
            data['is_reply'] = True
            return ReplyObjects(data)

    def replyTo(self, text: str) -> dict:
        """
        Send a Message and reply on that
        """
        meta = Markdown(text=text).metadata
        meta['object_guid'] = self.chatId
        meta['reply_to_message_id'] = self.messageId
        meta['rnd'] = random.random() * 1e6 + 1
        return self.networkClient.option(meta, "sendMessage", self.ufa)
