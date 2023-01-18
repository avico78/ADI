from app_config.settings import Settings
def main(name):
    # Use a breakpoint in the code line below to debug your script.
    settings = Settings()
    print(settings.get('databases.mongo.ENGINE'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
