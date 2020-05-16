import feedparser
NewsFeed = feedparser.parse("https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss")
entry = NewsFeed.entries[1]

print = entry.keys()
#import feedparser

#NewsFeed = feedparser.parse("https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss")

#entry = NewsFeed.entries[1]

#print entry.published
#print "******"
#print entry.summary
#print "------News Link--------"
#print entry.link