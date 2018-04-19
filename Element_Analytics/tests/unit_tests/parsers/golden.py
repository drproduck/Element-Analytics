import libs.parser.tokenizer as lf

golden = [
    {
        lf._DATE : "Aug 20 06:38:51",
        lf._NAME : "dchq_tomcat[38866]",
        lf._TYPE : "INFO",
        lf._INFO : " s.m.r.HostPingNotificationMessageHandler",
        lf._MSSG : " : Received server ping for [13bb3a25-0b37-4167-b2eb-476720ebb0a5]"
    },
    {
        lf._DATE : "Aug 20 06:39:02",
        lf._NAME : "dchq_solr[38866]",
        lf._TYPE : "INFO",
        lf._INFO : "  org.apache.solr.update.processor.LogUpdateProcessor",
        lf._MSSG : " – [collection1] webapp=/solr path=/update params={waitSearcher=true&commit=" +
                  "true&softCommit=false&wt=javabin&version=2} {commit=} 0 81"
    },
    {
        lf._DATE : "Aug 20 06:39:02",
        lf._NAME : "dchq_solr[38866]",
        lf._TYPE : "",
        lf._INFO : "",
        lf._MSSG : ": #011commit{dir=NRTCachingDirectory(MMapDirectory@/opt/solr-4.10.4" +
                "/example/solr/collection1/data/index lockFactory=NativeFSLockFactory@/" +
                "opt/solr-4.10.4/example/solr/collection1/data/index; maxCacheMB=48.0 " +
                "maxMergeSizeMB=4.0),segFN=segments_7d8f,generation=343743}"
    },
    {
        lf._DATE : "Aug 20 06:59:22",
        lf._NAME : "dchq_nginx[38866]",
        lf._TYPE : "",
        lf._INFO : " 164.132.91.13",
        lf._MSSG : ' - - [20/Aug/2017:13:59:22 +0000] "GET / HTTP/1.1" 302 0 "-" "Firefox/24.0" "-"#015'
    },
    {
        lf._DATE: "Aug 22 09:08:35",
        lf._NAME: "dchq_nginx[38866]",
        lf._TYPE: "",
        lf._INFO: " 67.207.110.135",
        lf._MSSG: ': *10746 an upstream response is buffered to a temporary file /var/cache/nginx/proxy_temp/2/06/0000000062 while reading upstream, client: 67.207.110.135, server: , request: "GET /js/all-index.min.js HTTP/1.1", upstream: "http://172.17.0.7:8080/js/all-index.min.js", host: "hypercloud.run", referrer: "https://hypercloud.run/"#015'

    },
    {
        lf._DATE : "Aug 22 11:13:54",
        lf._NAME : "dchq_redis[38866]",
        lf._TYPE : "",
        lf._INFO : "",
        lf._MSSG : " * Background saving terminated with success"
    },
    {
        lf._DATE : "Aug 22 10:58:00",
        lf._NAME : "dchq_iaas[38866]",
        lf._TYPE : "INFO",
        lf._INFO : " com.dchq.iaas.amqp.Sender",
        lf._MSSG : " - Sending response [{}]..."
    },
    {
        lf._DATE: "Aug 18 09:40:35",
        lf._NAME: "dchq_iaas[38866]",
        lf._TYPE: "",
        lf._INFO: " org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer",
        lf._MSSG: ": #011at org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer$AsyncMessageProcessingConsumer.run(SimpleMessageListenerContainer.java:1143)"
    },
    {
        lf._DATE: "Aug 20 23:39:39",
        lf._NAME: "dchq_iaas[38866]",
        lf._TYPE: "",
        lf._INFO: " org.springframework.web.client.HttpClientErrorException",
        lf._MSSG: ": org.springframework.web.client.HttpClientErrorException: 401"
    },
    {
        lf._DATE: "Aug 20 06:47:01",
        lf._NAME: "CRON[39294]",
        lf._TYPE: "",
        lf._INFO: "",
        lf._MSSG: ": (root) CMD (test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly ))"
    },
    {
        lf._DATE: "Aug 20 23:17:01",
        lf._NAME: "CRON[35691]",
        lf._TYPE: "",
        lf._INFO: "",
        lf._MSSG: ": (root) CMD (   cd / && run-parts --report /etc/cron.hourly)"
    },
    {
        lf._DATE: "Aug 22 11:00:59",
        lf._NAME: "dchq_rabbitmq[38866]",
        lf._TYPE: "",
        lf._INFO: "",
        lf._MSSG: ""
    },
    {
        lf._DATE: "Aug 22 16:51:08",
        lf._NAME: "dchq_rabbitmq[38866]",
        lf._TYPE: "",
        lf._INFO: " 172.17.0.3",
        lf._MSSG: ": accepting AMQP connection <0.21265.2> (10.0.1.183:32806 -> 172.17.0.3:5671)"
    }

]