import java.io.PrintWriter

object TouchIgnore extends App {
    if (args.length < 1) println("please input a directionary path, not end with /")
    else {
        val path = args(0) + "/.gitignore"
        val out = new PrintWriter(path)
        out.println("*~")
        out.println("*.swp")
        out.println(".*")
        out.println("target")
        out.flush()
        out.close()
        println("touch ignore success")
    }
}
