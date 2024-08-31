from .network import XNetwork
import random
import json
import re

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

class ReplyObjects(object):
    def __init__(self, jsres: dict = {}):
        self.data = jsres

    def __str__(self) -> dict:
        return json.dumps(self.data, indent=2)

    @property
    def messageId(self) -> str:
        return self.jsres['message_id'] if 'message_id' in self.jsres.keys() else "null"
    
    @property
    def text(self) -> str:
        return self.jsres['text'] if 'text' in self.jsres.keys() else "null"
    
    @property
    def reply_to_message_id(self) -> str:
        return self.jsres['reply_to_message_id'] if 'reply_to_message_id' in self.jsres.keys() else "null"
    
    def messageTime(self) -> str:
        return self.jsres['time'] if 'time' in self.jsres.keys() else "null"
    
    def getType(self) -> str: 
        return self.jsres['type'] if 'type' in self.jsres.keys() else "null"
    
    def getAuthorType(self) -> str:
        return self.jsres['author_type'] if 'author_type' in self.jsres.keys() else "null"
    
    def isAllowTranscription(self) -> bool:
        return self.jsres['allow_transcription'] if 'allow_transcription' in self.jsres.keys() else "null"

    def isEdited(self) -> bool:
        return self.jsres['is_edited'] if 'is_edited' in self.jsres.keys() else "null"
    
    def isReply(self) -> bool:
        return self.jsres['is_reply']

class XUpdater(object):
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
        return self.chats[0] if type(self.data) == dict and "chats" in self.data.keys() else "Null"
    
    @property
    def lastChat(self) -> dict:
        return self.chats[0] if type(self.data) == dict and "chats" in self.data.keys() else "Null"

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
