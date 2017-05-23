from sys import argv

from twisted.internet import reactor

from modules import diffusion


def main(options):
    if options[1] == '--bet365':
        bet365()
        reactor.run()
        return
    if options[1] == '--williamhill':
        williamhill(options[2])
        reactor.run()
        return


def bet365():
    topics = [
        '__host',
        'CONFIG_1_3',
        'HL_L1_Z3_C1_W1',
        'HR_L1_Z3_C1_W1',
        'InPlay_1_3',
        'LHInPlay_1_3',
        'Media_l1_Z3',
        'OVInPlay_1_3',
        'XI_1_3',
        'XL_L1_Z3_C1_W1',
    ]
    diffusion_client = diffusion.DiffusionClient(
        'wss://premws-pt1.365lpodds.com/zap/',
        '1',
        session_url='https://www.bet365.com/',
        protocol='zap-protocol-v1',
        headers={},
        topics=topics,
    )
    if diffusion_client.can_connect():
        try:
            diffusion_client.connect()
        except KeyboardInterrupt:
            diffusion_client.disconnect()
        except Exception:
            diffusion_client.disconnect()


def williamhill(id):
    headers = {
        'Origin': 'http://cachescoreboards.williamhill.com',
    }
    topics = [
        'sportsbook/football/%s/i18n/en-gb/commentary' % id,
        'sportsbook/football/%s/stats/away/cards/red' % id,
        'sportsbook/football/%s/stats/away/cards/yellow' % id,
        'sportsbook/football/%s/stats/away/corners' % id,
        'sportsbook/football/%s/stats/away/goals' % id,
        'sportsbook/football/%s/stats/away/penalties' % id,
        'sportsbook/football/%s/stats/away/shots/offTarget' % id,
        'sportsbook/football/%s/stats/away/shots/onTarget' % id,
        'sportsbook/football/%s/stats/away/shots/onWoodwork' % id,
        'sportsbook/football/%s/stats/away/substitutions' % id,
        'sportsbook/football/%s/stats/away/throwIns' % id,
        'sportsbook/football/%s/stats/home/cards/red' % id,
        'sportsbook/football/%s/stats/home/cards/yellow' % id,
        'sportsbook/football/%s/stats/home/corners' % id,
        'sportsbook/football/%s/stats/home/goals' % id,
        'sportsbook/football/%s/stats/home/penalties' % id,
        'sportsbook/football/%s/stats/home/shots/offTarget' % id,
        'sportsbook/football/%s/stats/home/shots/onTarget' % id,
        'sportsbook/football/%s/stats/home/shots/onWoodwork' % id,
        'sportsbook/football/%s/stats/home/substitutions' % id,
        'sportsbook/football/%s/stats/home/throwIns' % id,
        'sportsbook/football/%s/stats/homeTeamPossesion' % id,
        'sportsbook/football/%s/stats/period' % id,
        'sportsbook/football/%s/stats/time' % id,
    ]
    diffusion_client = diffusion.DiffusionClient(
        'wss://scoreboards-ssl.williamhill.com/diffusion?v=4&ty=WB',
        '4',
        session_url=None,
        protocol=None,
        headers=headers,
        topics=topics,
    )
    if diffusion_client.can_connect():
        try:
            diffusion_client.connect()
        except KeyboardInterrupt:
            diffusion_client.disconnect()
        except Exception:
            diffusion_client.disconnect()


if __name__ == '__main__':
    main(argv)
