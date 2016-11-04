package cn.com.netis.dcd.parser.decoder.{{type}}.{{ioc}}.{{custname}};

import java.nio.ByteBuffer;

import cn.com.netis.dcd.parser.decoder.AbstractDecoder;
import cn.com.netis.dcd.parser.huygens.decode.DecodeStatus;
import cn.com.netis.dcd.parser.huygens.decode.ProtocolAttribute;

final class {{decoder}} extends AbstractDecoder {

    @Override
    public boolean decodeClearBuffer(ByteBuffer clearBuffer, DecodeStatus decodeStatus,
            ProtocolAttribute protAttr) {
        return true;
    }

    @Override
    public void cleanupDecoder() {

    }

}
