df1 <- read.csv('./Q1_getdata_data_ss06hid.csv')

subdf <- subset(df1, VAL == 24)
print(nrow(subdf))

agricultureLogical <- c(df1$ACR == 3 & df1$AGS == 6)
print(which(agricultureLogical, TRUE))

print(strsplit(names(df1), "wgtp"))


library(jpeg)
img <- readJPEG("./Q7_getdata_jeff.jpeg", native=TRUE)
print(quantile(img, probs=c(.3, .8)))


library("XML")
xml <- xmlToDataFrame("./Q8_data.xml")
# блять я їбав
i <- 0
for (row in xml$zipcode) {
    if (row == 21231) {
        i <- i + 1
    }
}
print(i)


df2 <- read.csv("./Q9_getdata_data_GDP.csv")
df2$GDP <- gsub(" ", "", df2$GDP)
df2$GDP <- gsub(",", "", df2$GDP)
df2$GDP <- as.numeric(as.character(df2$GDP))
print(mean(df2$GDP))


library(quantmod)
library(lubridate)
amzn <- getSymbols("AMZN", auto.assign=FALSE)
sampleTimes <- data.frame(index(amzn))
year <- data.frame(yea = as.numeric(format(sampleTimes$index.amzn.,'%Y')), day = wday(sampleTimes$index.amzn.))
result1 <- subset(year, yea == 2012)
result2 <- subset(result1, day == 2)
print(nrow(result1))
print(nrow(result2))