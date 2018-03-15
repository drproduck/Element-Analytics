import unittest
from libs.parser.tokenizer import LogTokenizer


class TestTokenizer(unittest.TestCase):

    lexer = LogTokenizer().build()

    def test_tomcat(self):
        tomcat = "Aug 20 06:38:51 hfvm dchq_tomcat[38866]: 2017-08-20 13:38:51.412  INFO 1 --- [cTaskExecutor-5] s.m.r.HostPingNotificationMessageHandler : Received server ping for [13bb3a25-0b37-4167-b2eb-476720ebb0a5]"
        tokens = self.extract_toks(tomcat, self.lexer)
        self.assertEqual(tokens[0], "Aug 20 06:38:51")
        self.assertEqual(tokens[1], "dchq_tomcat[38866]")
        self.assertEqual(tokens[2], "INFO")
        self.assertEqual(tokens[3], "s.m.r.HostPingNotificationMessageHandler")
        self.assertEqual(tokens[4], "Received server ping for [13bb3a25-0b37-4167-b2eb-476720ebb0a5]")

    def test_solr(self):
        solr = "Aug 20 06:39:02 hfvm dchq_solr[38866]: 390914431 [qtp101478235-1906] INFO  org.apache.solr.update.UpdateHandler  – start commit{,optimize=false,openSearcher=true,waitSearcher=true,expungeDeletes=false,softCommit=false,prepareCommit=false}"
        tokens = self.extract_toks(solr, self.lexer)
        self.assertEqual(tokens[0], "Aug 20 06:39:02")
        self.assertEqual(tokens[1], "dchq_solr[38866]")
        self.assertEqual(tokens[2], "INFO")
        self.assertEqual(tokens[3], "org.apache.solr.update.UpdateHandler")
        self.assertEqual(tokens[4], "start commit{,optimize=false,openSearcher=true,waitSearcher=true,expungeDeletes=false,softCommit=false,prepareCommit=false}")

    def test_solr_commit(self):
        solr_commit = "Aug 20 06:39:40 hfvm dchq_solr[38866]: #011commit{dir=NRTCachingDirectory(MMapDirectory@/opt/solr-4.10.4/example/solr/collection1/data/index lockFactory=NativeFSLockFactory@/opt/solr-4.10.4/example/solr/collection1/data/index; maxCacheMB=48.0 maxMergeSizeMB=4.0),segFN=segments_7d8h,generation=343745}"
        tokens = self.extract_toks(solr_commit, self.lexer)
        self.assertEqual(tokens[0], "Aug 20 06:39:40")
        self.assertEqual(tokens[1], "dchq_solr[38866]")
        self.assertEqual(tokens[2], "011commit{dir=NRTCachingDirectory(MMapDirectory@/opt/solr-4.10.4/example/solr/collection1/data/index lockFactory=NativeFSLockFactory@/opt/solr-4.10.4/example/solr/collection1/data/index; maxCacheMB=48.0 maxMergeSizeMB=4.0),segFN=segments_7d8h,generation=343745}")

    def test_nginx(self):
        nginx = 'Aug 20 06:59:22 hfvm dchq_nginx[38866]: 164.132.91.13 - - [20/Aug/2017:13:59:22 +0000] "GET / HTTP/1.1" 302 0 "-" "Firefox/24.0" "-"#015'
        tokens = self.extract_toks(nginx, self.lexer)
        self.assertEqual(tokens[0], "Aug 20 06:59:22")
        self.assertEqual(tokens[1], "dchq_nginx[38866]")
        self.assertEqual(tokens[2], "164.132.91.13")
        self.assertEqual(tokens[3], '[20/Aug/2017:13:59:22 +0000] "GET / HTTP/1.1" 302 0 "-" "Firefox/24.0" "-"#015')

    @staticmethod
    def extract_toks(string, lexer):
        lexer.input(string)
        tokens = [tok.value for tok in lexer]
        return tokens


if __name__ == "__main__":
    unittest.main()