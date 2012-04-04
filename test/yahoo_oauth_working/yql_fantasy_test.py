import yql
import oauthlib.oauth
import yahoo.oauth, yahoo.yql, yahoo.application

# Yahoo! OAuth Credentials - http://developer.yahoo.com/dashboard/
CONSUMER_KEY      = 'dj0yJmk9VTRsQXk1NDBqMEFTJmQ9WVdrOWNsaDFOVzlxTmpJbWNHbzlNak16TkRVME9UWXkmcz1jb25zdW1lcnNlY3JldCZ4PWRm'
CONSUMER_SECRET   = '97bdbac507462a4680984dab9e9abc10dd3def7e'
APPLICATION_ID    = 'rXu5oj62'
CALLBACK_URL      = 'http://fantasy-football-hybrid-draft.appspot.com/'

def main():
    """
    Demonstrates fetching of oauth tokens from yahoo apis
    """

    # make public request for data oauth requests for profiles
    oauthapp = yahoo.application.OAuthApplication(CONSUMER_KEY, CONSUMER_SECRET, APPLICATION_ID, CALLBACK_URL)

    y3 = yql.ThreeLegged(CONSUMER_KEY, CONSUMER_SECRET)
    query = "select * from fantasysports.players where game_key='nfl' and start='75' and count='5'"

    #request_token, auth_url = y3.get_token_and_auth_url()

    print '* Obtain a request token ...'
    request_token = oauthapp.get_request_token(CALLBACK_URL)

    # authorize the request token
    print '\n* Authorize the request token ...'
    print '\nAuthorization URL:\n\n%s' % oauthapp.get_authorization_url(request_token)
    verifier = raw_input('\nGo to above URL and authorize.\n\nVerifier from response URL: ')

    # now the token we get back is an access token
    print '\n* Obtain an access token ...'
    access_token = oauthapp.get_access_token(request_token, verifier.strip())
    print '\nkey: %s' % str(access_token.key)
    print 'secret: %s' % str(access_token.secret)
    print 'yahoo guid: %s' % str(access_token.yahoo_guid)

    #access_token = y3.get_access_token(request_token, verifier)

    response = y3.execute(query, token=access_token)


    print response.count

    if response.count > 0:
        print response.rows[-1]

if __name__ == '__main__':
    main()
