# DSL-6740U File Upload
Upload file to DLink DSL-6740U routers
I used this to run static tcpdump (also uploaded to this project)

## The steps for uploading a file
### Log in and get shell
    telnet 192.168.1.1
Authenticate
    sh

### Upload temp httpd configuration
On router telnet:
    cat > /tmp/httpd.conf
Paste content of httpd.conf (verify line endings)

### Run temp httpd configuration on port 8081
On router telnet:
    busybox httpd -c /tmp/httpd.conf -h /tmp -p 8081

### Upload uploader CGI
On router telnet:
    cat > /tmp/uploader.cgi
Paste content of uploader.cgi (verify line endings)
    chmod +x /tmp/uploader.cgi

### Upload file
    python uploader.py <FILE>

### Use the file
On router telnet:
    /tmp/uploaded_file

### When you're done - don't leave the httpd open!
On router telnet:
    ps | grep httpd
    kill <8081 httpd pid>


### For sniffing with tcpdump
    /tmp/uploaded_file -ni br0 "not tcp port 23"
