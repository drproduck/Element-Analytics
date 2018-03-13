from libs.parser.tokenizer import LogTokenizer

# Test it out
tomcat = \
    "Aug 20 06:38:51 hfvm dchq_tomcat[38866]: 2017-08-20 13:38:51.412  \
INFO 1 --- [cTaskExecutor-5] s.m.r.HostPingNotificationMessageHandler : \
Received server ping for [13bb3a25-0b37-4167-b2eb-476720ebb0a5]"

solr = \
    "Aug 20 06:39:02 hfvm dchq_solr[38866]: \
390914427 [qtp101478235-1906] INFO  \
org.apache.solr.update.processor.LogUpdateProcessor  – \
[collection1] webapp=/solr path=/update params={wt=javabin&version=2} \
{add=[2c9180865de18be7015de2cd718808ff (1576257551186526208)]} 0 2"

solr_commit = \
    'Aug 20 06:39:02 hfvm dchq_solr[38866]: \
#011commit{dir=NRTCachingDirectory\
(MMapDirectory@/opt/solr-4.10.4/example/solr/collection1/data/index \
lockFactory=NativeFSLockFactory@/opt/solr-4.10.4/example/solr/collection1/data/index; \
maxCacheMB=48.0 maxMergeSizeMB=4.0),segFN=segments_7d8f,generation=343743}'

nginx = \
    'Aug 20 06:59:23 hfvm dchq_nginx[38866]: \
164.132.91.13 - - [20/Aug/2017:13:59:23 +0000] \
"GET /landing/index_co.html HTTP/1.1" 200 4616 "-" "Firefox/24.0" "-"#015'

#new lexer instance
lexer = LogTokenizer().build()

# Give the lexer some input
lexer.input(solr)
print(solr)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

print()
lexer.input(tomcat)
# Tokenize
print(tomcat)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

print()
lexer.input(nginx)
# Tokenize
print(nginx)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

print()
lexer.input(solr_commit)
# Tokenize
print(solr_commit)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)