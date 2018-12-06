from apis import hello

from . import evaluation




evaluation.add_url_rule('/', 'hello', hello)