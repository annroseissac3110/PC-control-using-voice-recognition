def News():
    
    import requests    
    def NewsFromBBC():
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "d1597081db5541b69a233437b33c855e"
        }
        main_url = " https://newsapi.org/v1/articles"
    
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    
        article = open_bbc_page["articles"]
    

        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        for i in range(len(results)):
            print(i + 1, results[i])
    
        from win32com.client import Dispatch
        speak = Dispatch("SAPI.Spvoice")
        speak.Speak(results)                

    NewsFromBBC()