package cn.com.netis.dcd.parser.regression.stock.lxzq.thirdparty;

import java.io.IOException;

import org.junit.Test;

import cn.com.netis.dcd.parser.regression.RegressionInit;
import cn.com.netis.taux.regression.BatchSuite;
import cn.com.netis.taux.regression.RegressionSuite;

/**
 * The type Lxzq third party test.
 */
public class LxzqThirdPartyTest {

    /**
     * Test.
     *
     * @throws IOException the io exception
     */
    @Test
    public void test() throws IOException {
        suite.play();
    }

    static {
        RegressionInit.init();
    }

    /** The Constant suite. */
    private static final RegressionSuite suite = new BatchSuite(LxzqThirdPartyTest.class,
            new String[]{"-m", "batch", "-i", "file", "-o", "btr"});
}

