import libs.parser.logparser as parser
import libs.parser.logfields as lf
import unittest


with open("./test_log", 'r') as f:
    input = [line for line in f]

golden = [
    {
        lf.DATE : "Aug 20 06:38:51",
        lf.NAME : "dchq_tomcat[38866]",
        lf.TYPE : "INFO",
        lf.INFO : "s.m.r.HostPingNotificationMessageHandler",
        lf.MSSG : "Received server ping for [13bb3a25-0b37-4167-b2eb-476720ebb0a5]"
    },
    {
        lf.DATE : "Aug 20 06:39:02",
        lf.NAME : "dchq_solr[38866]",
        lf.TYPE : None,
        lf.INFO : None,
        lf.MSSG : "011commit{dir=NRTCachingDirectory(MMapDirectory@/opt/solr-4.10.4/example/solr/collection1/data/index lockFactory=NativeFSLockFactory@/opt/solr-4.10.4/example/solr/collection1/data/index; maxCacheMB=48.0 maxMergeSizeMB=4.0),segFN=segments_7d8f,generation=343743}"
    },
    {
        lf.DATE : "Aug 20 06:39:02",
        lf.NAME : "dchq_solr[38866]",
        lf.TYPE : "INFO",
        lf.INFO : "org.apache.solr.update.processor.LogUpdateProcessor",
        lf.MSSG : "[collection1] webapp=/solr path=/update params={waitSearcher=true&commit=true&softCommit=false&wt=javabin&version=2} {commit=} 0 81"
    },
    {
        lf.DATE : "Aug 20 06:59:22",
        lf.NAME : "dchq_nginx[38866]",
        lf.TYPE : None,
        lf.INFO : "164.132.91.13",
        lf.MSSG : '[20/Aug/2017:13:59:22 +0000] "GET / HTTP/1.1" 302 0 "-" "Firefox/24.0" "-"#015'
    }
]


class Test_Parser(unittest.TestCase):

    def test_parseline(self):
        self.assertEqual(parser.parse_line(input[0]), golden[0])
        self.assertEqual(parser.parse_line(input[1]), golden[1])
        self.assertEqual(parser.parse_line(input[2]), golden[2])
        self.assertEqual(parser.parse_line(input[3]), golden[3])

    def test_parsefile(self):
        self.assertEqual(parser.parse_file("./test_log"), golden)


if __name__ == "__main__":
    unittest.main()