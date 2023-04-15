import socket
import hashlib

# global defination
target_host = ""
target_port =


def create_connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    client.connect((target_host, target_port));
    return client;


def get_request():
    client = create_connection();

    request = "GET / HTTP/1.1\r\nHOST: {host}:{port}\r\n\r\n".format(host=target_host, port=target_port);
    print "[*]Sending GET request to " + target_host + ":" + str(target_port);

    # Sent Request
    client.send(request);
    response = client.recv(4096);
    client.close();

    read_response(response);

def post_request(data, session):
    print "[*]Post Request Sending...";
    client = create_connection();
    content_type = "application/x-www-form-urlencoded";
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36";
    content_length = len("hash=" + str(data));

    request = "POST / HTTP/1.1\r\nHOST: {host}:{port}\r\nContent-Type: {content_type}\r\nUser-Agent: {agent}\r\nCookie: {cookie}\r\nContent-Length: {content_length}\r\n\r\nhash={hash}".format(
        host=target_host, port=target_port, content_type=content_type,
        agent=user_agent, cookie=session, content_length=content_length, hash=data);

    client.send(request);
    response = client.recv(4069);
    client.close();

    print(request)
    print(response)


def read_response(response):

    # Read Session
    session_start = response.find("PHPSESSID=");
    session_end = response.find(";");
    session = response[session_start:session_end];

    keyIndex_start = response.find("<h3 align='center'>")
    keyIndex_end = response.find("</h3>")

    key = response[keyIndex_start + 19:keyIndex_end]

    md5 = hashlib.md5()
    md5.update(key)

    key = md5.hexdigest()
    print(key)
    post_request(key, session);

# Main Method
get_request();
