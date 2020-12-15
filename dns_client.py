import dnslib
from config import ADDRESS,PORT, QUESTION_ADDRESS

q = dnslib.DNSRecord.question(QUESTION_ADDRESS)
answer=q.send(ADDRESS, port=PORT, timeout=1)

parsed_answer=dnslib.DNSRecord.parse(answer)
print(parsed_answer)