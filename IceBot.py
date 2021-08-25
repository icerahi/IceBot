from fbchat import Client,log
from fbchat.models import *
 
from time import sleep
 
# reading username
username ="icebotq@gmail.com"
# reading password
password = "RahiNusu420"
group_id = 4272940849453841
# client = Client(myUsername, myPassword)

# print("Own id: {}".format(client.uid))
# #change chat themecolor of group
# client.changeThreadColor(ThreadColor.BILOBA_FLOWER, thread_id=thread_id)
# #send message of group
# #client.send(Message(text="Hi Sir it is me ur BOT! RoboPathshala"), thread_id= 4272940849453841, thread_type=ThreadType.GROUP)

# #get message id and send love react
# message_id = client.send(Message(text='message'), thread_id=thread_id, thread_type=ThreadType.GROUP)
# client.reactToMessage(message_id, MessageReaction.LOVE)

#Echobot
from fbchat import log, Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    
    def send_message(self,text,author_id,author_name,thread_id,thread_type):
        self.send(Message(
        text=f"@{author_name} {text}", mentions=[Mention(author_id,offset=0, length=len(author_name)+1)]
    ), thread_id=thread_id, thread_type=thread_type)        
        sleep(2)
        self.stopListening()
        
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        author = self.fetchUserInfo(author_id)
        author_name = author[author_id].first_name

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        #print(message_object,thread_id,thread_type.name)
        # If you're not the author, echo
        if author_id != self.uid:
            self.message = message_object.text.lower()
            if self.message.startswith("#"):
                if ('sleepnow') in  self.message:
                    self.send(Message(text="Going to sleep"), thread_id=thread_id, thread_type=thread_type)    
                    sleep(2)
                    self.stopListening()
                    # self.logout
                
                if ("how are you") in self.message:
                    self.send_message("I'm fine and you?",author_id,author_name,thread_id,thread_type)
            
            

            else:
               
                
                self.send(Message(
        text=f"@{author_name} {message_object.text}", mentions=[Mention(author_id, offset=0,length=len(author_name)+1)]
    ), thread_id=thread_id, thread_type=thread_type)
               # print("I will print message_object now")
                # print(message_object)
                # print(self.fetchUserInfo(author_id))
               # print(type(message_object))
              
 

client = EchoBot(username,password)
client.listen()