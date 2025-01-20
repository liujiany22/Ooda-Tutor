import os.path

import main
import json


generate_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/openapi.json'))


if __name__ == '__main__':
    with open(generate_path, 'w') as f:
        f.write(json.dumps(main.app.openapi(), indent=4))
    print(f'The openapi.json file is generated in {generate_path}, '
          'which should be the frontend directory.')
    print('If there is the openapi.json file, run `npm run generate-client` in the frontend directory')
