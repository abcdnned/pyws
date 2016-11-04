package cn.com.netis.dcd.parser.decoder.{{type}}.{{ioc}}.{{custname}};

import cn.com.netis.dcd.parser.huygens.field.DecodeField;
import cn.com.netis.dcd.parser.huygens.field.Encoding;
import cn.com.netis.dcd.parser.huygens.field.bank.BankFieldFactory;
import cn.com.netis.dp.commons.lang.ValueType;

/**
 * The Class {{cons}}.
 */
class {{cons}} {

    /** The Constant DEFS. */
    private static final Object[][][] DEFS = {
        { { 0 ,null,1,Encoding.CHARSET}, { "fldname", ValueType.STRING, false, "fldname" } },
    };

    /** The Constant FIELDS. */
    public static final DecodeField[] FIELDS = new DecodeField[DEFS.length];

    static {
        BankFieldFactory.buildFields(FIELDS, DEFS);
    }

}
