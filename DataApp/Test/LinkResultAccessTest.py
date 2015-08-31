__author__ = 'mwu'

import Test
from SQLAccess.LinkResultAccess import Link_Result_Access


class LinkResultAccesstest(Test.TestCase):

    def testGetLinkResult(self):
        batch = 10
        lra = Link_Result_Access("dms-cr-3","crlinking","LinkResultsService","WeeblesW0bble")
        lrCol = lra.get_link_result(57000000000001,batch)
        self.assertEqual(len(lrCol),batch)


if __name__ == '__main__':
    Test.main()