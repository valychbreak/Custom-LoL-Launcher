import subprocess
import argparse

from client_setup import setup


parser = argparse.ArgumentParser(prog='launcher', usage='%(prog)s [options]')
parser.add_argument('game_dir', help='Root directory to the game (where LeagueClient.exe is located)')
parser.add_argument('--username', nargs='?', help='Your account\'s username')
parser.add_argument('--locale', nargs='?', help='Locale. Example: en_GB, ru_RU, etc.')
parser.add_argument('--region', nargs='?', help='Region. Example: RU, EUNE, etc.')
# parser.print_help()

args = parser.parse_args()

game_path = args.game_dir
username = args.username
locale = args.locale
region = args.region

print("Setting up LoL path to: {}".format(game_path))
print("Setting up LoL settings to username: {}, locale: {}, region: {}".format(username, locale, region))

setup(game_path, username, locale, region)

subprocess.Popen([game_path + '/LeagueClient.exe'])
