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
            from traceback import print_exc
            print_exc()
            diffusion_client.disconnect()
        except Exception:
            from traceback import print_exc
            print_exc()
            diffusion_client.disconnect()


def williamhill():
    topics = [
        'sportsbook/football/{id:d}/i18n/en-gb/commentary'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/cards/red'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/cards/yellow'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/corners'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/goals'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/penalties'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/shots/offTarget'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/shots/onTarget'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/shots/onWoodwork'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/substitutions'.format(id=0),
        'sportsbook/football/{id:d}/stats/away/throwIns'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/cards/red'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/cards/yellow'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/corners'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/goals'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/penalties'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/shots/offTarget'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/shots/onTarget'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/shots/onWoodwork'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/substitutions'.format(id=0),
        'sportsbook/football/{id:d}/stats/home/throwIns'.format(id=0),
        'sportsbook/football/{id:d}/stats/homeTeamPossesion'.format(id=0),
        'sportsbook/football/{id:d}/stats/period'.format(id=0),
        'sportsbook/football/{id:d}/stats/time'.format(id=0),
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
            from traceback import print_exc
            print_exc()
            diffusion_client.disconnect()
        except Exception:
            from traceback import print_exc
            print_exc()
            diffusion_client.disconnect()


if __name__ == '__main__':
    main(argv)
