golden = [
    {
        "date" : "Aug 20 06:38:51",
        "sv_name" : "dchq_tomcat[38866]",
        "type" : "INFO",
        "metainfo" : " s.m.r.HostPingNotificationMessageHandler",
        "message" : " : Received server ping for [13bb3a25-0b37-4167-b2eb-476720ebb0a5]"
    },
    {
        "date" : "Aug 20 06:39:02",
        "sv_name" : "dchq_solr[38866]",
        "type" : "INFO",
        "metainfo" : "  org.apache.solr.update.processor.LogUpdateProcessor",
        "message" : " – [collection1] webapp=/solr path=/update params={waitSearcher=true&commit=" +
                  "true&softCommit=false&wt=javabin&version=2} {commit=} 0 81"
    },
    {
        "date" : "Aug 20 06:39:02",
        "sv_name" : "dchq_solr[38866]",
        "type" : "",
        "metainfo" : "",
        "message" : ": #011commit{dir=NRTCachingDirectory(MMapDirectory@/opt/solr-4.10.4" +
                "/example/solr/collection1/data/index lockFactory=NativeFSLockFactory@/" +
                "opt/solr-4.10.4/example/solr/collection1/data/index; maxCacheMB=48.0 " +
                "maxMergeSizeMB=4.0),segFN=segments_7d8f,generation=343743}"
    },
    {
        "date" : "Aug 20 06:59:22",
        "sv_name" : "dchq_nginx[38866]",
        "type" : "",
        "metainfo" : " 164.132.91.13",
        "message" : ' - - [20/Aug/2017:13:59:22 +0000] "GET / HTTP/1.1" 302 0 "-" "Firefox/24.0" "-"#015'
    },
    {
        "date": "Aug 22 09:08:35",
        "sv_name": "dchq_nginx[38866]",
        "type": "",
        "metainfo": " 67.207.110.135",
        "message": ': *10746 an upstream response is buffered to a temporary file /var/cache/nginx/proxy_temp/2/06/0000000062 while reading upstream, client: 67.207.110.135, server: , request: "GET /js/all-index.min.js HTTP/1.1", upstream: "http://172.17.0.7:8080/js/all-index.min.js", host: "hypercloud.run", referrer: "https://hypercloud.run/"#015'

    },
    {
        "date" : "Aug 22 11:13:54",
        "sv_name" : "dchq_redis[38866]",
        "type" : "",
        "metainfo" : "",
        "message" : " * Background saving terminated with success"
    },
    {
        "date" : "Aug 22 10:58:00",
        "sv_name" : "dchq_iaas[38866]",
        "type" : "INFO",
        "metainfo" : " com.dchq.iaas.amqp.Sender",
        "message" : " - Sending response [{}]..."
    },
    {
        "date": "Aug 18 09:40:35",
        "sv_name": "dchq_iaas[38866]",
        "type": "",
        "metainfo": " org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer",
        "message": ": #011at org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer$AsyncMessageProcessingConsumer.run(SimpleMessageListenerContainer.java:1143)"
    },
    {
        "date": "Aug 20 23:39:39",
        "sv_name": "dchq_iaas[38866]",
        "type": "",
        "metainfo": " org.springframework.web.client.HttpClientErrorException",
        "message": ": org.springframework.web.client.HttpClientErrorException: 401"
    },
    {
        "date": "Aug 20 06:47:01",
        "sv_name": "CRON[39294]",
        "type": "",
        "metainfo": "",
        "message": ": (root) CMD (test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly ))"
    },
    {
        "date": "Aug 20 23:17:01",
        "sv_name": "CRON[35691]",
        "type": "",
        "metainfo": "",
        "message": ": (root) CMD (   cd / && run-parts --report /etc/cron.hourly)"
    },
    {
        "date": "Aug 22 11:00:59",
        "sv_name": "dchq_rabbitmq[38866]",
        "type": "",
        "metainfo": "",
        "message": ""
    },
    {
        "date": "Aug 22 16:51:08",
        "sv_name": "dchq_rabbitmq[38866]",
        "type": "",
        "metainfo": " 172.17.0.3",
        "message": ": accepting AMQP connection <0.21265.2> (10.0.1.183:32806 -> 172.17.0.3:5671)"
    }

]