package cn.com.netis.dcd.parser.regression.{{rootflod}}.{{pkgname}};

import java.io.IOException;

import org.junit.Test;

import cn.com.netis.dcd.parser.regression.RegressionInit;
import cn.com.netis.taux.regression.BatchSuite;
import cn.com.netis.taux.regression.RegressionSuite;

/**
 * The Class {{testname}}.
 */
public final class {{testname}} {

    /**
     * Test normal.
     *
     * @throws IOException the IO exception
     */
    @Test
    public void testNormal() throws IOException {
        suite.play();
    }

    static {
        RegressionInit.init();
    }

    /** The Constant suite. */
    private static final RegressionSuite suite = new BatchSuite({{testname}}.class,
            new String[] { "-m", "batch", "-i", "file", "-o", "btr" });

}
