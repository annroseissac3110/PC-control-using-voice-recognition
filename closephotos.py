def ClosePhotos():
    from delete.main import message
    from AppOpener import close
    app_name = message.replace("close ","").strip()
    close(app_name, match_closest=True, output=False) 
    print(""+app_name+" closed")