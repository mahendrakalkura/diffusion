from sys import argv

from twisted.internet import reactor

from modules import diffusion


def main(options):
    length = len(options)
    if length < 2:
        return
    if options[1] == '--bet365':
        bet365()
        reactor.run()
        return
    if options[1] == '--williamhill':
        williamhill()
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
        topics=topics,
    )
    if diffusion_client.can_connect():
        try:
            diffusion_client.connect()
        except KeyboardInterrupt:
            diffusion_client.disconnect()
        except Exception:
            diffusion_client.disconnect()


def williamhill():
    topics = [
        'sportsbook/football/0/i18n/en-gb/commentary',
        'sportsbook/football/0/stats/away/cards/red',
        'sportsbook/football/0/stats/away/cards/yellow',
        'sportsbook/football/0/stats/away/corners',
        'sportsbook/football/0/stats/away/goals',
        'sportsbook/football/0/stats/away/penalties',
        'sportsbook/football/0/stats/away/shots/offTarget',
        'sportsbook/football/0/stats/away/shots/onTarget',
        'sportsbook/football/0/stats/away/shots/onWoodwork',
        'sportsbook/football/0/stats/away/substitutions',
        'sportsbook/football/0/stats/away/throwIns',
        'sportsbook/football/0/stats/home/cards/red',
        'sportsbook/football/0/stats/home/cards/yellow',
        'sportsbook/football/0/stats/home/corners',
        'sportsbook/football/0/stats/home/goals',
        'sportsbook/football/0/stats/home/penalties',
        'sportsbook/football/0/stats/home/shots/offTarget',
        'sportsbook/football/0/stats/home/shots/onTarget',
        'sportsbook/football/0/stats/home/shots/onWoodwork',
        'sportsbook/football/0/stats/home/substitutions',
        'sportsbook/football/0/stats/home/throwIns',
        'sportsbook/football/0/stats/homeTeamPossesion',
        'sportsbook/football/0/stats/period',
        'sportsbook/football/0/stats/time',
    ]
    diffusion_client = diffusion.DiffusionClient(
        'wss://scoreboards-ssl.williamhill.com/diffusion?v=4&ty=WB',
        '4',
        session_url=None,
        protocol=None,
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
