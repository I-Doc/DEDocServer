import os
import sys

from dedoc.app import app, db


def run():
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


def not_found():
    print('command not found')


def migrate():
    print('applying migrations...')
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    from seed import seed

    try:
        command = sys.argv[1]
    except Exception:
        print('command not found... default will be chosen (run)')
        command = 'run'

    commands = {
        'run': run,
        'migrate': migrate,
        'seed': seed
    }
    commands.get(command, not_found)()
