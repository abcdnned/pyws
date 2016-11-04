import fdsfdsafdsaf
import fdsfdsafdsaf
import fdsfdsafdsaf
import fdsfdsafdsaf
import fdsfdsafdsaf
import fdsfdsafdsaf


public class DecoderName extends AbstractDecoder {

    @Override
    public boolean decodeClearBuffer(final ByteBuffer clearBuffer, final DecodeStatus decodeStatus,
        final ProtocolAttribute protAttr) {
    }

    @Override
    public void cleanupDecoder() {
        // do nothing
    }

    /**
     * Get name.
     *
     * @return name as String.
     */
    public String getName() {
        return name;
    }

    /**
     * Set name.
     *
     * @param name the value to set.
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Get age.
     *
     * @return age as long.
     */
    public long getAge() {
        return age;
    }

    /**
     * Set age.
     *
     * @param age the value to set.
     */
    public void setAge(long age) {
        this.age = age;
    }




    private long age;

    private String name;
}
