val str=io.Source.fromFile("9.8.txt").mkString
print(str)
val pattern=""".*?(image).*?src="([a-z]+)".*"""".r
for(pattern(image,src) <- pattern findAllIn str) print(image,src)
