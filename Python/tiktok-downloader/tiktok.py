try:
    import random, os, threading, time, requests, sys
    from pystyle import *
except Exception as e:
    print(f'ERROR [{e}]')


class Main():
    try:
        def download(url):
            """
            Downloading video
            :param url:
            :return:
            """
            global x, videocount
            try:
                with open(f'./download{random.randint(1000, 9999)}.mp4', 'wb') as out_file:
                    videobytes = requests.get(f'{url}.mp4', stream=True)
                    out_file.write(videobytes.content)
                    x += 1
                    os.system(f"title Tiktok Downloader ^| Downloaded: {x} ^| Folder: ./download")
            except:
                pass


        def start():
            global x
            """
            main function
            """

            os.system('cls' if os.name == 'nt' else "clear")
            os.system(f"title Tiktok Downloader ^| STATUS: LOADING")

            Anime.Fade(Center.Center("Tiktok Downloader"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=2)
            Anime.Fade(Center.Center("THE INPUT IS A RANDOM ID FROM A VIDEO OF THE TARGET ACCOUNT"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=5)

            user = Write.Input(Center.Center("id > "), Colors.blue_to_red, interval=0)

            os.system('cls' if os.name == 'nt' else "clear")
            print(Colorate.Vertical(Colors.blue_to_red, Center.Center("DOWNLOADING...")))

            if not os.path.exists(f'backup'):
                os.makedirs(f'backup')

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            }

            secUid = requests.get(f"https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{user}%5D", headers=headers).json()["aweme_details"][0]["author"]["sec_uid"]

            max_cursor = "0"
            x = 0

            while True:
                try:
                    """
                    While True to get all user videos
                    """

                    url = f"https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/post/?sec_user_id={secUid}&count=33&device_id=9999999999999999999&max_cursor={max_cursor}&aid=1180"
                    headers = {
                        "accept-encoding": "gzip",
                        "user-agent": "com.ss.android.ugc.trill/240303 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004;tt-ok/3.10.0.2)",
                        "x-gorgon": "0"
                    }
                    response = requests.request("GET", url, headers=headers)
                    try:
                        if response.json()["status_msg"] == "No more videos":
                            break
                    except:
                        try:
                            max_cursor = response.json()["max_cursor"]
                        except:
                            break

                    videos = response.json()["aweme_list"]

                    for vid in videos:
                        url = vid["video"]["play_addr"]["url_list"][0]
                        threading.Thread(target=Main.download, args=(url,)).start()
                except:
                    print(Colorate.Vertical(Colors.blue_to_red, Center.Center("FINISHED...")))
                    break

    except Exception as e:
        os.system('cls' if os.name == 'nt' else "clear")
        print(f'ERROR {e}')
        input()
        sys.exit()


if __name__ == '__main__':
    Main.start()
