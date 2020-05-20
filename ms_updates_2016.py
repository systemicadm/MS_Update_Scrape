import feedparser
UpdateFeed = feedparser.parse("https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss")
entry = UpdateFeed.entries[1]

print = entry.keys()
#import feedparser

#UpdateFeed = feedparser.parse("https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss")

#entry = UpdateFeed.entries[1]

#print entry.published
#print "******"
#print entry.summary
#print "------Update Link--------"
#print entry.link