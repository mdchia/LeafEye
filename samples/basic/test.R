testdat <- read.csv("testout.csv", header=FALSE)

hist(testdat[,2],main="",xlab="Temperature (C)", ylab="Pixels", xaxt = "n")
axis(1, at = seq(21, 31, 2))
