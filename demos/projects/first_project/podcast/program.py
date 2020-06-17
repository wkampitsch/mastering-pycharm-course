import service


def main():
    print("Welcome to the talk python info downloader.")
    print()

    episode_count = service.download_info()
    print(f"Found {episode_count} episodes!")
    print()

    for show_id in range(1, episode_count + 1):
        info = service.get_episode(show_id)
        print(f'{info.show_id}. {info.title}')


if __name__ == '__main__':
    main()
