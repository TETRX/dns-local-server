from config import ADDRESS, PORT, QUESTION_ADDRESS
from dnslib.server import DNSServer, DNSLogger
from dnslib.dns import RR,A
import dnslib
import time

class HardcodedResolver:
    ANSWER="192.168.0.1"
    def resolve(self,request,handler):
        reply=request.reply()
        if request.questions[0].qname==QUESTION_ADDRESS:
            fake_rr=RR(rname=QUESTION_ADDRESS, ttl=5, rdata=A(HardcodedResolver.ANSWER))
            reply.add_answer(fake_rr)
        else:
            reply.header.rcode=dnslib.RCODE.REFUSED
        return reply
resolver=HardcodedResolver()

logger = DNSLogger(prefix=False)

server = DNSServer(resolver, port=PORT, address=ADDRESS, logger=logger, tcp=False)
server.start_thread()

time.sleep(100.0)