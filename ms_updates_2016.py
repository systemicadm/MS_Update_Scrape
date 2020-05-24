import feedparser

UpdateFeed = feedparser.parse("https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss")

entry = UpdateFeed.entries[0]

print = entry['title']
print = "------Update Link--------"
print = entry['link']
print = "******"

#import feedparser
#UpdateFeed = feedparser.parse("https://support.microsoft.com/app/content/api/content/feeds/sap/en-us/c3a1be8a-50db-47b7-d5eb-259debc3abcc/rss")
#entry = UpdateFeed.entries[0]

#print = entry.keys()
