package cn.com.netis.dcd.parser.regression.{{location}};

import java.io.IOException;

import org.junit.Test;

import cn.com.netis.dcd.parser.regression.RegressionInit;
import cn.com.netis.taux.regression.BatchSuite;
import cn.com.netis.taux.regression.RegressionSuite;

/**
 * The Class {{testname}}.
 */
public class {{testname}} {

    /** The Constant SUITE. */
    private static final RegressionSuite SUITE;

    /**
     * Test normal.
     *
     * @throws IOException Signals that an I/O exception has occurred.
     */
    @Test
    public final void testNormal() throws IOException {
        SUITE.play();
    }

    static {
        RegressionInit.init();
        SUITE = new BatchSuite({{testname}}.class,
                new String[] { "-m", "batch", "-i", "file", "-o", "btr" });
    }
}
