from Inic_conection import autenficar

yt = autenficar()
canal_response = yt.channels().list(mine=True, part='snippet,contentDetails,statistics').execute()

for canal in canal_response["items"]:
    upl_list_id = canal["contentDetails"]["relatedPlaylists"]["uploads"]

    print("Videos en ID: %s" % upl_list_id)

    playlist_list_request = yt.playlistItems().list(
        playlistId=upl_list_id,
        part="snippet",
        maxResults=50
    )
    while playlist_list_request:
        playlist_list_response = playlist_list_request.execute()

        for playlist_item in playlist_list_response["items"]:
            titulo = playlist_item["snippet"]["title"]
            video_id = playlist_item["snippet"]["resourceId"]["videoId"]
            print("%s (%s)" % (titulo, video_id))

        playlist_list_request = yt.playlistItems().list_next(
                playlist_list_request, playlist_list_response)

    print
