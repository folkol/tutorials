from pprint import pprint

from pubsub import *

post_message('Matte', 'Lorem')
for n in range(50):
    post_message('Dunder', f'Lorem Ipsum #{n} #foo')
    post_message('Mart', f'Lorem Ipsum Dolor #{n}')
post_message('Stahl', 'Lorem Ipsum Dolor Sit #foo')
post_message('Matte', 'Lorem Ipsum Dolor Sit Amet')

follow('Matte', 'Dunder')
follow('Matte', 'Mart')
follow('Mart', 'Matte')

if __name__ == '__main__':
    # pprint(posts)
    # pprint(user_posts['Matte'])
    # pprint(followers)
    # pprint(following)
    # pprint(posts_for_user('Matte', 6))
    pprint(search('#foo', 6))
