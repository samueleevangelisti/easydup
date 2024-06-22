'''
sync.py
'''
import sys
import json
import click

from utils import prints
from utils import commands
from utils import paths
from utils import datetimes
from classes.core_configs import CoreConfigs



@click.command()
@click.argument('is-force-sync', type=bool)
def _main(is_force_sync):
    '''
    Core command. Use easydup instead
    '''
    core_configs_path = paths.resolve_path(paths.folder_path(__file__), 'core-configs.json')
    print(f"core_configs_path is `{core_configs_path}`")

    if not paths.is_entry(core_configs_path):
        with open(core_configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(CoreConfigs(datetimes.create(1970, 1, 1)).to_dict(), indent=2))
    if paths.is_folder(core_configs_path):
        prints.red(f"`{core_configs_path}` is a folder")
        sys.exit(1)

    with open(core_configs_path, 'r', encoding='utf-8') as file:
        core_configs = CoreConfigs.from_dict(json.loads(file.read()))

    today_datetime = datetimes.today()
    if (core_configs.sync_datetime < today_datetime) or is_force_sync:
        commands.run('git pull', True)
        core_configs.sync_datetime = today_datetime
        with open(core_configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(core_configs.to_dict(), indent=2))



if __name__ == '__main__':
    # pylint: disable-next=no-value-for-parameter
    _main()
