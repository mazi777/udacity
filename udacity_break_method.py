# applying break method to the loop; aim: to create a string made with elements of a list; the string lenght should be equal 140

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:

    if len(news_ticker+headline+" ")<=140:
        print("lenght of news_ticker will be less than 140, so add the headline element")
        news_ticker+=headline+" "
        print("lenght of news_ticker after adding: {}".format(len(news_ticker)))
    elif len(news_ticker + headline)>140:
        print("after adding a next headline we will have len= {}". format(len(news_ticker + headline)))
        news_ticker=news_ticker+headline
        news_ticker=news_ticker[:140]
        print("string len after cutting the last element: {}".format(len(news_ticker)))
        break

           #   news_ticker=news_ticker[:(len(news_ticker)-140)]
      #  print("lenght after cutting: {}".format(len(news_ticker)))


print(news_ticker)
print("lenght of news_ticker: {}".format(len(news_ticker)))
