import time
import stomp

import logging
logger = logging.getLogger('stomp.py')
logger.setLevel(logging.ERROR)

logger = logging.getLogger('classrec.communication')
logger.setLevel(logging.INFO)

class CommListener(stomp.ConnectionListener):        
    def on_error(self, headers, message):
        logger.error('An error has been occurred with the broker: %s', message)
    
    def on_message(self, headers, message):
        logger.info('Message received: %s', message)
        
        
class CommSession:
    def __init__(self, address='localhost', port=61613, destination="test", username=None, password=None):
        self.address = address
        self.port= port
        self.dest = destination
        self.username = username
        self.password = password
        self._listener = None
    
    def set_listener(self, listener):
        self._listener = listener
        
    def connect(self):
        logger.info("Connecting to broker: %s:%d%s", self.address, self.port, self.dest)
        try:
            if self.password != None and self.username != None:
                self._conn = stomp.Connection(host_and_ports=[ (self.address, self.port) ], 
                                          user=self.username, passcode=self.password)
            else:
                self._conn = stomp.Connection([ (self.address, self.port) ])
                
            self._conn.set_listener('listener', self._listener)
            self._conn.start()
            self._conn.connect(wait=True)
            self._conn.subscribe(destination=self.dest, ack='auto', id=1)
            logger.info("Connected!")
        except:
            logger.exception("Error on connecting to broker.")
        
        
    def disconenct(self):
        logger.info("Disconnecting from broker.")
        try:
            self._conn.disconnect()
            logger.info("Disconnected!")
        except:
            logger.exception("Error on disconnecting from broker.")
        
    def send_message(self, message):
        logger.debug('Sending Message.')
        self._conn.send(body=message, destination=self.dest)
        
        
def test():
    class MyListener(CommListener):
        def on_message(self, headers, message):
            print 'Message from MyListener: "' + message + '"'
            
    session = CommSession('200.18.98.19', 61613, "/topic/TVMONITOR", 'guest', 'guest')
    session.set_listener(MyListener())
    session.connect()
    
    notification_message = \
        '{ "notification" :\
           { "channel" : 6,\
             "confidence" : 0.9,\
             "id" : 1,\
             "label" : "Alguma coisa aconteceu?",\
             "options" : [\
                { "id" : 1, "label" : "Sim" },\
                { "id" : 2, "label" : "Nao" } ],\
            "time" : 20,\
            "type" : "timer"\
           }\
        }'
    
    session.send_message(notification_message)
    while True:
        time.sleep(2)
    session.disconenct()
    
if __name__ == "__main__":
    test()