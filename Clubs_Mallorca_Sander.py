import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'sendergrem'
insta_password = '0653440096'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				  delimit_by_numbers=True,
				   max_followers=100000,
				    max_following=1000000,
				     min_followers=150,
				      min_following=77)
    session.set_do_comment(False, percentage=10)
    session.set_comments([])
    session.set_dont_include([])
    session.set_dont_like([])
    session.set_delimit_liking(enabled=True, max=6000, min=50)

    # actions
    session.like_by_locations(['294113899/club-nl-mallorca/',
                               '286188453/the-beachhouse-mallorca/',
                               '786933408/shooters-el-arenal/',
                               '1022056388/de-heeren-van-amstel-mallorca/',
                               '432015589/megapark-komplex-mallorca-offizielle-seite/',
                               '152319604831465/riu-palace-mallorca/',
                               '416262354/titos-palma/',
                               '1340533/mar-salada/',
                               '983820509/cc-palma-de-mallorca/]',
                               '1033668836/discotheek-veronica-el-arenal-mallorca/',
                               ] , amount=100)                


except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
