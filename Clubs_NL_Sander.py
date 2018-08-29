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
                  headless_browser=False,
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
    session.like_by_locations(['159361027964473/club-fix/',
                               '793500/club-vie-rotterdam/',
                               '213325339/abe-club-lounge/',
                               '145053/air-amsterdam/',
                               '220618189/mondial/',
                               '376234/jimmy-woo/',
                               '551884066/club-villa-thalia/',
                               '8383345/the-vip-room/',
                               '1631651210489819/nora-rotterdam/'
                               '128895423/club-cell/',
                               '145053/air-amsterdam/',
                               '494265620/bret/',
                               '2494477/chicago-social-club/',
                               '2198949/club-nl/',
                               '35568742/club-nyx/',
                               '956326/de-clubup/',
                               '618037300/amsterdam-escape/',
                               '625085156/john-doe/',
                               '942644716/the-box/',
                               '561379756/w-amsterdam/',
                               '220618189/mondial/',
                               '9230705/graanbeurs-breda/',
                               '1014074294/steck-podium-club-bar/',
                               '434808773588336/millers-cocktail-kitchen/',
                               '5402494/danzig-den-haag/',
                               '249663720/club-ruis/',
                               '612001/club-stalker-official/',
                               '1031056/superdisco/',
                               '857434232/the-suicide-club/',
                               '10635059/beachclub-bloomingdale/',
                               '1997197/beachclub-vroeger/',
                               '7646385/toffler/',
                               '234483204/clooney-zoetermeer/',
                               '3166421/whoosah-beachclub/',
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
